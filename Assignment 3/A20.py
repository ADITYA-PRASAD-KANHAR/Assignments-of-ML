# 20.  Create a class `Rectangle` with method to calculate area and perimeter. 
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)

# Example
rect = Rectangle(4, 5)
print(rect.area())
print(rect.perimeter())