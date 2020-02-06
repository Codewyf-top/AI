import urllib.request
from urllib import request
base_url = "http://www.gaoqing111.com"

#发送http请求,并返回响应
response = request.urlopen(base_url)
print(response)

#获取数据
data = response.read()
print(data)

with open("./gaoqing111.html","wb") as f:
    f.write(data)

def get_gaoqing():
    """
    获取百度首页信息
    :return: 百度首页信息
    """
    base_url = "http://www.gaoqing111.com"
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
    gaoqing_data = get_gaoqing()
    #保存文件
    write_info(gaoqing_data)

if __name__ == '__main__':
    main()