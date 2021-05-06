# VECTOR
# WRITE STR METHOD  TO PRINT VECTOR AS 
# 7i + 8j + 10k format

class Vector:
    def __init__(self,vec):
        self.vec = vec
    
    def __str__(self):
        str1 = ""
        index = 0
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k" # to escape 2 from back

v1 = Vector([1, 4, 6])
v2 = Vector([1, 6, 9])

print(v1)
print(v2)