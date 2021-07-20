## 项目结构说明:
    .${root}/               项目根目录
    ├── README.md           项目简介
    ├── api_server          项目配置APP根目录
    │   ├── settings.py     项目配置
    │   ├── urls.py         根路由
    │   ├── views.py        根视图
    │   └── wsgi.py         uwsg启动配置文件
    ├── apps                项目使用的app模块全部放在此文件夹下
    │   └── xa_6_metro      西安6号线api
    │       ├── __init__.py
    │       ├── admin.py
    │       ├── apps.py     当前app配置
    │       ├── migrations  DB迁移文件
    │       ├── models.py   app模型
    │       └── views.py    app视图
    ├── core
    │   ├── examine_middleware.py
    │   ├── middleware.py   中间件
    │   └── router.py
    ├── docs                项目文档,如models,apidoc配置文件,项目目录结构,接口规范文档
    │   ├── apidoc.json
    │   ├── header.md
    │   └── 代码规范.md
    ├── libs                公共库文件夹
    │   ├── __init__.py
    │   └── util            工具库
    │       ├── __init__.py
    │       ├── ajax.py     Ajax工具
    │       ├── com_db.py   DB工具
    │       └── common.py   其他公共方法
    ├── log                 项目运行日志
    ├── manage.py
    ├── statics             静态资源目录
    │   ├── apidoc          apidoc文档目录
    │   ├── css             CSS文件目录
    │   ├── js              JS文件目录
    │   └── images          图片目录
    ├── templates           模板目录
    │   └── templates.html
    └── weblog              
    └── .gitignore          git忽略文件配置


## API DOC文档生成命令：
    进入 docs 目录下执行以下命令
    apidoc -f ".*\\.py$" -i ../ -o .
    @apiGroup XA6 分组名称，分组按照名称排序
    @apiName get_token  根据分组名称(apiGroup) + 接口名称(apiName) 组成左侧书签导航栏

## 访问接口文档地址：
    http://localhost:8000/apidoc/index.html

## 数据模型文件(使用Navicat客户端打开该文件)
    *.ndm
