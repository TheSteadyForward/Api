# -*- coding: utf-8 -*-

import logging
import time
import traceback

from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.sessions.models import Session
from django.utils.deprecation import MiddlewareMixin  # Django 1.11.x
from django.conf import settings

from libs.utils.ajax import ajax_fail
from apps.common.common import request_interrupt

SESSION_KEY = '_auth_user_id'
PROJECT_ID = settings.PROJECT_ID
PROJECT_DB_NAME = settings.PROJECT_DB_NAME
tracer = settings.TRACER

log = logging.getLogger('account.middleware')

not_login_urls = ["/apidoc/", "/weblog/", "/upload_media/", "/template/"]


class AuthenticationMiddleware(MiddlewareMixin):
    """"""
    @request_interrupt
    def process_request(self, request):
        # 过滤 跨域、post请求参数为空的请求
        r_method = request.method
        if r_method == 'OPTIONS' or (r_method == 'POST' and not request.body):
            return HttpResponse()

        role = 0    # 0 默认值 1 学生端请求 2 教师端请求
        path = str(request.path)

        for obj in not_login_urls:
            if path.startswith(obj):
                return None

        session_key = ""
        if request.GET.get("sessionid"):
            session_key = request.GET.get("sessionid")
        if not session_key:
            if request.META.get("HTTP_SESSIONID"):
                session_key = request.META.get("HTTP_SESSIONID")

        uid = request.GET.get("uid", 0)
        if session_key:
            try:
                s = Session.objects.get(pk=session_key, expire_date__gt=timezone.now())
                uid = s.get_decoded().get('_auth_user_id')
            except:
                log.info(traceback.format_exc())
                return ajax_fail(error=9, message="会话过期，请重新登录！")

        if not uid:
            return None

        request.uid = int(uid)
        print(request.uid, request.get_full_path())

        return None

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        功能说明: 请求视图时执行
        -------------------------------
        修改人     修改时间
        -------------------------------
        Nick        2020-08-19
        """
        request.start_time = time.time()
        if settings.TRACER_APP == 1 and settings.YH_ENV == 3:  # 测试覆盖率
            try:
                response = tracer.runfunc(view_func, request, *view_args, **view_kwargs)
                results = tracer.results()
                results.write_results(summary=False, coverdir='/code/', show_missing=True)
                return response
            except:
                log.exception(traceback.format_exc(), extra=dict(req=request))  # 将错误日志发送到阿里云日志服务
                return ajax_fail(error='', message=settings.ERROR_MESSAGES)

    def process_response(self, request, response):
        """
        功能说明: 请求返回响应时执行
        -------------------------------
        修改人     修改时间
        -------------------------------
        Nick        2020-08-19
        """
        try:
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
            response["Access-Control-Allow-Headers"] = "Origin, X-Requested-With, Content-Type, Accept"
            response["Access-Control-Max-Age"] = "1728000"
            response["Access-Control-Expose-Headers"] = 'Date'  # 允许前端获取响应头里面的date字段 保持与服务器时间统一
        except Exception as e:
            log.debug("process_response1:%s" % e)
        return response

    def process_exception(self, request, exception):
        """
        功能说明:请求view视图函数抛出异常处理
        -------------------------------
        修改人     修改时间
        --------------------------------
        Nick        2020-08-19
        """
        for obj in not_login_urls:
            if request.path.startswith(obj):
                return None

        print(exception)
        log.exception(exception, extra=dict(req=request))  # 将错误日志发送到阿里云日志服务

        if not request.uid:
            return ajax_fail(error=9, message="会话过期，请重新登录！")

        return ajax_fail(error="500", message=u"服务器开小差了~~")
