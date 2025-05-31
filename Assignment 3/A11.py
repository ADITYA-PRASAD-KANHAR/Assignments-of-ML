# 11. Demonstrate method overriding in inheritance. 
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

# Example
d = Dog()
d.speak()

