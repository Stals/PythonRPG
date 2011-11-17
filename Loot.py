import Item
from statistics import *

## Возвращает рандомную вещь как вознгараждение
class Loot:
    def __init__(self):
        pass

    ## Возвращает случайную вещь
    def getLoot(self):
        #TODO return a true random item
        return Item.Weapon("Fire Sword",Stats(),Damage(1,10))