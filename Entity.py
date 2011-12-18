from Damage import *
from Stats import *

class Entity:

	def __init__(self,name,stats,resists,money):
		self.name = name
		self.defence = 0 # 2 defence защищают от 1 урона
		self.stats = Stats()
		self.stats.addStats(stats)
		self.resists = resists
		self.money = money

	## Перелпределяется в наслдениках
	## Метод отвечает за ход в бою
	def doTurn(self, hero, enemies):
		pass

	## Обычная атака оружием
	def simpleAttack(self,target):#simple attack with a weapon // returns true if this killed an enemy
		#Разность в Agi влияет на попадание
		hitChance = self.stats.agi() / target.stats.agi()
		if hitChance > 1 or random.random() < hitChance: #Если у вас agi больше или random попал в шанс попадания
			dmg = self.stats.damage.getDamage() - round(target.defence / 2)
			if dmg < 0:
				dmg = 0
			target.stats.hp -= dmg
			if target.isDead():
				print('"{0}" kills "{1}" with {2} damage.'.format(self.name,target.name,dmg))
				return True
			else:
				print('"{0}" hits "{1}" for {2} damage. ({3}/{4} hp left)'.format(self.name,target.name,dmg,target.stats.hp,target.stats.maxHp))
				return False
		else: #you missed
			print('"{0}" missed "{1}" with {2}% hit chance.'.format(self.name, target.name, round(hitChance*100)))

	## Возвращает true если Entity мертв
	def isDead(self):
		return self.stats.hp<=0

	## Возвращает описание Entity в виде строки
	def __str__(self):
		#return '"{0}" Health: {1}/{2} Mana: {3}/{4} {5} Defence: {6}'.format(self.name,self.hp,self.maxHp,self.mp,self.maxMp,self.stats.damage,self.defence)
		return '"{0}" Health: {1.hp}/{1.maxHp} Mana: {1.mp}/{1.maxMp} {1.damage} Defence: {2}'.format(self.name, self.stats, self.defence)
