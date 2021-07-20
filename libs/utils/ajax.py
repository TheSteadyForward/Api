# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from django.conf import settings


class SimpleAjaxException(Exception):
    pass


def ajax_ok_data(data='', message=None):

    return ajax_data('ok', data=data, message=message)


def json_ok_data(data='', message=None):
    return json_data(ajax_data('ok', data=data))


def json_data(data, check=False):
    encode = settings.DEFAULT_CHARSET
    if check:
        if not is_ajax_data(data):
            raise SimpleAjaxException('Return data should be follow the Simple Ajax Data Format')
    return json.dumps(uni_str(data, encode))


def ajax_fail_data(error='', message=None):
    return ajax_data('fail', error=error, message=message)


def ajax_ok(data='', message=None):
    """
    return a success response
    """
    
    # return json_response(ajax_ok_data(data, message))
    return HttpResponse(json.dumps(dict(response='ok', data=data, error='', message='')))


def ajax_fail(error='', message=None):
    """
    return an error response
    """
   
    return json_response(ajax_fail_data(error, message))


def json_response(data, check=False):

    encode = settings.DEFAULT_CHARSET

    if check:
        if not is_ajax_data(data):
            raise SimpleAjaxException('Return data should be follow the Simple Ajax Data Format')
    try:
        return HttpResponse(json.dumps(uni_str(data, encode)))
    except:
        return HttpResponse(json.dumps(uni_str(data, "gb2312")))


def ajax_data(response_code, data=None, error=None, message=None):
    """if the response_code is true, then the data is set in 'data',
    if the response_code is false, then the data is set in 'error'
    """

    r = dict(response='ok', data='', error='', message='')
    if response_code is True or response_code.lower() in ('ok', 'yes', 'true'):
        r['response'] = 'ok'
    else:
        r['response'] = 'fail'
    if data:
        r['data'] = data
    if error:
        r['error'] = error
    if message:
        r['message'] = message
    return r


def is_ajax_data(data):
    """Judge if a data is an Ajax data"""

    if not isinstance(data, dict):
        return False
    for k in data.keys():
        if k not in ('response', 'data', 'error', 'message'):
            return False
    if 'response' not in data:
        return False
    if not data['response'] in ('ok', 'fail'): return False
    return True


def uni_str(a, encoding=None):
    if not encoding:
        encoding = settings.DEFAULT_CHARSET
    
    if isinstance(a, (list, tuple)):
    
        s = []
        for i, k in enumerate(a):
            s.append(uni_str(k, encoding))
        return s
    elif isinstance(a, dict):
    
        s = {}
        for i, k in enumerate(a.items()):
            key, value = k
            s[uni_str(key, encoding)] = uni_str(value, encoding)
        return s
    elif isinstance(a, str):
    
        return a
    elif isinstance(a, (int, float)):
    
        return a
    # elif isinstance(a, str) or (hasattr(a, '__str__') and callable(getattr(a, '__str__'))):
    #
    #     if getattr(a, '__str__'):
    #         a = str(a)
    #
    #     return unicode(a, encoding)
    else:
        return a

