from urllib import request
import random
#确定url
base_url = "http://www.baidu.com"
ua_list=["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3676.400 QQBrowser/10.4.3505.400"
 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"

]
user_agent = random.choice(ua_list)
#构建headers,构建浏览器版本
headers = {
"User-Agent": user_agent
}
print(user_agent)
# #构建一个request对象，让对象帮助我们去发送请求
# req = request.Request(url=base_url,headers = headers)
# req.add_header("Cache-Control", "private")
# #获取所有的请求头
# print(req.headers)
# #发送http请求，并返回响应
# resp = request.urlopen(req)
#
# data  = resp.read().decode("utf-8")
# print(data)
