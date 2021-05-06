# WAP to create dictionary for hindi words with english meaning and
# user will be able to fetch value

# mydc = {
#     "haath": "Hand",
#     "dabba": "Box",
#     "chata": "Slap",
#     "rasta": "Road"
# }

# print("Options present are: ",mydc.keys())
# a = input("Enter hindi word to search: ")

# #or print("Fetched Value: ",mydc[a]) --normally
# #or
# print("Meaning Is: ",mydc.get(a)) # -- this will not throw an error if key is not present


# WAP to input 8 numbers and display only unique number
# So by using set we can do it

# a = set()
# i = 0
# for i in range(0,8):
#     x = int(input())
#     a.add(x)
# print("Unique list Is: ",a)

# can we have set of value 18(int) and "18"(str)

# b = {18,"18"}
# print(b) #-- both will be printed as unique one is int and str type
# # also we can have
# b1 = {18,18.5,"18"} # also has float new type in it
# print(b1)

# calculate length of set

# s = {20,20.0,"20"}
# print(len(s)) # will give 2 as 20 and 20.0 are same

# create empty dictionary allow 4 friends to enter their
# favourite language as values and use keys as their name
# assume that names are unique

# dic = {}
# a = input("Enter your favourite language A:\n ")
# b = input("Enter your favourite language B:\n ")
# c = input("Enter your favourite language C:\n ")
# d = input("Enter your favourite language D:\n ")

# # assigning keys as names:
# dic["A"] = a;
# dic["B"] = b;
# dic["C"] = c;
# dic["D"] = d;

# dic["A"] = c; will take latest value of A if we repeated it.

# print(dic)

#we cant store list & dictionary,in a set we can only store tuple