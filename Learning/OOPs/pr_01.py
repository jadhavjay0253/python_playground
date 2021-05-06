# CREATE A CLASS PROGRAMMER having company MICROSOFT FOR STORE INFORMATION OF SOME PROGRAMMERS 
class Programmer:
    company = "Microsoft"

    def __init__(self,name, prd):
        self.name = name
        self.prd = prd
    
    def getDet(self):
        print(f"Employee's name is {self.name}, company in which he works in {self.company}, and product is {self.prd}.")

jay = Programmer("Jay", "Git")
soniya = Programmer("Soniya", "Hub")

jay.getDet()
soniya.getDet()