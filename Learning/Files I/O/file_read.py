f = open("D:/Work/Python/Learning/Files/x.txt", 'r') #Bydefault mode is "r of open 2 parameter"
#data = f.read() 
data2 = f.read(4) # only reads first 4 letter but read can only run once

#print(data)

print(data2)

f.close()