#TODO! Переименовать имя файла и функий!
#TODO! Переписать Описание функций

#TODO!!! Везьде где я хочу чтобы форматировалось ставить 2 пробела, и просто делать split по двум пробелам

# Возвращает Список отформатированных строк из двуменроного списка.
# Если split = True тогда строки внутри списка будут разбиты на элементы списка там где есть 2 пробела

# Пример
# Входные данные
# 	[['1', '2', '3'],
#	 ['11', '22', '33']]
# Выходные
#	[['1  2  3'],
# 	[11 22 33']]
def joinListWithFormat(list, split = False):
	#Code from: http://stackoverflow.com/questions/7136432/data-table-in-python
	if len(list) >=1 :
		if split:
			list = splitListBy2Spaces(list)
		newList = []
		sub1 = [
			[s.ljust(max(len(i) for i in grp)) for s in grp]
			for grp in zip(*list)]
		for p in [" ".join(row) for row in zip(*sub1)]: newList.append(p)
		return newList
	else:
		raise Exception("List length < 1")

# Разделяет строки внутри двумерного массива на элементы списка там где есть 2 пробела
# Пример 
# Вход : [['1  2'],['2', '3 2']]
# Выход: [['1','2'],['2','3 2']]'
#BUG: Не работает если передавать туда не список списков а просто список строк
def splitListBy2Spaces(list):
	if len(list) >=1 :
		newList = []
		newLine = []
		for line in list:
			#line also should be a list
			for str in line:
				newLine.extend(str.split('  '))
			newList.append(newLine)
			newLine = []
		return newList
	else:
			raise Exception("List length < 1")
