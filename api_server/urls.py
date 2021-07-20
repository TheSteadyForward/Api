"""api_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve

from api_server import views

urlpatterns = [
    path('', views.api_doc_home),
    path('admin/', admin.site.urls),
]

urlpatterns += [
    url(r'^logview/(?P<path>.*)$', serve, {'document_root': settings.LOG_DIR}),
    url(r'^site_media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_SITE}),
    url(r'^apidoc/(?P<path>.*)$', serve, {'document_root': settings.API_DOC}),
    url(r'^weblog/', include('weblog.urls')),    # 网站日志
]


handler400 = views.bad_request
handler403 = views.permission_denied
handler404 = views.page_not_found
handler500 = views.server_error


"""
@apiDefine XA9 西安9号线
@apiDefine XA6 西安6号线OA
@apiDefine ZZ3 郑州3号线
@apiDefine ZZ4 郑州4号线
"""
