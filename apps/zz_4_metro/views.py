# -*- coding: utf-8 -*-
from libs.utils.ajax import ajax_ok


def auth_login(request):
    """
    接口功能说明: 用户登录
    --------------------------------------------
    接口逻辑说明:
    --------------------------------------------
    修改人        修改时间          修改原因
    --------------------------------------------
    Nick         2021-07-07        新建
    --------------------------------------------
    """
    """
    @api {post} /web/auth  01 用户登录
    @apiGroup ZZ4

    @apiVersion 1.0.0
    @apiName auth_login
    @apiDescription 用户登录

    @apiParam     {Str}        login						账号
    @apiParam     {Str}        password						密码
    @apiParam     {Str}        redirect				        重定向url
    @apiParam     {Str}        img_code						图片验证码
    @apiParam     {Str}        img_code_id					图片验证码id
    @apiParam     {Str}        csrf_token					token
    @apiParam     {Str}        crypto_token					公钥

    @apiParamExample {JSON} 参数示例
    {
        'params': {
            'login': '100010',
            'password': '',
            'csrf_token': '',
            'redirect': '',
            'img_code': '',
            'img_code_id':'',
            'crypto_token': ''
        }
    }                                                                          

    @apiSuccessExample {JSON} 响应示例
    返回值类型: JSON
    {
        'message': '注册成功',
        'code': 200
    }
    """
    return ajax_ok()


def sign_up(request):
    """
    接口功能说明: 用户注册
    --------------------------------------------
    接口逻辑说明:
    --------------------------------------------
    修改人        修改时间          修改原因
    --------------------------------------------
    Nick         2021-07-07        新建
    --------------------------------------------
    """
    """
    @api {post} /web/register/signUp  02 用户注册
    @apiGroup ZZ4

    @apiVersion 1.0.0
    @apiName sign_up
    @apiDescription 用户注册

    @apiParam     {Str}        phone						手机号码
    @apiParam     {Str}        token					    待匹配的token
    @apiParam     {Str}        code						    验证码
    @apiParam     {Str}        password						密码
    @apiParam     {Str}        registerType				    注册类型 internal：本单位 outsource：委外 external：外单位
    @apiParam     {Str}        img_code						图片验证码
    @apiParam     {Str}        img_code_id					图片验证码id
    @apiParam     {Str}        crypto_token					公钥

    @apiParamExample {JSON} 参数示例
    {
        'phone': '15617889999',
        'token': 'xx',
        'code': 'xx',
        'password': 'xx',
        'registerType': 'xx',
        'img_code': '',
        'img_code_id': '',
        'crypto_token': ''
    }                                                                          

    @apiSuccessExample {JSON} 响应示例
    返回值类型: JSON
    {
        'message': '注册成功',
        'code': 200
    }
    """
    return ajax_ok()


def send_register_code(request):
    """
    接口功能说明: 发送注册验证码
    --------------------------------------------
    接口逻辑说明:
    --------------------------------------------
    修改人        修改时间          修改原因
    --------------------------------------------
    Nick         2021-07-07        新建
    --------------------------------------------
    """
    """
    @api {post} /alimessage/send/register  03 发送注册验证码
    @apiGroup ZZ4

    @apiVersion 1.0.0
    @apiName send_register_code
    @apiDescription 发送注册验证码

    @apiParam     {Str}        phone						手机号

    @apiParamExample {JSON} 参数示例
    {
        "phone": 15617778888
    }                                                                           

    @apiSuccessExample {JSON} 响应示例
    返回值类型: JSON
    {
        'message': '发送成功',
        'token': token,
        'code': 200
    }
    """
    return ajax_ok()


def send_reset_pw_code(request):
    """
    接口功能说明: 重置密码发送短信验证码
    --------------------------------------------
    接口逻辑说明:
    --------------------------------------------
    修改人        修改时间          修改原因
    --------------------------------------------
    Nick         2021-07-07        新建
    --------------------------------------------
    """
    """
    @api {post} /alimessage/send/rpassword  04 发送重置验证码
    @apiGroup ZZ4

    @apiVersion 1.0.0
    @apiName send_reset_pw_code
    @apiDescription 重置密码发送短信验证码

    @apiParam     {Str}        phone						手机号

    @apiParamExample {JSON} 参数示例
    {
        "phone": 15617778888
    }                                                                           

    @apiSuccessExample {JSON} 响应示例
    返回值类型: JSON
    {
        'message': '发送成功',
        'token': token,
        'code': 200
    }
    """
    return ajax_ok()


