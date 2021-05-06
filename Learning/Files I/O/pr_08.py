# WAP TO FIND IF TWO FILES ARE IDENTICAL OR NOT

with open("x.txt") as f:
    data1 = f.read()
    
with open("copy_this.txt") as f1:
    data2 = f1.read()
        
if data1 == data2:
    print("Both the files are identical.")
else:
    print("Both the files are not identical.")