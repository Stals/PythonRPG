from Hero import *
from Monster import *
from Elements import *
from Potion import *
from Item import *
from Battle import *
player = Hero()
monster = Monster("Dragon",Stats(9,5,5,10),Damage(2,6),4,Elements(),10)
monster2= Monster("Puppy ",Stats(1,1,1,2),Damage(1,1),1,Elements(),5)

# TODO Если player.class = "Warrior" сделать
# player = Warrior(player)
#

magicBow=Weapon("Magic Bow",Stats(1,3,0,1),Damage(1,5))
fireSword=Weapon("Fire Sword",Stats(3,0,0,2),Damage(1,5))

bronzeHead=Armour("Bronze Head",Stats(Con=1),1,armourType.Head)
bronzeGloves=Armour("Bronze Gloves",Stats(Con=1),1,armourType.Gloves)
bronzeChest=Armour("Bronze Chest",Stats(Con=1),1,armourType.Chest)
bronzeLeggings=Armour("Bronze Leggings",Stats(Con=1),1,armourType.Leggings)
bronzeBoots=Armour("Bronze Boots",Stats(Con=1),1,armourType.Boots)


player.inventory.addItem(magicBow)
player.inventory.addItem(fireSword)


player.equip(func.getChoice("Choose weapon to equip?",player.inventory.items()))

player.equip(bronzeHead)
player.equip(bronzeGloves)
player.equip(bronzeChest)
player.equip(bronzeLeggings)
player.equip(bronzeBoots)
#print(player.equipment)

player.potionsPocket.addPotion(Potion(0.25))
player.potionsPocket.addPotion(Potion(0.33))
#print(player.potionsPocket)

Battle(player,monster)


# TODO Что нужно сделать
# Quest / QuestJournal
# SpellBook
# City
