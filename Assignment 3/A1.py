# 1. Create a simple class `Person` with name and age as attributes. 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Example
p1 = Person("Alice", 30)
print(p1.name, p1.age)
