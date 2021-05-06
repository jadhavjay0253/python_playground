# CREATE A CLASS CALCULATOR TO FIND SQRROOT, CUBE, SQUARE OF A NUMBER

class Calculator:

    @staticmethod
    def greet():
        print("Hello User.")

    def sqr(self, n):
        self.nm = n
        print(f"Square of {self.nm} is: ", self.nm**2)
    
    def cbe(self, n):
        self.nm = n
        print(f"Cube of {self.nm} is: ", self.nm * self.nm * self.nm)
    
    def sqrt(self, n):
        self.nm = n
        print(f"Square root of {self.nm} is: ", self.nm**0.5 )

a = Calculator()
a.greet()
a.sqr(2)
a.cbe(2)
a.sqrt(16)