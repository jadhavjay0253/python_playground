a = set()
print(type(a))

a.add(4)
a.add(5)
a.add(8)
a.add(2)
a.add(4) # adding value repeatedly doesnot make new memory
a.add(3)

# if we add list to set it gives error unhashable
#a.add([1,2,3,4])

# if we add tuple to set it accepts
a.add((1,2,3,4))

# if we add dictionary to set it gives error unhashable
#a.add({3:4})

print(a) 

print(len(a))#-- returns length

a.remove(3) # removes 3 from set a
print(a)

a.pop() # removes random element from set
print(a)

# intersection()	Returns a set, that contains only element from both sets
# union()	Return a set containing the all values of both sets

# Clears the set
a.clear() 
print("After Clearing elements: ",a)