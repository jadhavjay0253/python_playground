class RailwayForm: # class defination
    formtype = "Railway Form" # class variable
    def printdata(self): # class function
        print(f"Name Is: {self.name} and Train is {self.train}.") #statement

jays = RailwayForm() # object initialisation
jays.name = "Jay" # variable initialisation
jays.train = "Punjab Mail" # variable initialisation
jays.printdata() # function call using object