from Item import Item
#Хранит вещи игрока

#TODO сделать максимально переносимое число вещей ( зависит от Stamina )
class Inventory:
    inventory = []
    def __int__(self):
        pass
    def addItem(self,newItem):
        self.inventory.append(newItem)
        self.__sort()
    def removeItem(self,item):# if item is in invenrory it will be removed
        if item in self.inventory:
            self.inventory.remove(item)
    def __sort(self):
        #TODO сделать сортировку по типу Ботинки вместе, оружие вместе и тд
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
