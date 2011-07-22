##Potion  восстанавливает percent процентов hp и mana при применении use на target
class Potion:

    ## percent в дроби, типо 0.33
    def __init__(self,percent=0.33,price=0):
        self.percent = percent
        self.price = price

    ## uses potion on a target and removes potion from potionsPocket
    def use(self,target):
        beforeHp=target.hp
        beforeMp=target.mp

        target.hp += round(self.percent * target.maxHp)
        target.mp += round(self.percent * target.maxMp)
        if target.hp > target.maxHp : target.hp = target.maxHp
        if target.mp > target.maxMp : target.mp = target.maxMp
        #removes potion from pocket after it was used
        target.potionsPocket.removePotion(self)

        afterHp=target.hp
        afterMp=target.mp

        print ('Potion healed "{0}" for {1} health and {2} mana'.format(target.name,(afterHp-beforeHp),(afterMp-beforeMp)))

    ## Возвращает описание potion
    def __str__(self):
        return "Potion heals {0}% of HP and MP".format(int(self.percent*100))

## Карман с Лечебками
class PotionsPocket:#TODO сделать ограничение в количество которое можно носить с собой


    def __init__(self):
        self.pocket = []

    ## Добавлет potion в карман
    def addPotion(self,potion):
        self.pocket.append(potion)
        self.__sort()

    ## Уберает potion из кармана
    def removePotion(self,potion):
        if potion in self.pocket:
            self.pocket.remove(potion)

    ## Возвращает список всех лечебок в кармане
    def items(self):
        return self.pocket

    ## Возвращает True если карман пуст
    def isEmpty(self):
        return not len(self.pocket)
    ## Сортирует лечебки в кармане по проценту который они восстанавливают
    def __sort(self):
        def percent(potion):
            return potion.percent
        self.pocket.sort(key=percent)
    ## Возвращает список всех лечебок в виде строки
    def __str__(self):
        result = ""
        if len(self.pocket)!=0:
            for potion in self.pocket:
                result+="{0} \n".format(potion)
        else: #pocket is empty
            result = "empty"
        return result

