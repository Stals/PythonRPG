from Item import Item
from utils import getChoice as utils
#Хранит вещи игрока

#TODO сделать максимально переносимое число вещей ( зависит от Stamina )
#или как в линеечке, все дать стандартное кол-во слотов, а гномам +20 слотов, ибо барыги же 
#TODO Сделать чтобы при выводе через getChoice использовали player.inventory.items()  // И ДЛЯ ДРУГИХ ТИПО POTIONSPOCKET

## Инвентарь (Хранит наследники Item)
class Inventory:
    def __init__(self):
         self.inventory = []

    ## Добавляет item в inventory
    def addItem(self, item):
        self.inventory.append(item)
        self.__sort()


    def removeItem(self, item):
        """Убирает item из инвентаря если он там есть"""
        if item in self.inventory:
            self.inventory.remove(item)

    def removeSelectedItem(self): #TODO rename
        """Даёт выбор какую вещь выкинуть из инвентаря"""
        if self.inventory:
            selectedItem = utils.getChoice("Which item to drop?", self.inventory, cancel=True)
            if selectedItem:
                self.removeItem(selectedItem)
                print("Droped "+selectedItem.__str__()+"\n")
        else:
            print("Inventory is empty\n")

    ## Возвращает список всех вещей в инвентаре
    def items(self):
        return self.inventory

    ## Сортирует вещи по типу - Ботинки / Шлем / Оружие и тд
    def __sort(self):#TODO сделать сортировку по типу Ботинки вместе, оружие вместе и тд (тогда у Оружия тоже должен быть piece)
        pass
    
    ## Возвращает список всех вещей в инвентаре в виде строки
    def __str__(self):
        result = ""
        if self.inventory:
            result = "\n".join(map(str, self.inventory))
        else: #inventory is empty
            result = "empty"
        return result
