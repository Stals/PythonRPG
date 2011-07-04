import random
import os
#Вообще може было всё запизнуть в один класс entity и уже переменные назвать human и monnster , но я сделал так потому
#что думаю что У человека возможно будет больше чего (например опыт и уровни и тД)

#Из за моей лени тут вообще нету проверок на вводы (ника и монстра)
class Entity:
    def __init__(self,name,hp,dmg):
        self.name=name
        self.hp=hp
        self.dmg=dmg

    def attack(self,monster):
        randDmg=random.randint(self.dmg[0],self.dmg[1])
        monster.hp-=randDmg
        print("{0} attacks for {1} dmg".format(self.name,randDmg))
        print("{0} now have {1} hp".format(monster.name,str(monster.hp)))



class monster(Entity):
    pass

class human(Entity):
    pass

#создаём список всех монстров
monsters=[monster("Dragon",50,(10,20)),
          monster("Black Knight",30,(20,30)),
          monster("Mighty Wizard",20,(40,40)),
          monster("Zaraki Kempachi",70,(50,100)),
          monster("Phenix",100,(1,200))
]
#Получаем имя Игрока
#TODO Если вводить русские буквы то ломается
player=human(input("Введите ваше имя: "),100,(7,15))


print("{0} выходит на арену и его просят выбрать себе противника".format(player.name))

#выводим всех монстров для выбора
i=0
while i<len(monsters):
   print("{0}. {1}".format(i,monsters[i].name))
   i+=1

#выбираем монстра которого выбрал Игрок
#TODO Если тут дадут не число то всё сломается
choosedMonster=monsters[int(input("Ваш выбор: "))]
print("Замечательно, вашим противником будет {0}. Да начнётся бой!".format(choosedMonster.name))

#делам цикл до тех пор пока ктонибудь не умрёт
while player.hp>=0 and choosedMonster.hp>=0:
    player.attack(choosedMonster)
    choosedMonster.attack(player)

#Сообщаем о выйгрыше/Проигрыше/Ничье
if player.hp<=0 and choosedMonster.hp<=0:
    print("DRAW!")
elif player.hp>0:
    print("{0} WINS!".format(player.name))
else:
    print("{0} LOOSE!".format(player.name))

os.system("pause")