class Item():
    """Crates an item for the inventory"""
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name.title()



class Money():
    """Creates a monetary item for the inventory"""
    def __init__(self, value):
        self.value = value
    
    def pay(self, amount):
        self.value -= amount

    
    def __str__(self):
        return "{}€".format(self.value)


class Inventory():
    """Creates an inventory, with one included start Item"""
    def __init__(self):
        self.contents = []
        self.money = Money(20)

    def add(self, item):
        self.contents.append(item)
    
    def __str__(self):
        i ="Your bag contains:\n"
        i += str(self.money)+"\n"
        for item in self.contents:
            i += str(item)
            i += "\n" 
        return i

