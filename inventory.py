# -*- coding: utf-8 -*-
# Creates items and an inventory.
# Eileen Niedenführ | Matrikelnr. 811770
# Datum

class Item():
    """
    Creates an item for the inventory.
    """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name.title()


class Money():
    """
    Creates a monetary item for the inventory
    """
    def __init__(self, value):
        """
        Gets initialized with a numerical value.
        """
        self.value = value

    def pay(self, amount):
        """
        Function to reduce the value.
        Keyword arguments:
        amount -- int: Amount that is to be substracted.
        """
        self.value -= amount

    def __str__(self):
        return "{}€".format(self.value)


class Inventory():
    """
    Creates an inventory, with an empty list
    and included start money.
    """
    def __init__(self):
        self.contents = []
        self.money = Money(20)

    def add(self, item):
        """
        Function to add items to the inventory.
        """
        self.contents.append(item)

    def __str__(self):
        """
        Pretty printing the inventory instance.
        """
        i = "\nYour bag contains:\n"
        i += str(self.money)+"\n"
        for item in self.contents:
            i += str(item)
            i += "\n"
        return i
