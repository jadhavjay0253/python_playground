# Tuples are immutable can't be changed

t1 = (1,4,5,1,3,1)
print(t1)

t = ()
print(t) #empty tuple

# t2 = (1) #wrong declaration for tuple with one element it should have comma
t2 = (1,)
print(t2)

# Functions--------------------------------------

print(t1.count(1)) # --return no.of time element occured
print(t1.index(3)) # returns index where it is present only first occurence