# Its best way to open file as file is closed automatically with this.
#  No need to write f.close method separately

with open("x.txt",'w') as f: 
    b = f.write("its me")
print(b)