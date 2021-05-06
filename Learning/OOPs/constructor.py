class Empl:
    com = "Google"

    def __init__(self, name, sal): # name must always be init
        self.name = name
        self.sal = sal
        print(f"Employee is created with name {self.name}, and salary of {self.sal}.")

    def getSalary(self, sign): 
        print(f'''Salary of employee working in {self.com} is {self.salary} {sign}.''')
                                           
jay = Empl("Jay", 10000) # calls the constructor automatically
priya = Empl("Priya", 20000)