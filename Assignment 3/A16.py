# 16. Write a program to demonstrate polymorphism with a common method. 
class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

def animal_sound(animal):
    animal.sound()

# Example
cat = Cat()
dog = Dog()
animal_sound(cat)
animal_sound(dog)

