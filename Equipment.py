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
    def __str__(self):
        result = ""
        for piece,item in self.equipment.items():
            result+="{0} : {1}\n".format(piece,item)
        return result