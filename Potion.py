#Potion  восстанавливает percent процентов hp и mana при применении use на target
#percent в дроби, типо 0.33
class Potion:
    def __init__(self,percent=0.33,price=0):
        self.percent = percent
        self.price = price
    def __str__(self):
        return "Potion heals {0}% of HP and MP".format(int(self.percent*100))
        pass
    def use(self,target): #uses potion on a target and removes potion from potionsPocket
        target.hp += self.percent * target.maxHp
        target.mp += self.percent * target.maxMp
        if target.hp > target.maxHp : target.hp = target.maxHp
        if target.mp > target.maxMp : target.mp = target.maxMp
        #removes potion from pocket after it was used
        target.potionsPocket.removePotion(self)

#TODO сделать ограничение в количество которое можно носить с собой
class PotionsPocket:
    pocket = []
    def __init__(self):
        pass

    def __str__(self):
        result = ""
        if len(self.pocket)!=0:
            for potion in self.pocket:
                result+="{0} \n".format(potion)
        else: #pocket is empty
            result = "empty"
        return result

    def addPotion(self,potion):
        self.pocket.append(potion)
        self.__sort()
    def removePotion(self,potion):
        if potion in self.pocket:
            self.pocket.remove(potion)
    #TODO проверить работает ли
    def __sort(self):
        def percent(potion):
            return potion.percent
        self.pocket.sort(key=percent)