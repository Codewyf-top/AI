import json
import random
from jsonpath import jsonpath
from urllib import request


def get_LG(url):
    """
    paqu lg city data
    :param url: 
    :return: 
    """
    #自行构建随机
    ua_list = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"]

    # proxy_list = [
    #     {"http": "60.216.101.46"},
    #     {"http": "220.168.52.245	"},
    #     {"http": "122.4.47.219"},
    #
    # ]
    user_agent = random.choice(ua_list)

    headers = {
        "User-Agent": user_agent
    }
    # # 随机选择ip
    # proxy_ip = random.choice(proxy_list)
    # # 构建代理服务器
    # proxy_http = request.ProxyHandler(proxy_ip)
    # # 构建管理器托管代理服务器
    # opener = request.build_opener(proxy_http)
    #构建Request
    request.Request(url,headers=headers)
    req = request.Request(url, headers=headers)
    req.add_header("Cache-Control", "max-age=0")
    #发送请求
    # resp = opener.open(req)
    resp = request.urlopen(req)

    json_data = resp.read().decode("utf-8")
    # print(type(json_data))
    print(json_data)
    dict_data = json.loads(json_data)

    #解析数据
    city_list = jsonpath(dict_data,"$..name")
    print(city_list)

    #保存数据
    with open("./LG_city.txt","w",encoding="utf-8") as f:
        json.dump(city_list,f,ensure_ascii=False,indent=4)

def main():
    """
    主函数
    :return: 
    """
    # 确定url
    url ="http://www.lagou.com/lbs/getAllCitySearchLabels.json"

    #调用函数爬取数据并进行保存
    get_LG(url)

#调用主函数
if __name__ == '__main__':
    main()