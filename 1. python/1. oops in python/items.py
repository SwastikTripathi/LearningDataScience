class Item:
    pay_rate = 0.8 # default discount of 20% on all items
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # validate inputs
        assert price >= 0, "price should not be negative"
        assert quantity >= 0, "quantity should not be negative"

        # assign values
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
    
    def calculatePrice(self):
        return self.price*self.quantity
    
    def priceAfterDiscount(self):
        return self.price*self.pay_rate
    
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 50, 10)
item4 = Item("Mouse", 80, 3)
item5 = Item("Keyboard", 75)

item4.pay_rate = 0.7

print(Item.all.__str__())

for item in Item.all:
    print(item.priceAfterDiscount())