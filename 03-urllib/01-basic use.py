import urllib.request
from urllib import request
#以百度首位为例
base_url = "http://www.baidu.com"

#发送http请求,并返回响应
response = request.urlopen(base_url)
print(response)

#获取数据
data = response.read().decode("utf-8")
print(data)

with open("./baidu.html","w",encoding="utf-8") as f:
    f.write(data)

def get_baidu():
    """
    获取百度首页信息
    :return: 百度首页信息
    """
    base_url = "http://www.baidu.com"
    response = request.urlopen(base_url)
    print(response)

    data = response.read().decode("utf-8")
    # print(data)
    return data
def write_info(data):
    f.write(data)

def main():
    """
    主业务逻辑
    :return: none
    """
    #获取百度信息
    baidu_data = get_baidu()
    #保存文件
    write_info(baidu_data)

if __name__ == '__main__':
    main()

#作业 爬取jd首页,写到文件中
#url  = "http://www.jd.com"