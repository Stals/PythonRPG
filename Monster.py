from Entity import *
from Money import *
class Monster(Entity): #TODOlater если будут заклинания сделать добавление через monster.spellBook.addSpell() наверно [и при создании монстра ему накидывать заклинаний]

	def __init__(self,name,stats,bonusDamage,bonusDefence,resists,money=Money()):
		super().__init__(name,stats,resists,money)
		self.stats.damage.addDamage(bonusDamage) #TODOlater Убрать если у монстров будет оружие
		self.defence = bonusDefence #TODOlater убрать если у монстров будет броня

	#TODOlater Сделать более сложной (если будут заклинания(можно сделать Класс MageMonster у которого будет список заклинаний при инициализации и он сможет их использовать (даже heal)), + возможно potions) [сделать возможные варианты также как и у героя через getAvailableChoices а потом из них уже выбирать]
	def doTurn(self, hero, enemies):
		self.simpleAttack(hero)

	## Дать опыт hero в зависимоти от статистик monster
	def giveExp(self, hero):
		pass

	## Даёт Награду hero
	def giveLoot(self, hero):
		hero.money += self.money
		#TODO Давать рандомный шмот ( не каждый раз ) Но при этом может упасть вещь типо Dragon lether и тд

#NOTE: __str__() опеределен в Entity

#initialization looks like that
#monster = Monster("Dragon",Stats(5,5,5,5),Damage(1,10),5,Elements(0,0,0,0),10)
#                    |              |        |          |            |       |
#                  name           Stats  bonusDamage  bonusDefence resists  money