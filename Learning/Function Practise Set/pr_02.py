# WAP to convert celcius into fahrenheit

def convrt(c):
    return (c * (9/5)) + 32 

c = int(input("Enter Celcius "))
x = convrt(c)
print(round(x,2))# puts value upto only 2 decimal

# prevent python from preventing going on next line:
print("Its on new line..",end="")
print(" Im not on new line") # stops from going on new line