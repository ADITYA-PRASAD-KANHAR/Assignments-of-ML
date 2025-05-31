# 12. Use `super()` to call a parent class method. 
class Parent:
    def display(self):
        print("Parent display")

class Child(Parent):
    def display(self):
        super().display()
        print("Child display")

# Example
c = Child()
c.display()