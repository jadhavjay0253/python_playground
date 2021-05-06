# SNAKE WATER GUN GAME OR ROCK PAPER SCISSOR

import random

def game(ch,v):
    if(ch==v):
        return None
    elif(ch=="s"):
        if(v=="g"):
            return True
        elif(v=="w"):
            return False
    elif(ch=="g"):
        if(v=="s"):
            return False
        elif(v=="w"):
            return True
    elif(ch=="w"):
        if(v=="s"):
            return True
        elif(v=="g"):
            return False


c = random.randint(1,3) # generates random value between 1 to 3 

print("Computer choice Snake(s) Water(w) Gun(g): ")
if c==1:
    ch = 's'
elif c==2:
    ch ='w'
else:
    ch = 'g'

print("Your choice Snake(s) Water(w) Gun(g): ")
v = input()

print(f"Computer choice {ch} and you choice is {v}.")
m = game(ch,v)

if(m==None):
    print("Game is tie")
elif(m==False):
    print("You lose.")
elif(m==True):
    print("You Won.")