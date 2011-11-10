from Entity import *
class Monster(Entity):

    def __init__(self,name,stats,bonusDamage,bonusDefence,resists,gold=0):
        super().__init__(name,stats,resists,gold)
        self.damage.addDamage(bonusDamage) #TODO Убрать если у монстров будет оружие
        self.defence=bonusDefence#TODO убрать если у монстров будет броня

    def getBattleChoice(self): #TODO Сделать более сложной (если будут заклинания, + возможно potions)
        # чтобы в Battle было выбрано simpleAttack
        return "Attack"
    
    #TODO переписать give в get?
    ## Дат опыт hero в зависимоти от статистик monster
    def giveExp(self, hero):
        pass

    ## Даёт Награду hero
    def giveLoot(self,hero):
        hero.gold+=self.gold
        #TODO Давать рандомный шмот ( не каждый раз ) Но при этом может упасть вещь типо Dragon lether и тд

	#NOTE: __str__() опеределен в Entity
	
#initialization looks like that
#monster = Monster("Dragon",Stats(5,5,5,5),Damage(1,10),5,Elements(0,0,0,0),10)
#                    |              |        |          |            |       |
#                  name           Stats  bonusDamage  bonusDefence resists  gold