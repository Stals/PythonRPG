from Item import Item
#Хранит вещи игрока

#TODO сделать максимально переносимое число вещей ( зависит от Stamina )
#TODO Сделать чтобы при выводе через func использовали player.inventory.items()  // И ДЛЯ ДРУГИХ ТИПО POTIONSPOCKET
class Inventory:
    def __init__(self):
         self.inventory = []

    def addItem(self,newItem):
        self.inventory.append(newItem)
        self.__sort()
    def removeItem(self,item):# if item is in invenrory it will be removed
        if item in self.inventory:
            self.inventory.remove(item)
    def items(self):
        return self.inventory
    def __sort(self):
        #TODO сделать сортировку по типу Ботинки вместе, оружие вместе и тд (тогда у Оружия тоже должен быть piece)
        pass
    def __str__(self):
        result = ""
        if len(self.inventory)!=0:
            for item in self.inventory:
                #result=result+item.__str__()+"\n"
                result+="{0} \n".format(item)
        else: #inventory is empty
            result = "empty"
        return result
