class Animal:
    def __init__(self, habitat):
        self.habitat = habitat
    def printHabitat(self):
        print(self.habitat)
    def sound(self):
        print('some animal sound')

class Dog(Animal):
    def __init__(self, habitat):
        super().__init__(habitat)
    def sound(self):
        print('woof woof')

ob = Animal('river')
ob.printHabitat()
ob.sound()
ob1 = Dog('canal')
ob1.printHabitat()
ob1.sound()