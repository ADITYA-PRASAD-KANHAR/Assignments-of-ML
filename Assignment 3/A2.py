# 2. Add a method to the `Person` class that prints a greeting. 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Example
p2 = Person("Bob", 25)
p2.greet()

