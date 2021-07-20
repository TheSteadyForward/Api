define({
  "name": "Funenc项目接口文档",
  "version": "1.0.0",
  "description": "",
  "title": "项目接口文档",
  "url": "http://nick.cn1.utools.club",
  "header": {
    "title": "综述",
    "content": "<h3>概述:</h3>\n<p><strong>请求说明:</strong></p>\n<ul>\n<li>本API全部请求采用http POST 请求</li>\n<li>请求、响应全部json格式数据</li>\n<li>除登录接口外，全部接口需要header加参数 sessionid:登录后服务端返回</li>\n<li>接口需要用的project_id从settings文件里面读取默认的 ！！！</li>\n</ul>\n<p><strong>异常状态:</strong>\n<code>{&quot;message&quot;: &quot;数据获取失败，请重试&quot;, &quot;error&quot;: &quot;&quot;, &quot;data&quot;: &quot;&quot;, &quot;response&quot;: &quot;fail&quot;, &quot;next&quot;: &quot;&quot;}</code></p>\n<p><strong>成功状态:</strong>\n<code>{&quot;message&quot;: &quot;&quot;, &quot;error&quot;: &quot;&quot;, &quot;data&quot;: &quot;&quot;, &quot;response&quot;: &quot;ok&quot;, &quot;next&quot;: &quot;&quot;}</code></p>\n<p><strong>注意事项:</strong></p>\n<ul>\n<li>SessionID为客户端与服务器用户认证的SessionID,除登录接口除外，其他接口每次请求的时候必传该值</li>\n</ul>\n<h3>捕获全局设置:</h3>\n<ul>\n<li>error 为  1  message=&quot;该账号不存在&quot;</li>\n<li>error 为  2  message=&quot;用户名或密码错误&quot;</li>\n<li>error 为  3  message=&quot;该账号目前不可用“</li>\n<li>error 为  4  message=&quot;账号未开通该学科”</li>\n<li>error 为  5  message=&quot;请先加入一个班级”</li>\n<li>error 为  6  message=&quot;请联系老师设置班级“</li>\n<li>error 为  7  message=&quot;本次课你已经请假了，下次课再来吧”</li>\n<li>error 为  9  message=&quot;会话过期，请重新登录！&quot;</li>\n</ul>\n"
  },
  "template": {
    "forceLanguage": "zh_cn",
    "withCompare": false,
    "withGenerator": true
  },
  "sampleUrl": false,
  "defaultVersion": "0.0.0",
  "apidoc": "0.3.0",
  "generator": {
    "name": "apidoc",
    "time": "2021-07-20T05:14:03.196Z",
    "url": "https://apidocjs.com",
    "version": "0.28.1"
  }
});
