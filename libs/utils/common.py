# -*- coding: utf-8 -*-
import hashlib
import logging
import time

from functools import wraps

import pypinyin
from django.http.request import UnreadablePostError
from django.http import HttpResponse

log = logging.getLogger(__name__)

#                            _ooOoo_
#                           o8888888o
#                           88" . "88
#                           (| -_- |)
#                            O\ = /O
#                        ____/`---'\____
#                      .   ' \\| |// `.
#                       / \\||| : |||// \
#                     / _||||| -:- |||||- \
#                       | | \\\ - /// | |
#                     | \_| ''\---/'' | |
#                      \ .-\__ `-` ___/-. /
#                   ___`. .' /--.--\ `. . __
#                ."" '< `.___\_<|>_/___.' >'"".
#               | | : `- \`.;`\ _ /`;.`/ - ` : | |
#                 \ \ `-. \_ __\ /__ _/ .-` / /
#         ======`-.____`-.___\_____/___.-`____.-'======
#                            `=---='
#                 佛祖保佑     永无bug     永不修改
#         .............................................
#                 佛祖镇楼                 BUG辟易


class Struct(dict):
    """
    - 为字典加上点语法. 例如:
    - >>> o = Struct({'a':1})
    - >>> o.a
    - >>> 1
    - >>> o.b
    - >>> None
    """

    def __init__(self, dict_obj={}):
        super().__init__()
        self.update(dict_obj)

    def __getattr__(self, name):
        # Pickle is trying to get state from your object, and dict doesn't implement it.
        # Your __getattr__ is being called with "__getstate__" to find that magic method,
        # and returning None instead of raising AttributeError as it should.
        if name.startswith('__'):
            raise AttributeError
        return self.get(name)

    def __setattr__(self, name, val):
        self[name] = val

    def __hash__(self):
        return id(self)


def fn_timer(func):
    """
    测量接口运行时间
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print('{}.{} : {}'.format(func.__module__, func.__name__, end - start))
        return r

    return wrapper


def create_tree(tree_list, data_list, parent_id):
    """
    递归生成树形结构数据
    :param tree_list:
    :param data_list:
    :param parent_id:
    :return:
    """
    filter_list = []

    for obj in data_list:
        if obj.parent_id == parent_id:
            filter_list.append(obj)

    for obj in filter_list:
        tree_list.append(obj)
        # 递归创建子节点
        create_tree(tree_list, data_list, obj.id)
    return tree_list


def request_interrupt(fun):
    """
    用户中断请求(设备断电、应用崩溃、网络波动等)异常捕获
    """

    @wraps(fun)
    def wrapper(*args, **kwargs):
        try:
            try_result = fun(*args, **kwargs)
            return try_result
        except UnreadablePostError:
            log.info("客户端中断请求：UnreadablePostError")
            return HttpResponse()

    return wrapper


def num_to_ch(num):
    """
    功能说明：讲阿拉伯数字转换成中文数字（转换[0, 10000)之间的阿拉伯数字 ）
    ----------------------------------------------------------------------------
    修改人                修改时间                修改原因
    ----------------------------------------------------------------------------
    陈龙                2012.2.9
    """
    num = int(num)
    _MAPPING = (u'零', u'一', u'二', u'三', u'四', u'五', u'六', u'七', u'八', u'九', )
    _P0 = (u'', u'十', u'百', u'千', )
    _S4 = 10 ** 4
    if num < 0 or num >= _S4:
        return None
    if num < 10:
        return _MAPPING[num]
    else:
        lst = []
        while num >= 10:
            lst.append(num % 10)
            num = num // 10
        lst.append(num)
        c = len(lst)    # 位数
        result = u''
        for idx, val in enumerate(lst):
            if val != 0:
                result += _P0[idx] + _MAPPING[val]
            if idx < c - 1 and lst[idx + 1] == 0:
                result += u'零'
        result = result[::-1]
        if result[:2] == u"一十":
            result = result[1:]
        if result[-1:] == u"零":
            result = result[:-1]
        return result


def dedupe(items, key=None):
    """
    字典列表去重

    :param items:字典列表
    :param key:
    :return:
    """
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


def replace_symbol(content):
    """
    替换特殊符号
    """
    content = u"%s" % content
    replace_content = content.replace('\t', '').replace('\r', '').replace('\n', '')

    return replace_content


def pinyin_abb(last_name):
    """
    功能说明：       将姓名转换为拼音首字母缩写
    pinyin_abb(u'王晨光')
    wcg
    ----------------------------------------------------------------------------
    修改人                修改时间                修改原因
    ----------------------------------------------------------------------------
    Nick                2016-10-10
    """
    rows = pypinyin.pinyin(last_name, style=pypinyin.NORMAL)  # 获取姓氏首字母
    return ''.join(row[0][0] for row in rows if len(row) > 0)


def md5_encode(original_str):
    """
    md5加密
    :param original_str:
    :return:
    """
    m = hashlib.md5()
    m.update(original_str.encode(encoding='UTF-8'))
    return m.hexdigest()
