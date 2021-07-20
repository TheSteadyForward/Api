# -*- coding: utf-8 -*-
from django.db.transaction import atomic

from libs.utils.ajax import ajax_ok

"""
@apiDefine XA6 西安6号线
"""


def get_token(request):
    """
    接口功能说明: 获取临时token
    --------------------------------------------
    接口逻辑说明:
    --------------------------------------------
    修改人        修改时间          修改原因
    --------------------------------------------
    Nick         2020-11-20        新建
    --------------------------------------------
    """
    """
    @api {get} /external_use/construction_dispatch/get_token?uid=oa100000    01 获取临时token
    @apiGroup XA6
    
    @apiVersion 1.0.0
    @apiName get_token
    @apiDescription 获取临时token
    
    @apiParam     	{Str}        uid							OA系统用户ID, oa开头
    
    @apiSuccess     {Str}        access_token					临时token，有效期1H
    
    @apiSuccessExample {JSON} 响应示例
    返回值类型: JSON
    {
        "message": "OK",
        "access_token": ""
    }
    """
    return ajax_ok()


@atomic()
def cur_station_info(request):
    """
    接口功能说明: 获取本站A类施工请销点详情
    --------------------------------------------
    接口逻辑说明:
    --------------------------------------------
    修改人        修改时间          修改原因
    --------------------------------------------
    Nick         2020-11-20        新建
    --------------------------------------------
    """
    """
    @api {post} /external_use/construction_dispatch/cur_station_info    02 获取施工请销点详情
    @apiGroup XA6
    
    @apiVersion 1.0.0
    @apiName cur_station_info
    @apiDescription 获取本站A类施工请销点详情

    @apiParam     {Dict}       params								参数
    @apiParam     {Str}        params.token							    认证token
    @apiParam     {Str}        params.line_no							线别序号，如：六号线为6
    @apiParam     {Str}        params.station_name						站点名称
    @apiParam     {List}       params.fields							查询的字段列表
    @apiParam     {Int}        params.limit								分页查询参数
    @apiParam     {Int}        params.offset							分页查询参数
    @apiParam     {Str}        params.sort								排序，默认逆序，如："id DESC"
    @apiParam     {Str}        params.day								查询日期，如：2020-11-23
    
    @apiParamExample {JSON} 参数示例
    {
        "params": {
            "uid": 'oa111',
            "line_no": "6",
            "station_name": "大唐芙蓉园站",
            "fields": [    
                "construction_recognize_number",
                "p_work_code",
                "p_work_date_str",
                "p_work_date",
                "p_station_ask",
                "show_start_pause",
                "p_use_type",
                "work_category_for_list",
                "p_work_time",
                "p_con_unit_name",
                "p_work_content",
                "work_area_summary_compute",
                "elec_area_str",
                "p_protect_measures_compute",
                "p_protect_measures",
                "cooperate_content",
                "principal_for_list",
                "remark",
                "cc_state",
                "_task_definition_key",
                "btns_str",
                "plan_type",
                "_back",
                "ecs",
                "p_outsource",
                "_is_parallel",
                "_level_role",
                "_group",
                "_department",
                "_compute_task_id",
                "_compute_task_definition_key"
            ],
            "limit": 10,
            "offset": 0,
            "sort": "id ASC",
            "day": "2020-11-23"
        },
        "id": 110732623
    }                                                                          
    
    @apiSuccess     {List}       data										返回数据
    @apiSuccess     {Str}        data.id										施工计划id
    @apiSuccess     {Int}        data.construction_recognize_number				施工承认号
    @apiSuccess     {Int}        data.p_work_code								作业代码
    @apiSuccess     {Int}        data.p_work_date_str							作业日期
    @apiSuccess     {Int}        data.p_work_date								作业日期
    @apiSuccess     {Int}        data.p_station_ask								站点信息
    @apiSuccess     {Int}        data.show_start_pause							是否显示开始暂停
    @apiSuccess     {Int}        data.p_use_type                         	    计划用途
    @apiSuccess     {Int}        data.work_category_for_list					作业类别
    @apiSuccess     {Int}        data.p_work_time								总作业时间
    @apiSuccess     {Int}        data.p_con_unit_name							施工单位
    @apiSuccess     {Int}        data.p_work_content							作业内容
    @apiSuccess     {Int}        data.work_area_summary_compute					作业区域
    @apiSuccess     {Int}        data.elec_area_str								接触网供电安排
    @apiSuccess     {Int}        data.p_protect_measures_compute				防护措施
    @apiSuccess     {Int}        data.p_protect_measures									
    @apiSuccess     {Int}        data.cooperate_content							配合单位及内容
    @apiSuccess     {Int}        data.principal_for_list						施工负责人
    @apiSuccess     {Int}        data.remark									备注
    @apiSuccess     {Int}        data.cc_state									施工控制状态
    @apiSuccess     {Int}        data._task_definition_key						任务key
    @apiSuccess     {Int}        data.btns_str									操作按扭
    @apiSuccess     {Int}        data.plan_type									计划类型
    @apiSuccess     {Int}        data._back										驳回任务
    @apiSuccess     {Int}        data.ecs										供电情况
    @apiSuccess     {Int}        data.p_outsource								外单位单选框
    @apiSuccess     {Int}        data._is_parallel								并行任务中
    @apiSuccess     {Int}        data._level_role								阶段角色
    @apiSuccess     {Int}        data._group									群组
    @apiSuccess     {Int}        data._department								部门
    @apiSuccess     {Int}        data._compute_task_id							务id
    @apiSuccess     {Int}        data._compute_task_definition_key														
    
    @apiSuccessExample {JSON} 响应示例
    返回值类型: JSON
    {
        "jsonrpc": "2.0",
        "id": 110732623,
        "result": {
            "message": "OK",
            "data": [
                {
                    "id": 803034,
                    "construction_recognize_number": "无",
                    "p_work_code": "Z-6A2-26-05",
                    "p_work_date": "2020-11-26",
                    "p_station_ask": [
                        445,
                        "仁村站"
                    ],
                    "p_use_type": "construct",
                    "p_work_time": "2020年11月26日 从次日0:30开始至4:30结束, 总耗时4小时0分钟",
                    "p_con_unit_name": "中国铁塔股份有限公司西安市分公司",
                    "p_work_content": "区间施工、电缆整理、AP箱调试、漏缆整理、天线安装、馈线接地、安装扁铁、布放野战光缆\n",
                    "p_protect_measures": [
                        1,
                        "现场防护"
                    ],
                    "remark": "1、中铁七局（夏亚华13519172660）负责西电科大南校区·未来之瞳至西安国际医学中心站上下行线。。。",
                    "cc_state": "un_start",
                    "_task_definition_key": "",
                    "plan_type": "week",
                    "p_outsource": true,
                    "_is_parallel": false,
                    "_level_role": "552-group_dispatch_dep_mg",
                    "p_work_date_str": "2020/11/26",
                    "show_start_pause": false,
                    "work_category_for_list": "6A2",
                    "work_area_summary_compute": "六号线,西电科大南校区·未来之瞳站至郭杜西站上下行线及其辅助线;",
                    "elec_area_str": "无要求",
                    "p_protect_measures_compute": "现场防护",
                    "cooperate_content": "通号六分部(主配合)",
                    "principal_for_list": "余佃中,17788062006",
                    "btns_str": "",
                    "_back": false,
                    "ecs": false,
                    "_group": false,
                    "_department": "[0, '', -1]",
                    "_compute_task_id": "ccbb1d07-2a10-11eb-a2bf-0242ac110003",
                    "_compute_task_definition_key": ""
                }
            ]
        }
    }
    """
    return ajax_ok()


@atomic()
def sync_face_info(request):
    """
    接口功能说明: 人脸识别信息提交
    --------------------------------------------
    接口逻辑说明:
    --------------------------------------------
    修改人        修改时间          修改原因
    --------------------------------------------
    Nick         2020-11-20        新建
    --------------------------------------------
    """
    """
    @api {post} /external_use/construction_dispatch/sync_face_info  03 人脸识别信息提交
    @apiGroup XA6

    @apiVersion 1.0.0
    @apiName sync_face_info
    @apiDescription 人脸识别信息提交

    @apiParam     {Int}        params.plan_id						施工计划ID
    @apiParam     {Str}        params.face_id						人脸识别ID

    @apiParamExample {JSON} 参数示例
    {
        "params": {
            "plan_id": 803034,
            "face_id": "Q006458",
            "token": "u4f05cUrp973Ft5MCuGzJFmUh4Ds"
        }
    }                                                                           
    
    @apiSuccessExample {JSON} 响应示例
    返回值类型: JSON
    {
        "jsonrpc": "2.0",
        "id": 11111,
        "result": {
            "message": "",
            "response": "OK"
        }
    }
    """
    return ajax_ok()
