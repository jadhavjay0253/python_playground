# MODES OF OPEN:
# r - open for read
# w - open for write
# a - open for append
# + - open for update
# rb -for binary
# rt - for read in text mode

# Opening in write mode and writing data
# overwrites whole data
# f = open("an.txt","w")
# f.write("Iam writing to a file")
# f.close()

# Opening in append mode and writing data
# adds data at end of file content
f = open("an.txt","a")
f.write(" Iam adding the text") #->keeps adding data till we call write method
f.close()
