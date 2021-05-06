# WAP TO READ DATA FROM POEM.TXT AND FIND IF IT CONTAINS 'TWINKLE OR NOT'
with open("D:/Work/Python/Learning/Files I/O/poems.txt","r") as f:
    d = f.read()

if 'twinkle' in d:
    print("Yes, present")
else:
    print("Not present")    