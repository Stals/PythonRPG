# Задаёт question и возвращает выбранный вариант ответа из данного списка вариантов (choices)
# Тоесть человек выбирает вариант цифрами но возвращается не цифра введенная пользователем а сам объект (если список строк то строка например)

#! Объект внутри списка обязан обладать методом __str__() который выводит описание этого объекта
#!(встроенные типы уже обладают этим методом)[Даже список списков нормально будет выведен]

# Если передать cancel = True или просто True , то будет также предложен вариант отмены
# Если был выбран вариант - возвращается ссылка на него
# Если была выбрана Отмена (Cancel) будет возвращен 0
# В случае ошибки будет возвращен -1

#TODO! защиту от русских букв
def getChoice(question , choices , cancel = False):
	if len(choices)>=1:
		print(question)
		if cancel == True:
				print ("0. Cancel")
		for i in range(1, len(choices) + 1):
			print("{0}. {1}".format(i, choices[i - 1]))# Для вывода элемента из choices вызывается __str__()

		# Бесконечный цикл до тех пор пока не будет правильный ввод
		while True:
			result = input("Your choice is: ")
			if result.isdigit():
				if not cancel:
					# Если вариант отмены не предусмотрен
					if 1 <= int(result) <= len(choices):
						return choices[ int(result) - 1 ]

				elif cancel:
					# Если возможен вариант отмены разрешаем вариант ввода нуля
					if 0 <= int(result) <= len(choices):
						if int(result) == 0 :
							return 0
						else:
							return choices[ int(result) - 1 ]
	else:
		raise Exception("There should be 1 or more choices!")



## Пример 1 (Простой вариант):
## result=getChoice("Are You Sure?",["Yes","No","Not Sure"])
## if result=="Yes":
## #doSomthing

## Пример 2 (Использование Отмены)
## result = getChoice("Do you want to Exit?",["Yes","No"],cancel = True)
## if result == 0 :
##     #Обработка Cancel
## elif result == "Yes":
##     #Обработка Yes
## else:
##     #Обработка No

## Пример 3 (Встроенные типы):
## result = getChoice("Choose three numbers",[[1,2,3],[4,5,6],[7,8,9]])
## print ("first number is {result[0]}".format(result[0]))

## Пример 4 (Свой класс):
## class item:
##     def __init__(self,name):
##         self.name=name
##     def __str__(self):
##         return self.name
##     def equip(self):
##         pass

## itemList=[item("Sword"),item("Bow"),item("Pickaxe")]
## choosedItem=getChoice("Choose your weapon:",itemList) #choosedItem станет ссылкой на объект выбранный пользователем
## print("You choosed a {0}".format(choosedItem.name))
###После чего можно просто сделать
## choosedItem.equip()

#TODO перемсотреть необходимость
# returns 0 for the first element and so on
def getChoiceId(question , choices):
	if len(choices)>=1:
		print(question)
		for i in range(1,len(choices)+1):
			print("{0}. {1}".format(i,choices[i-1]))# Для вывода элемента из choices вызывается __str__()
		while True: #Бесконечный цикл до тех пор пока не будет правильный ввод
			result=input("Your choice is: ")
			if result.isdigit():
				if 1 <= int(result) <= len(choices):
					return int(result)-1
	else:
		return -1
