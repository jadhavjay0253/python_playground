# WAP recursive program to find sum of first n natural number:

def nat(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return n + nat(n-1)

n = int(input("Till where: "))
x = (nat(n))
print("Sum is: ",x)