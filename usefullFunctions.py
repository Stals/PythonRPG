#Задаёт задаёт question и возвращает выбраннй вариант ответа из данного списка вариантов (choices)
## Использование : result=getChoice("Are You Sure?",["Yes","No","Not Sure"])
## if result=="Yes":
## #doSomthing
# Hint: Как 2ой аргумент можно передавать просто список элементов из который нужно выбрать. Допустим у вас есть список Расс из
# которых можно выбрать , вы передаёте этот список и получаете ответ прямо в Race внутри класса
def getChoice(question , choices):
    if len(choices)>=2:
        print(question)
        for i in range(1,len(choices)+1):
            print("{0}. {1}".format(i,choices[i-1]))
        #TODO DO WHILE в PYHTHON
        while True: #Бесконечный цикл до тех пор пока не будет правильный ввод
            result=input("Your choice is: ")
            if result.isdigit():
                if 1 <= int(result) <= len(choices):
                    return choices[int(result)-1]
                    break
    else:
        return -1



#result = getChoice("are you ok?",["yes","no"])
#сразу запихнуть результат в race внутри класса hero
#self.Race=getChoice("Choose your Race:",["Human","Were-Wolf","Demon","Elf"])
#после чего уже в зависимости от варианта  сделать статы
#if self.Race=="Human"
#    pass
#elif self.Race=="Were-Worf"
