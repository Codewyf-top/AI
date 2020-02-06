#url  http://www.stat-nba.com/query.php?page=0&QueryType=all&AllType=season&AT=avg&order=1&crtcol=pts&PageNum=20#label_show_result
from urllib import request
import random
from lxml import etree
import numpy as np
import pandas as pd

#页码之间与url之间的关系
#第一页 page=0
#第二页 page=1
#第三页 page=2
#第n页  page=n-1

def get_NBA(start,end):
    """
    爬取NBA球员数据
    :param start: 开始爬取页面
    :param end: 结束爬取页面
    :return: None
    """
    ua_list = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"]

    # proxy_list = [
    #     {"http": "60.216.101.46"},
    #     {"http": "220.168.52.245	"},
    #     {"http": "122.4.47.219"},
    #
    # ]
    columns_name=[]
    data_list=[]
    for i in range (start,end+1):
        #确定每一此爬取的url
        url = "http://www.stat-nba.com/query.php?page=%s&QueryType=all&AllType=season&AT=avg&order=1&crtcol=pts&PageNum=20#label_show_result"% str(i-1)

        # print(url)
        user_agent = random.choice(ua_list)

        headers = {
            "User-Agent": user_agent
        }
        # 随机选择ip
        # proxy_ip = random.choice(proxy_list)
        # # 构建代理服务器
        # proxy_http = request.ProxyHandler(proxy_ip)
        # # 构建管理器托管代理服务器
        # opener = request.build_opener(proxy_http)
        # 构建Request
        req = request.Request(url=url, headers=headers)
        req.add_header("Cache-Control", "max-age=0")
        # 发送http请求，返回响应对象
        resp = request.urlopen(req)
        # # 发送请求
        # req = opener.open(req)

        #获取数据
        data = resp.read()
        #将html 转化为etree对象
        html = etree.HTML(data)
        # print(html)

        #解析etree对象
        #第一步：解析列名
        if not columns_name:
            columns_name = html.xpath('//table[@class="stat_box"]/thead/tr/th/text()')
            columns_name[0] = "序号"
            # print(columns_name)
        #第二步：解析数据
        #1.解析到tr
        tr_list =  html.xpath('//table[@class="stat_box"]/tbody/tr')
        for tr in tr_list:
            tr_data = tr.xpath('./td//text()')
            # print (tr_data)
            data_list.append(tr_data)#二维列表嵌套
    #组成一个大列表
    # print(data_list)
    #将列表转化为numpy里面支持的ndarry类型
    #ndarry类型是一种存储多维数组
    array = np.array(data_list)
    # print(array)
    # print(type(array))

    #将ndarry转化为pandas里面支持的DataFrame结构
    #dataframe 是pandas里面的一种存储二维数据的格式
    #相比于二维ndarry来说，只是多了行索引和列索引
    data_df = pd.DataFrame(array,columns=columns_name)
    # print(data_df)
    return data_df

def save_data (data):
    """
    将爬取到的nba数据保存到excel里面
    :param data: nba数据
    :return: None
    """
    data.to_excel("./nba_data.xlsx",encoding="utf-8",index=False)


def main():
    """
    主函数
    :return: 
    """
    #确定基准url
    base_url = "http://www.stat-nba.com/query.php?page=0&QueryType=all&AllType=season&AT=avg&order=1&crtcol=pts&PageNum=20#label_show_result"
    #确定输入开始结束页码
    start = int(input("please input the start page:"))
    end = int(input("please input the end page:"))

    #调用爬取
    nba_data = get_NBA(start,end)

    #将我们爬取到的nba数据保存到excel里面
    save_data(nba_data)
if __name__ == '__main__':
    main()

