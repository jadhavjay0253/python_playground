class Empl:
    com = "Google"
    def getSalary(self, sign): # self refers to the object of which it is
        print(f"Salary of employee working in {self.com} is {self.salary} {sign}.") # will work with object which is calling this method
                                           # in our case jay is object so self-> jay.salary=100000

jay = Empl()

jay.salary = 100000
jay.getSalary("thanks") # Empl.getSalary(jay) -->same|| parameter also passed 