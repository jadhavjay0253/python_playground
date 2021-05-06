class Em:
    company = "GO"
    ecode = 110

class We:
    company = "fiver"
    level = 10

class Ca(Em, We): # MULTIPLE INHERITANCE
    cam = 10

c = Ca()

# WE CAN CALL ABOVE CLASSES MEMBER FROM LAST CLASS'S OBJECT

print(c.level)
print(c.ecode)

# AMBIGUITY

print(c.company) #--> gives GO because we inherited Em first then we if
                 # we is 1 then fiver will be print