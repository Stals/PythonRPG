from Entity import *
class Monster(Entity):
    def __init__(self,name,stats,bonusDamage,resists,gold):
        super().__init__()
        self.name=name
        self.stats=stats

        #TODO ПЕРЕНЕСТИ В ENTITY ТАК КАК У МОБА ТОЖЕСАМОЕ может сделать player=Hero(Hero.getName,и ТД) Или просто в main определить эти функции с рассой и тд?
        self.maxHp=self.hp=self.stats.con()*10
        self.maxMp=self.mp=self.stats.mag()*10
        #TODO ПЕРЕПИСАТЬ какнить....
        self.damage.min=self.stats.str()
        self.damage.max=self.stats.str()

        self.damage.addDamage(bonusDamage)
        self.resists=resists
        self.gold=gold

    def doTurn(self):#used by Battle to make one turn
        pass


#initialization looks like that
#monster = Monster("Dragon",stats(5,5,5,5),damage(1,10),Elements(0,0,0,0),10)
#                    |        |               |             |              |
#                  name     stats          bonusDamage  resists          gold