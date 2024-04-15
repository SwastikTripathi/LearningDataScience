import csv

class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # assertions
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero"

        # assigning values
        self.name = name
        self.price = price
        self.quantity = quantity

        # add object to all[]
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # call init of super and run its intialization
        super().__init__(
            name, price, quantity
        )

        # assertions
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal to zero"

        # assigning values
        self.broken_phones = broken_phones

phone1 = Phone("jscPhonev10", 500, 5, 1)

# print(Item.all)
Item.instantiate_from_csv()
print(Item.all)