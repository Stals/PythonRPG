from Entity import *
class Monster(Entity):
    def __init__(self,name,stats,bonusDamage,resists,gold):
        super().__init__(name,stats,resists,gold)
        self.damage.addDamage(bonusDamage) #TODO Убрать если у монстров будет оружие

    def doTurn(self):#used by Battle to make one turn
        pass


#initialization looks like that
#monster = Monster("Dragon",stats(5,5,5,5),damage(1,10),Elements(0,0,0,0),10)
#                    |              |              |               |       |
#                  name           stats        bonusDamage      resists  gold