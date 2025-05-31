# 3. Create a class with a class variable and instance variable. 
class MyClass:
    class_var = "I am a class variable"
    def __init__(self, value):
        self.instance_var = value

# Example
obj1 = MyClass(10)
obj2 = MyClass(20)
print(MyClass.class_var)
print(obj1.instance_var, obj2.instance_var)
