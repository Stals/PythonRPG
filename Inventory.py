from Item import Item
#Хранит вещи игрока
class Inventory:
    inventory=[]
    def __int__(self):
        pass
    def addItem(self,newItem):
        self.inventory.append(newItem)
    def removeItem(self,index):# Сюда передаются индекс как он отображается пользователю
        self.inventory.pop(index+1)
    def sort(self):
        #TODO сделать сортировку по типу Ботинки вместе, оружие вместе и тд
        pass


    def __str__(self):
        result=""
        for item in self.inventory:
            #result=result+item.__str__()+"\n"
            result+="{0} \n".format(item)
        return result
