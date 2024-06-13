class Point:
    def __init__(self, x, y) :   # constructor
        self.x = x
        self.y = y
        
    def move(self):
        print("move")
    
    def draw(self):
        print("draw")

    
point1 = Point(10, 20) 
print(point1.x)

# Exercise Question

class Person:
    def __init__(self, name) :
        self.name = name
    
    def talk(self):
        print(f"Hello, I am {self.name}")


person1 = Person("Arman wali")
print(person1.talk())
