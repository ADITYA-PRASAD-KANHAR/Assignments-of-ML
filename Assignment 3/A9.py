# 9. Demonstrate single inheritance in Python. 
class Parent:
    def show(self):
        print("Parent class")

class Child(Parent):
    pass

# Example
c = Child()
c.show()