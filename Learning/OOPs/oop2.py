class Emp:
    salary = 300000

jay = Emp()
tanisha = Emp()

jay.salary = 400000 #object refrence then value updated

print("Of Jay: " ,jay.salary)
print("Of Tanisha: ",tanisha.salary) # but tanisha will have salry of class only