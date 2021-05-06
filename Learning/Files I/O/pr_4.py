# replace text of file containing "donkey" with "good"

with open("D:/Work/Python/Learning/Files I/O/d.txt","r") as f:
    s = f.read()
    print(f"Before replacing: {s}")
    if("donkey" in s):
        s = s.replace("donkey","good")
        print(f"After replacing: {s}")
        with open("D:/Work/Python/Learning/Files I/O/d.txt","w") as f:
            f.write(s)