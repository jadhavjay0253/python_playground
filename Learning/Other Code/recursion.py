# normally
# def fct(n):
#     prd = 1
#     for i in range(1,n+1):
#         prd = prd * i
#     return prd

# recursion
def fct_recursion(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fct_recursion(n-1) # call fct for its n-1 value

t = int(input("Enter for fact: "))
b = fct_recursion(t)
print(b)