# CREATE A CLASS TRAIN AND SHOULD HAVE METHODS TO BOOK, GET STATUS N ALL

class Train:
    def __init__(self, name, seats, fare):
        self.name = name
        self.seats = seats
        self.fare = fare
    def getStatus(self):
        print("######################################")
        print(f"The name of train is: {self.name}")
        print(f"Seats available: {self.seats}")
        print("######################################")
    
    def fareInfo(self):
        print(f"The fare is: Rs.{self.fare}")
    
    def book(self):
        if self.seats>0:
            print(f"Your ticket has been booked, Your seat number is {self.seats}")
            self.seats -= 1
        else:
            print("Sorry this train is full, check with another one.")

    def canCel(self):
            self.seats += 1
            print("Ticket is sucessfully cancelled.")

intrcity = Train("IntracityExpress: 14014", 2, 30)   
intrcity.getStatus() 

intrcity.fareInfo()  

intrcity.book()

intrcity.getStatus() 

intrcity.book()

intrcity.getStatus()

intrcity.book()

intrcity.getStatus()

intrcity.canCel()

intrcity.getStatus()