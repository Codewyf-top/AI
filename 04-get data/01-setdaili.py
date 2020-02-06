"""
基本url = "http://tieba.baidu.com/f?"
{
kw:LOL
}
如果是中文,那么会编码--?----url编码
第一页  pn =0
第二页  pn =50
第三页  pn =100
....
第N页  pn = (N-1)* 50

"""
# 导包
import random
from urllib import  request
#url编码的包
from  urllib import  parse
#导入os模块
import  os

#定义函数
def get_write_lol(base_url,start,end):
    """
     爬取lol贴吧内容
    :param base_url: 基准url 
    :param start: 开始爬取的页码
    :param end: 爬取结束的页码
    :return: 贴吧内容
    """
    if not os.path.exists("./LOL"):
        os.makedirs("./LOL")

    # httpProxy= request.ProxyHandler({"http":"114.88."})
    proxy_list = [
        {"http":"60.216.101.46"},
        {"http": "220.168.52.245	"},
        {"http": "122.4.47.219"},

    ]
    proxy_ip = random.choice(proxy_list)


    kw = input("请输入你要爬取的贴吧名称：")
    qs ={
        "kw":kw
    }

    # 构建浏览器版本
    ua_list = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"]

    for i in range(start,end+1):
        pn = (i-1) * 50
        qs["pn"] = str(pn)

        httpProxy = request.ProxyHandler(proxy_ip)

        opener = request.build_opener(httpProxy)
        # url编码
        qs_data = parse.urlencode(qs)

        #拼接url
        url = base_url + qs_data

        #随机选择浏览器版本
        user_agent = random.choice(ua_list)
        #构建headers
        headers ={
            "User-Agent":user_agent
        }
        #构建请求Request对象
        req = request.Request(url=url,headers=headers)

        # 再增加一个不缓存的头部信息
        req.add_header("Cache-Control", "max-age=0")

        #发送http请求，返回响应对象
        resp = request.urlopen(req)

        #读取数据
        data = resp.read().decode("utf-8")

        #写入文件
        with open("./LOL/"+str(i)+".html","w",encoding="utf-8") as  f:
            f.write(data)


def main():
    """
    主函数
    :return:None 
    """
    base_url = "http://tieba.baidu.com/f?"
    start = int(input("请输入开始页码："))
    end = int(input("请输入结束页码:"))

    get_write_lol(base_url, start, end)

if __name__ == '__main__':
   main()