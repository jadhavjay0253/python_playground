class Person:
    country = "INDIA"
    def __init__(self):
        print("its base constructor")

    def takeBreath(self):
        print("Yes Iam breathing.")

class Emp(Person): # inherits person
    def takeBreath(self):
        print("Yes Iam EMP and Iam also breathing.")

class Prog(Emp): 

    def __init__(self):
        super().__init__() # CALLS BASE CLASS CONTRUCTOR
        print("its child constructor")

    def takeBreath(self):
        super().takeBreath() # calls previous class's method 
        print("Iam a programmer and breathing++.")
    a=0

p = Person()
p.takeBreath()

e = Emp()
e.takeBreath()

pr = Prog()
pr.takeBreath()