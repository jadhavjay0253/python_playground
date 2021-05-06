# OPERATOR OVERLOADING
# __ --> is known as dunder method.
class Num:
    def __init__(self, num):
        self.num = num

    def __add__(self, nm2): # gets called on addition operation
        print("Let's add..")
        return self.num + nm2.num

    def __sub__(self, nm2): # gets called on addition operation
        print("Let's sub..")
        return self.num - nm2.num

    def __mul__(self,nm2): # gets called on multplication operation
        print("Let's multiply..")
        return self.num * nm2.num

    def __str__(self): # additional
        return f"Decimal Number is: {self.num}" #returns prope value

    def __len__(self): # additional
        return 1

n1 = Num(6)
n2 = Num(4)

print(n1) # without dender method it will not
          # print value, after __str method we can get proper output

print(len(n1))