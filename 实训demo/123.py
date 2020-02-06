i=1
while i<=5:
    j=5
    while j>=i:
        print("*",end="")
        j -= 1
    i += 1
    print()


    def print_(a):
        num = a
        while num > 0:
            print("*" * num)
            num -= 1


    res = print_(10)