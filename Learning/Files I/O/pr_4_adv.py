# replace text of file containing "donkey" with "good"
words = ["donkey", "are"]

with open("D:/Work/Python/Learning/Files I/O/d.txt","r") as f:
    s = f.read()
    print(f"Before replacing: {s}")
    for word in words:
        with open("D:/Work/Python/Learning/Files I/O/d.txt","w") as f:
            s = s.replace(word,"$$")
            print(f"After replacing: {s}")
            f.write(s)