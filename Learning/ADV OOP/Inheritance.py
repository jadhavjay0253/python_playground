# SINGLE INHERITANCE

class Emp():
    company = "Google"
    def showdet(self):
        print("Iam a employee")

class Programmer(Emp): # inherits parent class Emp
    language = "python"

    def getla(self):
        print(f"Language is {self.language}")
    
    def showdet(self): #FUNCTION OVERRIDING
        print("Iam a programmer")

e = Emp()
p = Programmer()

e.showdet()
p.showdet() # both gives same output

# but what if we make 2 show det in both classes -- results will change

# function overriding