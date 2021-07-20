### 概述:
**请求说明:**
* 本API全部请求采用http POST 请求
* 请求、响应全部json格式数据
* 除登录接口外，全部接口需要header加参数 sessionid:登录后服务端返回
* 接口需要用的project_id从settings文件里面读取默认的 ！！！

**异常状态:**
`{"message": "数据获取失败，请重试", "error": "", "data": "", "response": "fail", "next": ""}`

**成功状态:**
`{"message": "", "error": "", "data": "", "response": "ok", "next": ""}`

**注意事项:**
* SessionID为客户端与服务器用户认证的SessionID,除登录接口除外，其他接口每次请求的时候必传该值

### 捕获全局设置:

 * error 为  1  message="该账号不存在" 
 * error 为  2  message="用户名或密码错误"
 * error 为  3  message="该账号目前不可用“ 
 * error 为  4  message="账号未开通该学科” 
 * error 为  5  message="请先加入一个班级” 
 * error 为  6  message="请联系老师设置班级“ 
 * error 为  7  message="本次课你已经请假了，下次课再来吧” 
 * error 为  9  message="会话过期，请重新登录！"
