# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect


def api_doc_home(request):
    """
    接口功能说明: 接口文档首页
    --------------------------------------------
    接口逻辑说明:
    --------------------------------------------
    修改人        修改时间          修改原因
    --------------------------------------------
    Nick         2020-11-20        新建
    --------------------------------------------
    """
    host = request.META['HTTP_HOST']
    api_doc_url = f'http://{host}/apidoc/index.html'

    return redirect(api_doc_url)


def bad_request(request, exception, template_name='400.html'):
    return render(request, template_name)


def permission_denied(request, exception, template_name='403.html'):
    return render(request, template_name)


def page_not_found(request, exception, template_name='404.html'):
    return render(request, template_name)


# 注意这里没有 exception 参数
def server_error(request, template_name='500.html'):
    return render(request, template_name)
