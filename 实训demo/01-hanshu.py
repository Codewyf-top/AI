# # # def print_star():
# # #     i = 1
# # #     while i <= 5:
# # #         j = 5
# # #         while j >= i:
# # #             print("*", end="")
# # #             j -= 1
# # #         i += 1
# # #         a = 100
# # #         print("hello world")
# # #         print("device")
# # #         return a
# # #
# # # #调用
# # # res = print_star()
# # # print(res)
# # # #
# # # # print(res)
# # # def sum_(a,b):
# # #     print(a)
# # #     print(b)
# # #     return a+b
# # # re=sum_(4,5)
# # # print(re)
# # def sum_(a,b,c):
# #     print(a)
# #     print(b)
# #     print(c)
# #     return a+b+c
# # res = sum_(1,2,3)
# # print(res)
# def b():
#     print("doing b")
# def a():
#     print("start a")
#     b()
#     print("end a ")
#
# a()
def get(a):
    i=0
    while i<=a:
        j=1
        while j<=i:
            print("*",end="")
            j += 1
        print ()
        i += 1
get(7)

def print_(a):
    num =a
    while num >0:
        print("*" * num)
        num -= 1
res = print_(10)