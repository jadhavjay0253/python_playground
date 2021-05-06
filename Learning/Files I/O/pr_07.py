# WAP TO CREATE COPY OF THIS.TXT AS COPY.TXT
with open("x.txt") as f:
    content = f.read()

with open("copy_this.txt","w") as f:
    f.write(content)