## Класс хранит элементы и их значения
# класс может быть использован в качесте Сопротивления этим элементам 
# или наоборот дополнительному урону этими элементами
class Elements:
    def __init__(self,Fire=0,Ice=0,Water=0,Lightning=0):
        self.resists={
            "Fire" : Fire,
            "Ice" : Ice,
            "Water" : Water,
            "Lightning" : Lightning
        }
		
    ## Возвращает показатель Элемента Огня
    def fire(self):
        return self.resists["Fire"]

    ## Возвращает показатель Элемента Льдя
    def ice(self):
        return self.resists["Ice"]

    ## Возвращает показатель Элемента Воды
    def water(self):
        return self.resists["Water"]

    ## Возвращает показатель Элемента Молнии
    def lightning(self):
        return self.resists["Lightning"]

    ## Возвращает список всех элементов в виде строки
    def __str__(self):
        result = ""
        for key,value in self.resists.items():
            result+="{0}: {1} \n".format(key,value)
        return result

