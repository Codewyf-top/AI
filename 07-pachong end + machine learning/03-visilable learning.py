#导包
import matplotlib.pyplot as plt
import numpy as np
# #绘图流程
# #1、创建画布
# plt.figure()
# #2、绘图
# #绘图数据构建
# #构建xy值
# x = [1,2,3,4,5,6]
# y = [2,5,7,8,6,10]
# plt.plot(x,y)
# #3、图形展示
# plt.show()

#1创建画布
plt.figure()
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus']=False
#构建xy
x = np.arange(0,2*np.pi,0.1)#生成一个数组参数1、开始 参数2 结束 参数3 步长（间隔）
print(x)
y1 = np.sin(x)
y2 = np.cos(x)
#进行绘图
# plt.plot(x,y1)
# plt.plot(x,y2)
plt.scatter(x,y1)
plt.scatter(x,y2)
#增加一些修饰
plt.xlabel("x值:")
plt.ylabel("y值:")
#增加图例
plt.legend(['y=sin(x）','y=cos(x)'])

#设置标题
plt.title("三角函数图")

#保存图片
plt.savefig("./x&y的三角函数散点图.png")
#图形展示
plt.show()

