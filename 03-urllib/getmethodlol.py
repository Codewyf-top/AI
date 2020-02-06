"""
基本url = "http://tieba.baidu.com"
{
kw：LOL
}
如果是中文，那么会编码--？----url编码
第一页 pn=0
第二页 pn=50
第三页 pn=100
...
第N页 pn=(n-1)*50
"""
#导包

import random
from urllib import request
#url编码的包

from urllib import parse
#导入os模块
import os

#定义函数
def get_wirte_lol(base_url,start,end):
    """
    爬取lol贴吧内容
    :param base_url: 基准url
    :param start :爬开始的页码
    :param end :爬取结束的页码
    :return: 贴吧内容
    """
    if not os.path.exists("./LOL"):
     os.makedirs("./LOL")
    kw = input ("Please input the name of tieba you wanna get:")
    qs = {
        "kw":kw
    }

    ua_list=[
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3676.400 QQBrowser/10.4.3505.400"
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    ]

    #url编码
    qs_data = parse.urlencode(qs)
    for i in range (start,end+1):
        pn = (i-1)*50
        qs["pn"] = str(pn)
        qs_data = parse.urlencode(qs)
    #拼接url
        url = base_url + qs_data
        user_agent = random.choice(ua_list)

        headers = {
        "User-Agent": user_agent
        }
        #构建请求 Request对象
        req = request.Request(url = url , headers =headers)
        #再增加一个不缓存
        req.add_header("Cache-Control", "private")
        #发送http请求，返回响应对象
        resp = request.urlopen(req)

    #读取数据
    data = resp.read().decode("utf-8")

    with open("./LOL/"+str(i)+".html","w",encoding = "utf-8") as f :
        f.write(data)

# def write_data(lol_data):
#     """
#     写入保存Lol信息
#     :param lol_data: lol贴吧内容
#     :return: None
#     """
#     if not os.path.exists("./LOL"):
#         os.makedirs("./LOL")
#     with open("./LOL/lol"):
if __name__ == '__main__':
    base_url="http://tieba.baidu.com/f?"
    start = int(input ("please input the start page :"))
    end = int (input ("please input the end page "))
    get_wirte_lol(base_url,start,end)0