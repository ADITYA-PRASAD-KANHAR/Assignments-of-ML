# 4. Create a private attribute in a class and access it using a method. 
class PrivateDemo:
    def __init__(self, value):
        self.__private = value
    def get_private(self):
        return self.__private

# Example
pd = PrivateDemo(42)
print(pd.get_private())
