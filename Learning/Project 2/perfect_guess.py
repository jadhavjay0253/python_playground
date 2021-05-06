# PERFECT GUESS GAME

import random

n = random.randint(1,5) # PUT RANGE YOU WANT
#print(n)
g_count = 1
g = None

while(g!=n):
    g = int(input("Guess a number: "))
    if g==n:
        print(f"You guessed {g_count} times to guess it right.")
    else:
        if(g<n):
            print("You guessed it wrong, Enter a larger number..")
        elif(g>n):
            print("You guessed it wrong, Enter a smaller number..")
        g_count+=1
        
with open("hiscore.txt") as f:
    hc = int(f.read())

if g_count<hc:
    print("You have just broken the hi-score.")
    with open("hiscore.txt","w") as f:
        f.write(str(g_count)) # to store hi score in a file