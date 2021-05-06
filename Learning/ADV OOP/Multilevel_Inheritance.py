class Person:
    country = "INDIA"
    def takeBreath(self):
        print("Yes Iam breathing.")

class Emp(Person): # inherits person
    def takeBreath(self):
        print("Yes Iam EMP and Iam also breathing.")

class Prog(Emp): # inherits emp
    # def takeBreath(self):
    #     print("Iam a programmer and breathing++.")
    a=0

p = Person()
p.takeBreath()

e = Emp()
e.takeBreath()

pr = Prog()
pr.takeBreath()#->it will print latest class's method if pr doesnt have takebreath in it
print(pr.country) # doesnt have of own but will access of person class