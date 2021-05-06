# CREATE A CLASS EMP & ADD SALARY, INCREMENT PROPERTIES TO IT
# WRITE A METHOD Salary After Increment  with a @property decorator with setter to change
# value of increment based on salary

class EMP:
    salary = 1000
    ic = 1.5

    @property
    def salaryincrement(self):
        return self.salary * self.ic
    
    @salaryincrement.setter
    def salaryincrement(self, sai):
        self.ic = sai/self.salary

e = EMP()
print("Increamented salary: ",e.salaryincrement)
print(e.ic)
e.salaryincrement = 2000
print("Increment after running setter is: ", e.salaryincrement)
print(e.ic)