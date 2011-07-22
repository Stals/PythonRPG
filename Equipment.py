#чтобы предложить снять вещь из equipment'а нужео передать items() в getChoice()

## Обмундирование 
class Equipment:
    def __init__(self):

        ## Хранит обмундирование в виде Словаря
         self.equipment={
            "Weapon"   : "empty",
            "Head"     : "empty",
            "Gloves"   : "empty",
            "Chest"    : "empty",
            "Leggings" : "empty",
            "Boots"    : "empty"
        }

    ## Возвращает список всех вещей которые одеты
    def items(self):
        list = []

        for piece,item in self.equipment.items():
            if item!="empty":
                list.append(item)
        return list

    ## Возвращает имя оружия если оно есть, иначе возвращает Fists (кулаки)
    def weapon(self):
        if self.equipment["Weapon"] == "empty":
            return "Fists"
        else:
            return self.equipment["Weapon"].name

    ## Возвращает все одетые вещи в виде строки
    def __str__(self):
        result = ""
        for piece,item in self.equipment.items():
            result+="{0} : {1}\n".format(piece,item)
        return result