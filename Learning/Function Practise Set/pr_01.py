# find greatest of 3 number
def grt(n1, n2, n3):
    if(n1>n2):
        if(n1>n3):
            return n1
        else:
            return n3
    else:
        if(n2>n3):
            return n2
        else:
            return n3

x = grt(12, 44, 95)
print("Greatest is ", x)