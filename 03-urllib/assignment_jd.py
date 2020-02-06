import urllib.request
from urllib import request
base_url = "http://www.jd.com"

#发送http请求,并返回响应
response = request.urlopen(base_url)
print(response)

#获取数据
data = response.read().decode("utf-8")
print(data)

with open("./jd.html","w",encoding="utf-8") as f:
    f.write(data)

def get_jd():
    """
    获取jd首页信息
    :return: jd首页信息
    """
    base_url = "http://www.jd.com"
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
    #获取jd信息
    baidu_data = get_jd()
    #保存文件
    write_info(jd_data)

if __name__ == '__main__':
    main()