class Emp:
    salary = 5600
    bonus_salary = 400

    #hardcoded
    #total_salary = 454000

    #def total_salary using property decorator
    
    @property # also called as property getter DECORATOR
    def total_salary(self):
        return self.salary + self.bonus_salary

    #ABSTRACTION
    @total_salary.setter # setter DECORATOR to set value
    def total_salary(self,val):
        self.bonus_salary = val - self.salary

e = Emp()

print(e.total_salary) # used total salary as a variable
e.total_salary = 5800

print(e.salary)

print(e.bonus_salary)