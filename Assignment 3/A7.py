# 7. Create a class and use a method to set its attributes. 
class SetterDemo:
    def set_attributes(self, name, age):
        self.name = name
        self.age = age

# Example
sd = SetterDemo()
sd.set_attributes("Charlie", 28)
print(sd.name, sd.age)

