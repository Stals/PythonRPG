#чтобы предложить снять вещь из equipment'а нужео передать items() в getChoice()
class Equipment:
    def __init__(self):
         self.equipment={
            "Weapon"   : "empty",
            "Head"     : "empty",
            "Gloves"   : "empty",
            "Chest"    : "empty",
            "Leggings" : "empty",
            "Boots"    : "empty"
        }
    def items(self):#returns list of all items that are equiped
        list = []

        for piece,item in self.equipment.items():
            if item!="empty":
                list.append(item)
        return list

    def __str__(self):
        result = ""
        for piece,item in self.equipment.items():
            result+="{0} : {1}\n".format(piece,item)
        return result