def register_process(request):
    """
    接口功能说明: 注册进度
    --------------------------------------------
    接口逻辑说明:
    --------------------------------------------
    修改人        修改时间          修改原因
    --------------------------------------------
    Nick         2021-07-07        新建
    --------------------------------------------
    """
    """
    @api {post} /web/register/get/registerProcess  05 注册进度
    @apiGroup ZZ4

    @apiVersion 1.0.0
    @apiName register_process
    @apiDescription 注册进度

    @apiParam     {Str}        phone						注册的手机号码
    @apiParam     {Str}        token					    待匹配的token
    @apiParam     {Str}        code						    验证码
    @apiParam     {Str}        img_code						图片验证码
    @apiParam     {Str}        img_code_id					图片验证码id

    @apiParamExample {JSON} 参数示例
    {
        'phone': '15617889999',
        'token': 'xx',
        'code': 'xx',
        'img_code': '',
        'img_code_id': '',
    }
    
    @apiSuccess     {Dict}       data									返回数据
    @apiSuccess     {Str}        data.id									注册id
    @apiSuccess     {Int}        data.name				                    注册名字                                                             
    @apiSuccess     {Int}        data.registerType		                    注册类型                                                            
    @apiSuccess     {Int}        data.workNum				                工号                                                             
    @apiSuccess     {Int}        data.principalFileFront				    施工负责人证件照id                                                            
    @apiSuccess     {Int}        data.cardFileFront				            身份证正面                                                             
    @apiSuccess     {Int}        data.cardFileBack				            身份证反面                                                           
    @apiSuccess     {Int}        data.sex				                    性别                                                          
    @apiSuccess     {Int}        data.registerPrincipal				        是否注册施工负责人                                                            
    @apiSuccess     {Int}        data.cardDate				                身份证日期                                                            
    @apiSuccess     {Int}        data.cardId				                身份证id                                                           
    @apiSuccess     {Int}        data.department				            部门id                                                       
    @apiSuccess     {Int}        data.state				                    注册进度                                                             
    @apiSuccess     {Int}        data.principalId				            施工负责人id                                                          
    @apiSuccess     {Int}        data.grade				                    成绩                                                          

    @apiSuccessExample {JSON} 响应示例
    返回值类型: JSON
    {
        'message': '',
        'code': 200,
        'data': {
            'id': 1,
            'name': '',
            'registerType': '',
            'workNum': '',
            'principalFileFront': '',
            'cardFileFront': '',
            'cardFileBack': '',
            'sex': '',
            'registerPrincipal': '',
            'cardDate': '',
            'cardId': '',
            'department': '',
            'state': '',
            'principalId': '',
            'grade': ''
        }
    }
    """
    return ajax_ok()


def reset_password(request):
    """
    接口功能说明: 重置密码
    --------------------------------------------
    接口逻辑说明:
    --------------------------------------------
    修改人        修改时间          修改原因
    --------------------------------------------
    Nick         2021-07-07        新建
    --------------------------------------------
    """
    """
    @api {post} /web/forget/rPassword  06 重置密码
    @apiGroup ZZ4

    @apiVersion 1.0.0
    @apiName reset_password
    @apiDescription 重置密码

    @apiParam     {Str}        phone						手机号码
    @apiParam     {Str}        token					    待匹配的token
    @apiParam     {Str}        code						    验证码
    @apiParam     {Str}        password						密码
    @apiParam     {Str}        img_code						图片验证码
    @apiParam     {Str}        img_code_id					图片验证码id
    @apiParam     {Str}        crypto_token					公钥

    @apiParamExample {JSON} 参数示例
    {
        'phone': '15617889999',
        'token': 'xx',
        'code': 'xx',
        'password': 'xx',
        'img_code': '',
        'img_code_id': '',
        'crypto_token' : ''
    }                                                                          

    @apiSuccessExample {JSON} 响应示例
    返回值类型: JSON
    {
        'message': '注册成功',
        'code': 200
    }
    """
    return ajax_ok()


def plan_delete(request):
    """
    接口功能说明: 删除旧流程(用于业务流程已存在，不能重复发起)
    --------------------------------------------
    接口逻辑说明:
    --------------------------------------------
    修改人        修改时间          修改原因
    --------------------------------------------
    Nick         2021-07-07        新建
    --------------------------------------------
    """
    """
    @api {get} /construction/plan/delete?pwd=10788    09 删除旧流程
    @apiGroup ZZ4

    @apiVersion 1.0.0
    @apiName plan_delete
    @apiDescription 删除用户发起的旧流程(用于业务流程已存在，不能重复发起)

    @apiParam     	{Str}        pwd							用户ID(res_users)

    @apiSuccessExample {JSON} 响应示例
    返回值类型: JSON
    {
        "message": "success",
    }
    """
    return ajax_ok()
