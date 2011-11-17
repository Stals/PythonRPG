#NOTE перед операциями - + , нужно проверять хватает ли денег с помощью > < >= <=
class Money: #TODO сделать Exceptions Если при вычетании и сложении
	"""
	Класс Money позволяет хранить и производить операции над деньгами
	100 бронзы = 1 серебро
	100 серебра = 1 золото
	Серебро и бронза должны быть инициализировано числом от 0 до 99 ,
	а золото любым числом от 0.
	Сложение и вычитание бронзы может менять серебро, а серебра - золото
	"""
	def __init__(self, gold=0, silver=0, bronze=0):
		if gold>=0:
			self.gold = gold
		else:
			raise Exception("Wrong gold value!\nShould be >= 0.")

		if 100 > silver >= 0:
			self.silver = silver
		else:
			raise Exception("Wrong silver value!\nShould be between 0 and 99.")

		if 100 > silver >=0:
			self.bronze = bronze
		else:
			raise Exception("Wrong bronze value!\nShould be between 0 and 99.")

	## returns a copy of gold so that class variable would not be changed
	def getGold(self):
		return self.gold[:]

	## returns a copy of silver so that class variable would not be changed
	def getSilver(self):
		return self.silver[:]

	## returns a copy of bronze so that class variable would not be changed
	def getBronze(self):
		return self.bronze[:]

	## 	Возвращает кол-во денег в виде бронзы
	def toBronze(self):
		return self.gold*100*100 + self.silver*100 + self.bronze

	def __str__(self):
		return "{0} gold {1} silver {2} bronze".format(self.gold, self.silver, self.bronze)

	# >=
	def __ge__(self, other): #TODO mb проверять хватает ли золота перед конвертацией
		# Сравним Кол-во денег в Бронзовом эквиваленте
		if self.toBronze() >= other.toBronze():
			return True
		else:
			return False

	# >
	def __gt__(self, other):
		return not self.__le__(other)

	# <
	def __lt__(self, other):
		return not self.__ge__(other)

	# <=
	def __le__(self, other):
		# Сравним Кол-во денег в Бронзовом эквиваленте
		if self.toBronze() <= other.toBronze():
			return True
		else:
			return False

	# +
	def __add__(self, other):
		self.bronze += other.bronze
		if self.bronze > 100:
			self.bronze -= 100
			self.silver += 1
		self.silver += other.silver
		if self.silver > 100:
			self.silver -= 100
			self.gold += 1
		self.gold += other.gold
		return self

	# +=
	def __iadd__(self, other):
		self.__add__(other)
		return self

	# -
	def __sub__(self, other):
		self.bronze -= other.bronze
		if self.bronze < 0:
			self.bronze += 100
			self.silver -= 1
		self.silver -= other.silver
		if self.silver < 0:
			self.silver += 100
			self.gold -= 1
		self.gold -= other.gold
		return self

	# -=
	def __isub__(self, other):
		self.__sub__(other)
		return self

	# ==
	def __eq__(self, other):
		if self.gold == other.gold and\
			self.silver == other.silver and\
			self.bronze == other.bronze:
			return True
		else:
			return False
	# !=
	def __ne__(self, other):
		return not self.__eq__(other)
