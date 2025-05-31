# 18.  Demonstrate constructor overloading using default arguments. 
class Demo:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

# Example
d1 = Demo()
d2 = Demo(5)
d3 = Demo(5, 10)
print(d1.a, d1.b)
print(d2.a, d2.b)
print(d3.a, d3.b)

