# WAP TO WIPE OUT DATA OF A FILE
with open("an.txt") as f:
    dt = f.read()
    print(f"Data present in file before wiping: \n{dt}")

dt = ""
with open("an.txt","w") as f1:
    f1.write(dt)
    print("Data has been wiped out succesfully.")