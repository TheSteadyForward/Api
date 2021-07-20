# -*- coding: utf-8 -*-
from django.conf.urls import url
from weblog import views


urlpatterns = [
    url(r'^$', views.log_list),             # 日志列表
]
