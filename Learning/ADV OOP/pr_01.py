# CREATE ANOTHER CLASS 3D VECTOR USING A CLASS 2D VECTOR
class vec2d:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{ self.icap} i + {self.jcap}j"

class vec3d(vec2d):
    def __init__(self, i, j, k):
       super().__init__(i,j)
       self.kcap = k

    def __str__(self):
        return f"{ self.icap} i + {self.jcap}j + {self.kcap}k"

v2d = vec2d(5,6)
v3d = vec3d(5,6,9)
print(v2d)     
print(v3d)       