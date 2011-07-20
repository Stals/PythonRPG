from Hero import *
from Monster import *
from Elements import *
from Potion import *

player = Hero()
monster = Monster("Dragon",Stats(7,5,5,5),Damage(0,4),4,Elements(),10)


# TODO Если player.class = "Warrior" сделать
# player = Warrior(player)
#

magicBow=Weapon("Magic Bow",Stats(1,3,0,1),Damage(1,5))
fireSword=Weapon("Fire Sword",Stats(3,0,0,2),Damage(1,5))

bronzeHead=Armour("Bronze Head",Stats(Con=1),1,"Head")
bronzeGloves=Armour("Bronze Gloves",Stats(Con=1),1,"Gloves")
bronzeChest=Armour("Bronze Chest",Stats(Con=1),1,"Chest")
bronzeLeggings=Armour("Bronze Leggings",Stats(Con=1),1,"Leggings")
bronzeBoots=Armour("Bronze Boots",Stats(Con=1),1,"Boots")


player.inventory.addItem(magicBow)
player.inventory.addItem(fireSword)


player.equip(func.getChoice("Choose weapon to equip?",player.inventory.items()))

player.equip(bronzeHead)
player.equip(bronzeGloves)
player.equip(bronzeChest)
player.equip(bronzeLeggings)
player.equip(bronzeBoots)
print(player.equipment)

player.potionsPocket.addPotion(Potion(0.25))
player.potionsPocket.addPotion(Potion(0.33))
print(player.potionsPocket)



print (player)
print (monster)
print
while not player.isDead() and not monster.isDead():
    player.simpleAttack(monster)
    monster.simpleAttack(player)
print (player)
print (monster)





# TODO Что нужно сделать
# Quest / QuestJournal
# SpellBook
# Battle
# BattleChoices
# City
