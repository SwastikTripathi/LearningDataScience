class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def printEmployee(self):
        print(self.id,' ',self.name)
    
ob1 = Employee(1, 'rohan')
ob2 = Employee(2, 'Sanskriti')
ob1.printEmployee()
ob2.printEmployee()
del ob1.id
# ob1.printEmployee()
del ob1
# ob1.printEmployee()