from Entity import *
from Money import *
class Monster(Entity):

    def __init__(self,name,stats,bonusDamage,bonusDefence,resists,money=Money()):#TODO пропрвать GOLD на MONEY
        super().__init__(name,stats,resists,money)
        self.damage.addDamage(bonusDamage) #TODO Убрать если у монстров будет оружие
        self.defence = bonusDefence #TODO убрать если у монстров будет броня

    def getBattleChoice(self): #TODO Сделать более сложной (если будут заклинания(можно сделать Класс MageMonster у которого будет список заклинаний при инициализации и он сможет их использовать (даже heal)), + возможно potions)
        # чтобы в Battle было выбрано simpleAttack
        return "Attack"
    
    #TODO переписать give в get?
    ## Дать опыт hero в зависимоти от статистик monster
    def giveExp(self, hero):
        pass

    ## Даёт Награду hero
    def giveLoot(self, hero):
        hero.money += self.money #TODO изменить на money т.к. сломается
        #TODO Давать рандомный шмот ( не каждый раз ) Но при этом может упасть вещь типо Dragon lether и тд

	#NOTE: __str__() опеределен в Entity
	
#initialization looks like that
#monster = Monster("Dragon",Stats(5,5,5,5),Damage(1,10),5,Elements(0,0,0,0),10)
#                    |              |        |          |            |       |
#                  name           Stats  bonusDamage  bonusDefence resists  gold