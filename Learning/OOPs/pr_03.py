# INITIALISE CLASS ATTRIBUTE A=0, CHANGE IT FORM OBJECT
# DOES IT CHANGE CLASS ATTRIBUTE

class Xy:
    a = 0
    def pr(self):
        print(f"a is {self.a}")

c = Xy()
c.a = 10
c.pr()
print("Class a is:",Xy.a)

Xy.a = 20 # this will change a value of class

print("Class a is:",Xy.a)
# no it doesnt change class attribute