#基本使用
from lxml import etree
text = """
<div>
    <ul>
        <li class="item-0"><a href="link1.html">first item</a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html">third item</a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a>
        <image href="www.baidu.com">
    </ul>
</div>
"""
html = etree.HTML(text)
print(html)
print(type(html))

#转化为页面
res = etree.tostring(html)
print(res) # 二进制页面

# 解码
data = res.decode("utf-8")
print(data)

