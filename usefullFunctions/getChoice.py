#TODO Подчистить комментарии

#  Задаёт задаёт question и возвращает выбраннй вариант ответа из данного списка вариантов (choices)
#  Тоесть человек выбирает вариант цифрами но возвращается не цифра введенная пользователем а сам объект (если список строк то строка)
# Hint: Как 2ой аргумент можно передавать просто список элементов из который нужно выбрать. Допустим у вас есть список Race из
# которых можно выбрать , вы передаёте этот список и получаете ответ прямо в переменную Race внутри класса Human

#! Объект внутри списка обязан обладать методом __str__() который выводит описание этого объекта
#! (встроенные типы уже обладают этим методом)[Даже список списков нормально будет выведен]

def getChoice(question , choices):
    if len(choices)>=1:
        print(question)
        for i in range(1,len(choices)+1):
            print("{0}. {1}".format(i,choices[i-1]))# Для вывода элемента из choices вызывается __str__()
        while True: #Бесконечный цикл до тех пор пока не будет правильный ввод
            result=input("Your choice is: ")
            if result.isdigit():
                if 1 <= int(result) <= len(choices):
                    return choices[int(result)-1]
    else:
        return -1



## Пример 1 (Простой вариант):
## result=getChoice("Are You Sure?",["Yes","No","Not Sure"])
## if result=="Yes":
## #doSomthing

## Пример 2 (Встроенные типы):
## result = getChoice("Choose three numbers",[[1,2,3],[4,5,6],[7,8,9]])
## print ("first number is {result[0]}".format(result[0]))

## Пример 3 (Свой класс):
## class item:
##     def __init__(self,name):
##         self.name=name
##     def __str__(self):
##         return self.name
##     def print(self):
##         print(self.__str__())

## itemList=[item("Sword"),item("Bow"),item("Pickaxe")]
## choosedItem=getChoice("Choose your weapon:",itemList) #choosedItem станет ссылкой на объект выбранный пользователем
## print("You choosed a {0}".format(choosedItem.name))
###После чего можно просто сделать
## choosedItem.equip() # если все эти вещи определены в классе




#TODO как сделаю HERO убрать отсюда это
##сразу запихнуть результат в race внутри класса hero
#def getRace():
#self.Race=getChoice("Choose your Race:",["Human","Were-Wolf","Demon","Elf"])
##после чего уже в зависимости от того что лежит в Race сделать статы
#if self.Race=="Human"
#    pass
#elif self.Race=="Were-Worf"
#TODO __str__() в hero делать с переносом на новую строку при выводе каждого объекта. При этом с использованием \n и дальше на новой строке код