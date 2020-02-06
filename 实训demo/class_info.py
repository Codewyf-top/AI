class_info = []
stuid = 1
while True:

    a = str(input("please input the name:"))
    b = str(input("please input the age:"))
    c = str(input("please input the hight:"))
    d = str(input("please input the score"))
    stu = {'name':a,'age':b,'hight':c,'score':d}
    stu1 =  {stuid:stu}
    class_info.append(stu1)
    stuid+=1

    sa= str(class_info)
    with open("./stu_id2.txt","w",encoding="utf-8")as f:
        f.write(sa)

        #在查询框内查询数据之后在网络中都进行了哪些操作
        