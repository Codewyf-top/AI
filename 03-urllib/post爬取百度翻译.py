# url ="https://fanyi.baidu.com/sug"
# form data  "kw":需要翻译的内容
# 请求方式 post

# post  get区别 --->post 提交数据  请求数据 是放在请求体里面
#get 是拼接url

# 导包
import random
from  urllib import  request,parse
import json

def trans_data(data):
    """
    进行百度翻译，并返回翻译结果
    :param data: 需要翻译的内容
    :return: 翻译的结果
    """
    # 确定url
    url = "https://fanyi.baidu.com/sug"

    # 构建请求数据
    req_data = {
        "kw":data
    }

    # 对req_data进行编码
    fom_data = parse.urlencode(req_data)

    #请求数据长度
    length =len(fom_data)

    # 构建浏览器版本列表
    ua_list = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"
    ]
    # 构建headers
    # 每一随机选择不同的ua
    user_agent = random.choice(ua_list)

    headers = {
        "User-Agent": user_agent,
        "content-length":length
    }

    #构建Request
    req =request.Request(url=url,headers=headers,data=bytes(fom_data,encoding="utf-8"))

    # 发送请求 获取响应
    resp = request.urlopen(req)

    # 获取响应数据---返回json字符串
    json_data = resp.read().decode("utf-8")
    # print(json_data)
    # print(type(json_data))

    # json模块里面有一个loads方法可以把json字符串转化为Python中的类型
    dict_data = json.loads(json_data)
    # print(dict_data)
    # print(type(dict_data))

    # 取字典里面的data键所对应的值为一个列表
    val_list =dict_data["data"]

    # print(val_list)
    res =''
    #循环遍历里面的值，是字典，再取字典里面键为v所对应的值就是我们所翻译的内容，再进行拼接
    for tmp in val_list:
        res += tmp["v"] + '\n'

    # print(res)
    return  res

def main():
    """
    主函数
    :return: 
    """
    trans = input("需要翻译的内容：")

    result = trans_data(trans)

    print(result)

if __name__ == '__main__':
    main()