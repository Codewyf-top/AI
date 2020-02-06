# # """
# # list
# # tuple
# # dict
# # set
# # """
# # 简单列表
# li = [1,2,3,4,5,6]
# print(type(li))
# li_1=[2,3,4,5,6,7]
# new_li= li+li_1
# print(new_li)
# #
# # #获取列表中的某个元素————通过下标获取，下标从0开始
# # #获取3，下标为2所对应的值就是3
# # li[2]
# # print(li[2])
# # print(li[5])
#
# #通过循环列表
# for tmp in li :
#     print(tmp)
# range(start,end,step)
# li[start:end:step]
# print(li[3:9:1])
# li.append(7)
# li.append(li_1)
# li.extend(li_1)
# print(li)
# li.pop(0)
# val=li.pop(0)
# print(val)

# dic = {"name":"zs","age":18,"hight":180}
#
#
# dic["weight"]=190
#
# dic["name"]="ls"
# for key,val, in dic.items():
#     print("%s:%s"%(key,val))
# li=[1,2,3,4,5,6,6,5,4,3,21,1,2,34,5,62,1,8]
# s_li = set(li)
# new_li= list(s_li)
# print(new_li)
"""
有这样的需求：保存班级里的学生信息class_info是一个列表
class_info里面保存[{},{},{}]，这个字典里面又保存了stu_id:{name,age,hight,score等键值对}
封装成函数，要使用input去输入信息，最后将这些内容写入到文件stu_info.txt文件中去
要求分别封装函数
"""
