import Item
from statistics import *

class Loot:
    def __init__(self):
        pass
    def getLoot(self):
        #TODO return a true random item
        return Item.Weapon("Fire Sword",stats(),damage(1,10))