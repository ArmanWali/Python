class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):   # Dog class inherit from class Mammal
    def bark(self):
        print('Bark')
    

class Cat(Mammal):
    def talk(self):
        print("Meow")


dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.talk()