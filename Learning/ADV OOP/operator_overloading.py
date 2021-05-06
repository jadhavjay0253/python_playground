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

n1 = Num(6)
n2 = Num(4)

tot = n1 + n2
print(tot)

tot = n1 * n2
print(tot)

tot = n1 - n2
print(tot)
