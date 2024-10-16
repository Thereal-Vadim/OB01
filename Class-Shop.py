class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_item_price(self, item_name):
        return self.items.get(item_name)

    def update_item_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

    def __repr__(self):
        return f"Store(name={self.name}, address={self.address}, items={self.items})"


store1 = Store("Fruit Paradise", "123 Street")
store2 = Store("Veggie Market", "456 Ave")
store3 = Store("Healthy Store", "789 Road")

store1.add_item("apples", 15)
store1.add_item("bananas", 10)
store2.add_item("carrots", 25)
store2.add_item("lettuce", 20)
store3.add_item("oranges", 90)
store3.add_item("watermelons", 350)

print(store1)
store1.add_item("grapes", 150)
store1.update_item_price("apples", 60)
print(store1.get_item_price("apples"))
store1.remove_item("bananas")
print(store1)
