#Класс показывает Сопротивления существа к элементам
class Resists:
    def __init__(self,Fire=0,Ice=0,Water=0,Lightning=0):
        self.resists={
            "Fire" : Fire,
            "Ice" : Ice,
            "Water" : Water,
            "Lightning" : Lightning
        }
    def __str__(self):
        result=""
        for key,value in self.stats.items():
            result+="{0}: {1} \n".format(key,value)
        return result
    def fire(self):
        return self.resists["Fire"]
    def ice(self):
        return self.resists["Ice"]
    def water(self):
        return self.resists["Water"]
    def lightning(self):
        return self.resists["Lightning"]


