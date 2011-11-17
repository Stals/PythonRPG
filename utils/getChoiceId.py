#Question Может ли эта функция пригодиться?
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