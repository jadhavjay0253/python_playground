# readline reads a single line in file

f = open("D:/Work/Python/Learning/Files/x.txt")
datt = f.readline() # -->gives first line
print(datt)
datt = f.readline() # -->gives second line but with gap bcox after 1 line we get \n
print(datt)
f.close()