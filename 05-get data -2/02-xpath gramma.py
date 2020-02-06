from lxml import etree
text="""
<div>
    <ul>
        <li class="item-0"><a href="link1.html">first item</a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html">third item</a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
        <image href="www.baidu.com">
    </ul>
</div>
"""

#将html页面转化为可以用于xpath语法提取数据的etree类型
html = etree.HTML(text)

#使用xpath语法提取数据


# data=html.xpath("//div/ul/li[last()]/a/text()")[0]
li_list =html.xpath("//div/ul/li")
# print(data)
data_list=[]
for tmp in li_list:
    data = tmp.xpath("./a/text()")[0]
    print(data)
    data_list.append(data)
print(data_list)