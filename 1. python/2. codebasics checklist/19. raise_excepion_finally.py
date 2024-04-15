class AdultException(Exception):
    pass

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def getMinorAge(self):
        if self.age > 18:
            raise AdultException
        else:
            return self.age
    
    def display_age(self):
        try:
            print('Age -> ',str(self.getMinorAge()))
        except AdultException:
            print('person is adult')
        finally:
            print('Name -> ',self.name)

ob1 = Person('Ron', 15)
ob2 = Person('Ginny', 24)
ob1.display_age()
ob2.display_age()