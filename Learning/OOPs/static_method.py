from datetime import datetime

class A1:
    @staticmethod #called as decorator to modify function 
    def greet(): # if no need of self no dynamic value accesing then 
        print("Good Morning Sir.")

    @staticmethod # one more
    def ti():
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current time is: ",current_time)


r = A1()
r.greet()
r.ti()