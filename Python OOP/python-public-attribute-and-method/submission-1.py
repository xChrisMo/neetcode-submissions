class StoreItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        #print(f'Item: [{self.name}] - Price: $[{self.price}]')
        print(self.name)
        print(self.price)

chips = StoreItem("Chips", 1.99) # Don't modify this line

# TODO: Access the attributes of the chips object and display them


chips.display()