class Emp:
    com = "BYJUS"
    salary = 450000
    loc = "Nasik"

    # def changeSalary(self, s): # (1 method)to change class salary, not instance salary 
    #     self.__class__.salary = s #(called dender class)

    @classmethod #bounded to class not object
    def changeSalary(cls, s): # (2 method)to change class salary, not instance salary 
        cls.salary = s

e = Emp()

print(e.salary)
e.changeSalary(500000)
print(e.salary)