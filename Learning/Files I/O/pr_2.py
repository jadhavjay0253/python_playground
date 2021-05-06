# let user play game and update score as in hiscr.txt whichever is greater 
def game():
    return 65

with open("D:/Work/Python/Learning/Files I/O/hiscr.txt") as f:
    hcr = int(f.read())

n = game()
if n>int(hcr) or hcr == '':
    with open("D:/Work/Python/Learning/Files I/O/hiscr.txt","w") as f:
        f.write(str(n))