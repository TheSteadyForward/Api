# -*- coding: utf-8 -*-

import cProfile
import line_profiler
# from memory_profiler import profile as mproflie, show_results, LineProfiler, choose_backend
import pstats   # 自定义报表
from contextlib import contextmanager
from django.utils.deprecation import MiddlewareMixin  # Django 1.11.x


from django.conf import settings


# 代码分析使用的中间件
# 生产环境分析：中间件中会有慢查询使用time进行初步筛选(每次调用都需要判断)，超过3秒即写入慢查询
# 开发环境分析：第一步：同生产环境
#             第二步：当发现耗时较长的接口时，使用第二步进行详细代码分析
# 分析代码占用内存:

class ExamineMiddleware(MiddlewareMixin):

    def should_show_stats(self, request):
        if settings.DEBUG:
            if 'cprof' in request.GET:
                return 1
            elif 'lprof' in request.GET:
                return 2
            elif 'mprof' in request.GET:
                return 3
            else:
                return False

    def process_view(self, request, view_func, view_args, view_kwargs):

        @contextmanager
        def c_profiling(sortby='tottime', limit=10):
            """使用cProfile进行分析，统计函数的执行时间
                适用于较为耗时较长的程序，主要开销在对每个调用函数的计时
                注：limit应该是int型，默认只显示总时间(由于自身耗时一般借口大概会多耗时30ms左右)
            """
            pr = cProfile.Profile()
            pr.enable()
            yield
            pr.disable()
            ps = pstats.Stats(pr).sort_stats(sortby)
            ps.print_stats(limit)

        @contextmanager
        def line_profiling_ctx(func):
            """
            使用line_profile进行分析，统计每一行代码的执行时间，但是不能分析子函数的运行时间
            """
            pr = line_profiler.LineProfiler(func)
            pr.enable()  # 开始性能分析
            yield
            pr.disable()  # 停止性能分析
            pr.print_stats()

        @contextmanager
        def memory_profiling_ctx(func, *args, **kwargs):
            """
            使用memory_profiler进行分析, 统计每一行代码占用的内存
            """
            pass

        status = self.should_show_stats(request)
        if status == False:
            return
        elif status == 1:
            try:
                limit_num = int(request.GET.get("cprof", 10))
            except:
                limit_num = 10
            with c_profiling(sortby='tottime', limit=limit_num):
                view_func(request, *view_args, **view_kwargs)
        elif status == 2:
            with line_profiling_ctx(view_func):
                view_func(request, *view_args, **view_kwargs)
        elif status == 3:
            pass



