define({ "api": [
  {
    "type": "post",
    "url": "/external_use/construction_dispatch/cur_station_info",
    "title": "02 获取施工请销点详情",
    "group": "XA6",
    "version": "1.0.0",
    "name": "cur_station_info",
    "description": "<p>获取本站A类施工请销点详情</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Dict",
            "optional": false,
            "field": "params",
            "description": "<p>参数</p>"
          },
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "params.token",
            "description": "<p>认证token</p>"
          },
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "params.line_no",
            "description": "<p>线别序号，如：六号线为6</p>"
          },
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "params.station_name",
            "description": "<p>站点名称</p>"
          },
          {
            "group": "Parameter",
            "type": "List",
            "optional": false,
            "field": "params.fields",
            "description": "<p>查询的字段列表</p>"
          },
          {
            "group": "Parameter",
            "type": "Int",
            "optional": false,
            "field": "params.limit",
            "description": "<p>分页查询参数</p>"
          },
          {
            "group": "Parameter",
            "type": "Int",
            "optional": false,
            "field": "params.offset",
            "description": "<p>分页查询参数</p>"
          },
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "params.sort",
            "description": "<p>排序，默认逆序，如：&quot;id DESC&quot;</p>"
          },
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "params.day",
            "description": "<p>查询日期，如：2020-11-23</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "参数示例",
          "content": "{\n    \"params\": {\n        \"uid\": 'oa111',\n        \"line_no\": \"6\",\n        \"station_name\": \"大唐芙蓉园站\",\n        \"fields\": [    \n            \"construction_recognize_number\",\n            \"p_work_code\",\n            \"p_work_date_str\",\n            \"p_work_date\",\n            \"p_station_ask\",\n            \"show_start_pause\",\n            \"p_use_type\",\n            \"work_category_for_list\",\n            \"p_work_time\",\n            \"p_con_unit_name\",\n            \"p_work_content\",\n            \"work_area_summary_compute\",\n            \"elec_area_str\",\n            \"p_protect_measures_compute\",\n            \"p_protect_measures\",\n            \"cooperate_content\",\n            \"principal_for_list\",\n            \"remark\",\n            \"cc_state\",\n            \"_task_definition_key\",\n            \"btns_str\",\n            \"plan_type\",\n            \"_back\",\n            \"ecs\",\n            \"p_outsource\",\n            \"_is_parallel\",\n            \"_level_role\",\n            \"_group\",\n            \"_department\",\n            \"_compute_task_id\",\n            \"_compute_task_definition_key\"\n        ],\n        \"limit\": 10,\n        \"offset\": 0,\n        \"sort\": \"id ASC\",\n        \"day\": \"2020-11-23\"\n    },\n    \"id\": 110732623\n}",
          "type": "JSON"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "List",
            "optional": false,
            "field": "data",
            "description": "<p>返回数据</p>"
          },
          {
            "group": "Success 200",
            "type": "Str",
            "optional": false,
            "field": "data.id",
            "description": "<p>施工计划id</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.construction_recognize_number",
            "description": "<p>施工承认号</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.p_work_code",
            "description": "<p>作业代码</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.p_work_date_str",
            "description": "<p>作业日期</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.p_work_date",
            "description": "<p>作业日期</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.p_station_ask",
            "description": "<p>站点信息</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.show_start_pause",
            "description": "<p>是否显示开始暂停</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.p_use_type",
            "description": "<p>计划用途</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.work_category_for_list",
            "description": "<p>作业类别</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.p_work_time",
            "description": "<p>总作业时间</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.p_con_unit_name",
            "description": "<p>施工单位</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.p_work_content",
            "description": "<p>作业内容</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.work_area_summary_compute",
            "description": "<p>作业区域</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.elec_area_str",
            "description": "<p>接触网供电安排</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.p_protect_measures_compute",
            "description": "<p>防护措施</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.p_protect_measures",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.cooperate_content",
            "description": "<p>配合单位及内容</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.principal_for_list",
            "description": "<p>施工负责人</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.remark",
            "description": "<p>备注</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.cc_state",
            "description": "<p>施工控制状态</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data._task_definition_key",
            "description": "<p>任务key</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.btns_str",
            "description": "<p>操作按扭</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.plan_type",
            "description": "<p>计划类型</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data._back",
            "description": "<p>驳回任务</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.ecs",
            "description": "<p>供电情况</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.p_outsource",
            "description": "<p>外单位单选框</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data._is_parallel",
            "description": "<p>并行任务中</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data._level_role",
            "description": "<p>阶段角色</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data._group",
            "description": "<p>群组</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data._department",
            "description": "<p>部门</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data._compute_task_id",
            "description": "<p>务id</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data._compute_task_definition_key",
            "description": ""
          }
        ]
      },
      "examples": [
        {
          "title": "响应示例",
          "content": "返回值类型: JSON\n{\n    \"jsonrpc\": \"2.0\",\n    \"id\": 110732623,\n    \"result\": {\n        \"message\": \"OK\",\n        \"data\": [\n            {\n                \"id\": 803034,\n                \"construction_recognize_number\": \"无\",\n                \"p_work_code\": \"Z-6A2-26-05\",\n                \"p_work_date\": \"2020-11-26\",\n                \"p_station_ask\": [\n                    445,\n                    \"仁村站\"\n                ],\n                \"p_use_type\": \"construct\",\n                \"p_work_time\": \"2020年11月26日 从次日0:30开始至4:30结束, 总耗时4小时0分钟\",\n                \"p_con_unit_name\": \"中国铁塔股份有限公司西安市分公司\",\n                \"p_work_content\": \"区间施工、电缆整理、AP箱调试、漏缆整理、天线安装、馈线接地、安装扁铁、布放野战光缆\\n\",\n                \"p_protect_measures\": [\n                    1,\n                    \"现场防护\"\n                ],\n                \"remark\": \"1、中铁七局（夏亚华13519172660）负责西电科大南校区·未来之瞳至西安国际医学中心站上下行线。。。\",\n                \"cc_state\": \"un_start\",\n                \"_task_definition_key\": \"\",\n                \"plan_type\": \"week\",\n                \"p_outsource\": true,\n                \"_is_parallel\": false,\n                \"_level_role\": \"552-group_dispatch_dep_mg\",\n                \"p_work_date_str\": \"2020/11/26\",\n                \"show_start_pause\": false,\n                \"work_category_for_list\": \"6A2\",\n                \"work_area_summary_compute\": \"六号线,西电科大南校区·未来之瞳站至郭杜西站上下行线及其辅助线;\",\n                \"elec_area_str\": \"无要求\",\n                \"p_protect_measures_compute\": \"现场防护\",\n                \"cooperate_content\": \"通号六分部(主配合)\",\n                \"principal_for_list\": \"余佃中,17788062006\",\n                \"btns_str\": \"\",\n                \"_back\": false,\n                \"ecs\": false,\n                \"_group\": false,\n                \"_department\": \"[0, '', -1]\",\n                \"_compute_task_id\": \"ccbb1d07-2a10-11eb-a2bf-0242ac110003\",\n                \"_compute_task_definition_key\": \"\"\n            }\n        ]\n    }\n}",
          "type": "JSON"
        }
      ]
    },
    "filename": "../apps/xa_6_metro/views.py",
    "groupTitle": "西安6号线"
  },
  {
    "type": "get",
    "url": "/external_use/construction_dispatch/get_token?uid=oa100000",
    "title": "01 获取临时token",
    "group": "XA6",
    "version": "1.0.0",
    "name": "get_token",
    "description": "<p>获取临时token</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "uid",
            "description": "<p>OA系统用户ID, oa开头</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Str",
            "optional": false,
            "field": "access_token",
            "description": "<p>临时token，有效期1H</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "响应示例",
          "content": "返回值类型: JSON\n{\n    \"message\": \"OK\",\n    \"access_token\": \"\"\n}",
          "type": "JSON"
        }
      ]
    },
    "filename": "../apps/xa_6_metro/views.py",
    "groupTitle": "西安6号线"
  },
  {
    "type": "post",
    "url": "/external_use/construction_dispatch/sync_face_info",
    "title": "03 人脸识别信息提交",
    "group": "XA6",
    "version": "1.0.0",
    "name": "sync_face_info",
    "description": "<p>人脸识别信息提交</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Int",
            "optional": false,
            "field": "params.plan_id",
            "description": "<p>施工计划ID</p>"
          },
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "params.face_id",
            "description": "<p>人脸识别ID</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "参数示例",
          "content": "{\n    \"params\": {\n        \"plan_id\": 803034,\n        \"face_id\": \"Q006458\",\n        \"token\": \"u4f05cUrp973Ft5MCuGzJFmUh4Ds\"\n    }\n}",
          "type": "JSON"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "响应示例",
          "content": "返回值类型: JSON\n{\n    \"jsonrpc\": \"2.0\",\n    \"id\": 11111,\n    \"result\": {\n        \"message\": \"\",\n        \"response\": \"OK\"\n    }\n}",
          "type": "JSON"
        }
      ]
    },
    "filename": "../apps/xa_6_metro/views.py",
    "groupTitle": "西安6号线"
  },
  {
    "type": "post",
    "url": "/web/auth",
    "title": "01 用户登录",
    "group": "ZZ4",
    "version": "1.0.0",
    "name": "auth_login",
    "description": "<p>用户登录</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "login",
            "description": "<p>账号</p>"
          },
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "password",
            "description": "<p>密码</p>"
          },
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "redirect",
            "description": "<p>重定向url</p>"
          },
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "img_code",
            "description": "<p>图片验证码</p>"
          },
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "img_code_id",
            "description": "<p>图片验证码id</p>"
          },
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "csrf_token",
            "description": "<p>token</p>"
          },
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "crypto_token",
            "description": "<p>公钥</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "参数示例",
          "content": "{\n    'params': {\n        'login': '100010',\n        'password': '',\n        'csrf_token': '',\n        'redirect': '',\n        'img_code': '',\n        'img_code_id':'',\n        'crypto_token': ''\n    }\n}",
          "type": "JSON"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "响应示例",
          "content": "返回值类型: JSON\n{\n    'message': '注册成功',\n    'code': 200\n}",
          "type": "JSON"
        }
      ]
    },
    "filename": "../apps/zz_4_metro/views.py",
    "groupTitle": "郑州4号线"
  },
  {
    "type": "get",
    "url": "/construction/plan/delete?pwd=10788",
    "title": "09 删除旧流程",
    "group": "ZZ4",
    "version": "1.0.0",
    "name": "plan_delete",
    "description": "<p>删除用户发起的旧流程(用于业务流程已存在，不能重复发起)</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "pwd",
            "description": "<p>用户ID(res_users)</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "响应示例",
          "content": "返回值类型: JSON\n{\n    \"message\": \"success\",\n}",
          "type": "JSON"
        }
      ]
    },
    "filename": "../apps/zz_4_metro/views.py",
    "groupTitle": "郑州4号线"
  },
  {
    "type": "post",
    "url": "/web/register/get/registerProcess",
    "title": "05 注册进度",
    "group": "ZZ4",
    "version": "1.0.0",
    "name": "register_process",
    "description": "<p>注册进度</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "phone",
            "description": "<p>注册的手机号码</p>"
          },
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "token",
            "description": "<p>待匹配的token</p>"
          },
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "code",
            "description": "<p>验证码</p>"
          },
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "img_code",
            "description": "<p>图片验证码</p>"
          },
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "img_code_id",
            "description": "<p>图片验证码id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "参数示例",
          "content": "{\n    'phone': '15617889999',\n    'token': 'xx',\n    'code': 'xx',\n    'img_code': '',\n    'img_code_id': '',\n}",
          "type": "JSON"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Dict",
            "optional": false,
            "field": "data",
            "description": "<p>返回数据</p>"
          },
          {
            "group": "Success 200",
            "type": "Str",
            "optional": false,
            "field": "data.id",
            "description": "<p>注册id</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.name",
            "description": "<p>注册名字</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.registerType",
            "description": "<p>注册类型</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.workNum",
            "description": "<p>工号</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.principalFileFront",
            "description": "<p>施工负责人证件照id</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.cardFileFront",
            "description": "<p>身份证正面</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.cardFileBack",
            "description": "<p>身份证反面</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.sex",
            "description": "<p>性别</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.registerPrincipal",
            "description": "<p>是否注册施工负责人</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.cardDate",
            "description": "<p>身份证日期</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.cardId",
            "description": "<p>身份证id</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.department",
            "description": "<p>部门id</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.state",
            "description": "<p>注册进度</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.principalId",
            "description": "<p>施工负责人id</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "data.grade",
            "description": "<p>成绩</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "响应示例",
          "content": "返回值类型: JSON\n{\n    'message': '',\n    'code': 200,\n    'data': {\n        'id': 1,\n        'name': '',\n        'registerType': '',\n        'workNum': '',\n        'principalFileFront': '',\n        'cardFileFront': '',\n        'cardFileBack': '',\n        'sex': '',\n        'registerPrincipal': '',\n        'cardDate': '',\n        'cardId': '',\n        'department': '',\n        'state': '',\n        'principalId': '',\n        'grade': ''\n    }\n}",
          "type": "JSON"
        }
      ]
    },
    "filename": "../apps/zz_4_metro/views.py",
    "groupTitle": "郑州4号线"
  },
  {
    "type": "post",
    "url": "/web/forget/rPassword",
    "title": "06 重置密码",
    "group": "ZZ4",
    "version": "1.0.0",
    "name": "reset_password",
    "description": "<p>重置密码</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "phone",
            "description": "<p>手机号码</p>"
          },
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "token",
            "description": "<p>待匹配的token</p>"
          },
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "code",
            "description": "<p>验证码</p>"
          },
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "password",
            "description": "<p>密码</p>"
          },
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "img_code",
            "description": "<p>图片验证码</p>"
          },
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "img_code_id",
            "description": "<p>图片验证码id</p>"
          },
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "crypto_token",
            "description": "<p>公钥</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "参数示例",
          "content": "{\n    'phone': '15617889999',\n    'token': 'xx',\n    'code': 'xx',\n    'password': 'xx',\n    'img_code': '',\n    'img_code_id': '',\n    'crypto_token' : ''\n}",
          "type": "JSON"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "响应示例",
          "content": "返回值类型: JSON\n{\n    'message': '注册成功',\n    'code': 200\n}",
          "type": "JSON"
        }
      ]
    },
    "filename": "../apps/zz_4_metro/views.py",
    "groupTitle": "郑州4号线"
  },
  {
    "type": "post",
    "url": "/alimessage/send/register",
    "title": "03 发送注册验证码",
    "group": "ZZ4",
    "version": "1.0.0",
    "name": "send_register_code",
    "description": "<p>发送注册验证码</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "phone",
            "description": "<p>手机号</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "参数示例",
          "content": "{\n    \"phone\": 15617778888\n}",
          "type": "JSON"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "响应示例",
          "content": "返回值类型: JSON\n{\n    'message': '发送成功',\n    'token': token,\n    'code': 200\n}",
          "type": "JSON"
        }
      ]
    },
    "filename": "../apps/zz_4_metro/views.py",
    "groupTitle": "郑州4号线"
  },
  {
    "type": "post",
    "url": "/alimessage/send/rpassword",
    "title": "04 发送重置验证码",
    "group": "ZZ4",
    "version": "1.0.0",
    "name": "send_reset_pw_code",
    "description": "<p>重置密码发送短信验证码</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "phone",
            "description": "<p>手机号</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "参数示例",
          "content": "{\n    \"phone\": 15617778888\n}",
          "type": "JSON"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "响应示例",
          "content": "返回值类型: JSON\n{\n    'message': '发送成功',\n    'token': token,\n    'code': 200\n}",
          "type": "JSON"
        }
      ]
    },
    "filename": "../apps/zz_4_metro/views.py",
    "groupTitle": "郑州4号线"
  },
  {
    "type": "post",
    "url": "/web/register/signUp",
    "title": "02 用户注册",
    "group": "ZZ4",
    "version": "1.0.0",
    "name": "sign_up",
    "description": "<p>用户注册</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "phone",
            "description": "<p>手机号码</p>"
          },
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "token",
            "description": "<p>待匹配的token</p>"
          },
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "code",
            "description": "<p>验证码</p>"
          },
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "password",
            "description": "<p>密码</p>"
          },
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "registerType",
            "description": "<p>注册类型 internal：本单位 outsource：委外 external：外单位</p>"
          },
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "img_code",
            "description": "<p>图片验证码</p>"
          },
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "img_code_id",
            "description": "<p>图片验证码id</p>"
          },
          {
            "group": "Parameter",
            "type": "Str",
            "optional": false,
            "field": "crypto_token",
            "description": "<p>公钥</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "参数示例",
          "content": "{\n    'phone': '15617889999',\n    'token': 'xx',\n    'code': 'xx',\n    'password': 'xx',\n    'registerType': 'xx',\n    'img_code': '',\n    'img_code_id': '',\n    'crypto_token': ''\n}",
          "type": "JSON"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "响应示例",
          "content": "返回值类型: JSON\n{\n    'message': '注册成功',\n    'code': 200\n}",
          "type": "JSON"
        }
      ]
    },
    "filename": "../apps/zz_4_metro/views.py",
    "groupTitle": "郑州4号线"
  }
] });
