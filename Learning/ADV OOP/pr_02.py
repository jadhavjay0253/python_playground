# CREATE A CLASS PETS FROM CLASS ANIMALS AND FURTHER CREATE ANIMALS 
# AND FURTHER CREATE A CLASS DOG FROM PETS, ADD BARK METHOD TO CLASS DOG

class Animals:
    am1 = "dog"
    am2 = "horse"

class Pets(Animals):
    r1 = "rainer"

class Dog(Pets):
    @staticmethod
    def bark():
        print("Dog is barking from dog class.")

d = Dog()
print(d.am1)
d.bark()