# print table for an input value:
# n = int(input("Enter number:\n"))
# for i in range(1,11):
#     print(i ," X ", n," = ",n*i)

# WAP TO GREET ALL NAMES INLIST STARTING WITH LETTER S using for loop

# l = ["jay","ram", "sita","sundar","kriti", "saksham"]

# for b in l:
#     if(b.startswith("s")):
#         print("Hello ",b)

#WAP TO CHECK NO. IS PRIME OR NOT;
# n = int(input())
# prime = True
# for i in range(2,n):
#     if(n%i==0):
#         prime = False
#         break
# if(prime):
#     print("Given no. is prime.")
# else: 
#     print("Given no. is not prime.") 

# WAP TO FIND FACTORIAL OF NO.
# 5! = 1*2*3*4*5
# n!= 1*2*3.....n
#CODE-------------------------------------------------
# z = int(input())
# fct = 1
# for i in range(1,z+1):
#     fct *= i 
# print("Factorial is: ",fct)

# PRINT 
#   *
#   * *
#   * * *
# for i in range(0,4):
#     print("*" * (i+1))

# PRINT 
#     *
#   * * *
# * * * * *
#-------------------------------------
#  n=3
# for i in range(3):
#     print(" " * (n-i-1),end="")
#     print("*" * (2*i+1),end="")
#     print(" " * (n-i-1))

# print table for an input value in reverse order:
n = int(input("Enter number:\n"))
for i in range(11,0,-1):
    print(i ," X ", n," = ",n*i)