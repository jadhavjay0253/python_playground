# WA CLASS COMPLEX TO REPRESENT COMPLEX NUMBERS, ALONG WITH OVERLOADED
# OPERATORS + AND * WHICH ADDS AND MULTIPLIES THEM
class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imag = i

    def __add__(self,i):
        return Complex(self.real + i.real, self.imag + i.imag)

    def __str__(self):
        if self.imag<0:
            return f"{self.real} - {-self.imag}i" # to get its positive value
        return f"Number is: {self.real} + {self.imag}i" #returns prope value


    def __mul__(self,i):
        mulreal = self.real * i.real - self.imag * i.imag
        mulimg = self.real * i.imag + self.imag * i.real
        return Complex(mulreal, mulimg)

n1 = Complex(1,-4)
n2 = Complex(331,-37)

print(n1+n2)

print(n1*n2)