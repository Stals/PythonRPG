from Item import Item
#Хранит вещи игрока

#TODO сделать максимально переносимое число вещей ( зависит от Stamina )
#TODO Сделать чтобы при выводе через func использовали player.inventory.items()  // И ДЛЯ ДРУГИХ ТИПО POTIONSPOCKET

## Инвентарь (Хранит наследники Item)
class Inventory:
    def __init__(self):
         self.inventory = []

    ## Добавляет item в inventory
    def addItem(self,item):
        self.inventory.append(item)
        self.__sort()

    ## Убирает item из инвентаря
    def removeItem(self,item):
        if item in self.inventory:
			# if item is in invenrory it will be removed
            self.inventory.remove(item)

    ## Возвращает список всех вещей в инвентаре
    def items(self):
        return self.inventory

    ## Сортирует вещи по типу - Ботинки / Шлем / Оружие и тд
    def __sort(self):#TODO сделать сортировку по типу Ботинки вместе, оружие вместе и тд (тогда у Оружия тоже должен быть piece)
        pass
    
    ## Возвращает список всех вещей в инвентаре в виде строки
    def __str__(self):
        result = ""
        if len(self.inventory)!=0:
            for item in self.inventory:
                result+="{0} \n".format(item)
        else: #inventory is empty
            result = "empty"
        return result
