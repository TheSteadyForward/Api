# -*- coding: utf-8 -*-

import os
import logging
import inspect

from django.conf import settings as _settings
from django.http import HttpResponse


log = logging.getLogger(__name__)


def log_list(request):
    """
    功能说明：日志列表
    ----------------------------------------------
    修改人                    修改时间
    ----------------------------------------------
    Nick                    2016－01－04
    """
    html = ''
    try:
        base_dir = _settings.LOGDIR
        file_list = os.listdir(base_dir)

        for file_name in file_list:
            html += '<div style="margin:10px;"><a href="/logview/%s" target="_blank">%s</a></div>' % (file_name, file_name)

    except Exception as e:
        log.error("%s:%s" % (inspect.stack()[0][3], e))
        html = 'error:%s' % e

    return HttpResponse(html)
