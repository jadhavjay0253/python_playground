# WAP to store seven fruits in a list entered by user.
# l = []
# v=7

# while v>0:
#     n = input()
#     l.append(n)
#     v -= 1

# print(l)

# 2. WAP to accept marks of 6 students and display in sorted manner

# l2 = []
# v = 6
# while v>0:
#     n = int(input())
#     l2.append(n)
#     v -= 1
# l2.sort()
# print(l2)

# 3. Check that a tuple can't be changed in python
tx = (4,8,3,1)
# tx[1] = 5 # will give error

# 4. Write a program to sum a list of 4 numbers
l3 = [50, 10, 20, 50]

print(l3[0] + l3[1] + l3[2]+ l3[3])
# or 
print(sum(l3))

# 5. WAP to count 0 in following tuple a = (7,0,8,0,0,9)

a = (7,0,8,0,0,9)
print(a.count(0))
