# 6. Create two objects of a class and demonstrate that they are independent. 
class Independent:
    def __init__(self, value):
        self.value = value

# Example
a = Independent(1)
b = Independent(2)
print(a.value)
print(b.value)

