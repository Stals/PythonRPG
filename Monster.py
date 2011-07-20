from Entity import *
class Monster(Entity):
    def __init__(self,name,stats,bonusDamage,bonusDefence,resists,gold=0):
        super().__init__(name,stats,resists,gold)
        self.damage.addDamage(bonusDamage) #TODO Убрать если у монстров будет оружие
        self.defence=bonusDefence#TODO убрать если у монстров будет броня
    def doTurn(self):#used by Battle to make one turn
        pass


#initialization looks like that
#monster = Monster("Dragon",Stats(5,5,5,5),Damage(1,10),5,Elements(0,0,0,0),10)
#                    |              |        |          |            |       |
#                  name           Stats  bonusDamage  bonusDefence resists  gold