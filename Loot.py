import Item
from Stats import *
from Damage import *
#TODOlater Если буде делать бесполезный лут то сделать stacable вещи которые добавляются в 1, тупо увеличивая кол-во

## Возвращает рандомную вещь как вознгараждение
class Loot:
    def __init__(self):
        pass

    ## Возвращает случайную вещь
    def getLoot(self):
        #TODO return a true random item
        return Item.Weapon("Fire Sword",Stats(),Damage(1,10))