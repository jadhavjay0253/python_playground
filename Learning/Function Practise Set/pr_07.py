# wap to remove a given word from string and strip it (remove extra spaces in string)

def remv_split(str, w):
    str = str.replace(w, "") # will replace given string with blank
    return str.strip() #it will remove blank spaces

t = "   Jay is very good.   "
print("Before Calling: ",t)
print("After call:\t",remv_split(t,"very"))