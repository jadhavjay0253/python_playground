# VECTOR

class Vector:
    def __init__(self,vec):
        self.vec = vec
    
    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} + "
            index += 1
        return str1[:-2] # to escape 2 from back

    def __add__(self,vec2):
        newlist = []
        for i in range(len(self.vec)):
            newlist.append(self.vec[i]+vec2.vec[i])
        return Vector(newlist) #returns vector quantity
    
    def __mul__(self,vec2): #dot product
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i]*vec2.vec[i]
        return sum #returns scalar quantity not vector

v1 = Vector([1, 4, 6])
v2 = Vector([1, 6, 9])

print(v1)

print(v1+v2)

print(v1*v2)