# 15.  Demonstrate encapsulation using getter and setter. 
class Encapsulate:
    def __init__(self):
        self.__data = None
    def set_data(self, value):
        self.__data = value
    def get_data(self):
        return self.__data

# Example
e = Encapsulate()
e.set_data(100)
print(e.get_data())
