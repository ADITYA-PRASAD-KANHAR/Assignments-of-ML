# 10. Create a base class and derive two child classes with different methods(multi-level inheritance). 
class Base:
    def base_method(self):
        print("Base method")

class Child1(Base):
    def child1_method(self):
        print("Child1 method")

class Child2(Child1):
    def child2_method(self):
        print("Child2 method")

# Example
obj = Child2()
obj.base_method()
obj.child1_method()
obj.child2_method()
