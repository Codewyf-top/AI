# # #实现数据的持久化存储
# # #打开文件 操作文件（读/写） 关闭文件
# # # fp = open("123.py","r",encoding="utf-8")
# # # con = fp.read()
# # # print(con)
# # #
# # # fp.close()
# #
# fp=open("./gg.txt","a",encoding="utf-8")
#
# fp.write("乘夜枫韵百叶风云")
# fp.close
# #
# # with open ("123.py","r",encoding="utf-8") as f:
# #     con = f.read()
# #     print(con)
#
with open("123.py","r",encoding="utf-8") as f:
    while True:
        con=f.readline()
        if not con:
            break
    print(con,end="")
    print("*"*20)