# 17.  Create a class `Employee` with a method to display the number of employees created. 
class Employee:
    count = 0
    def __init__(self, name):
        self.name = name
        Employee.count += 1
    @classmethod
    def display_count(cls):
        print("Number of employees:", cls.count)

# Example
e1 = Employee("A")
e2 = Employee("B")
Employee.display_count()
