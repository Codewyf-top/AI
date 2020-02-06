#确定url= https://www.qiushibaike.com/8hr/page/4/

#页面控制与rul之间的关系
#第一页 1
#第二页 2
#第三页 3
#第n页 n
from urllib import request
import random
from lxml import etree
from  urllib import  parse
def get_qiubai(base_url,start,end):
    """
    爬取糗事百科内容
    :param base_url: 基准url
    :param start: 开始的页面
    :param end: 结束的页面
    :return: none
    """
    #构建浏览器版本列表
    ua_list = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"]

    proxy_list = [
        {"http": "60.216.101.46"},
        {"http": "220.168.52.245	"},
        {"http": "122.4.47.219"},

    ]
    for i in range (start,end+1):
        #拼接每一页的url
        url = base_url + "/8hr/page/"+ str(i)+"/"

        user_agent = random.choice(ua_list)

        headers={
            "User-Agent":user_agent
        }
        #随机选择ip
        proxy_ip=random.choice(proxy_list)
        #构建代理服务器
        proxy_http =request.ProxyHandler(proxy_ip)
        #构建管理器托管代理服务器
        opener = request.build_opener(proxy_http)
        #构建Request
        req =  request.Request(url,headers=headers)
        req.add_header("Cache-Control","max-age=0")
        # 发送http请求，返回响应对象
        resp = request.urlopen(req)
        #发送请求
        req = opener.open(req)
        #获取数据
        data=  resp.read()

        #将html数据转化为etree对象
        html = etree.HTML(data)

        #使用xpath提取内容
        #第一步：提取到li
        li_list = html.xpath('//div[@class ="recommend-article"]/ul/li')
        #第二步：循环对每一个li进行单独内容提取
        for li in li_list:
            # print(li)
            #需要提取用户姓名、用户头像链接、用户视频链接、点赞次数、评论次数
            #用户姓名
            user_name=li.xpath('.//span[@class="recmd-name"]/text()')
            if not user_name :
                user_name = None
            else:
                user_name = user_name[0]
            print("username:",user_name)

            #用户头像
            user_image = li.xpath('.//a[@class="recmd-user"]/img/@src')
            if not user_image:
                user_image = None
            else:
                user_image = "https://"+user_image[0]
            print("userimage:",user_image)

            #视频链接
            video_href = li.xpath('./a/@href')
            if not video_href:
                video_href = None
            else:
                video_href = base_url+ video_href[0]
            print("videohref:",video_href)
            #点赞次数
            point_num = li.xpath('.//div[@class="recmd-num"]/span[1]/text()')
            if not point_num:
                point_num = None
            else:
                point_num =  point_num[0]
            print("pointnum:",point_num)
            #评论次数
            content_num = li.xpath('.//div[@class="recmd-num"]/span[last-1]/text()')
            if not content_num:
                content_num = None
            else:
                content_num = content_num[0]
            print("contentnum:",content_num)

            print("♥" * 150)


def main():
    """
    主函数
    :return: 
    """
    #确定基准url
    base_url = "https://www.qiushibaike.com"
    #确定输入开始结束页码
    start = int(input("please input the start page:"))
    end = int(input("please input the end page:"))

    #调用爬取
    get_qiubai(base_url,start,end)
if __name__ == '__main__':
    main()