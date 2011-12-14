from Hero import *
from Monster import *
from Elements import *
from Potion import *
from Item import *
from Battle import *
from Stats import *

player = Hero()
dragonMonster = Monster("Dragon",Stats(9,10,4,4,6,1),Damage(2,6),4,Elements(),10)
puppyMonster = Monster("Puppy",Stats(1,2,1,2,1,1),Damage(1,1),1,Elements(),5)

# TODO Если player.class = "Warrior" сделать
# player = Warrior(player)
#

magicBow = Weapon("Magic Bow",Stats(Agi=3,Dex=2),Damage(1,5))
fireSword = Weapon("Fire Sword",Stats(Str=3,Con=2),Damage(1,5))

player.inventory.addItem(magicBow)
player.inventory.addItem(fireSword)

player.equip(utils.getChoice("Choose weapon to equip:", player.inventory.items()))


bronzeHead = Armor("Bronze Head",Stats(Con=1),1,armorType.Head)
bronzeGloves = Armor("Bronze Gloves",Stats(Con=1),1,armorType.Gloves)
bronzeChest = Armor("Bronze Chest",Stats(Con=1),1,armorType.Chest)
bronzeLeggings = Armor("Bronze Leggings",Stats(Con=1),1,armorType.Leggings)
bronzeBoots = Armor("Bronze Boots",Stats(Con=1),1,armorType.Boots)

player.equip(bronzeHead)
player.equip(bronzeGloves)
player.equip(bronzeChest)
player.equip(bronzeLeggings)
player.equip(bronzeBoots)
print(player.equipment)

player.potionsPocket.addPotion(Potion(0.25))
player.potionsPocket.addPotion(Potion(0.33))
#print(player.potionsPocket)

Battle(player,[dragonMonster,puppyMonster])


# TODO Что нужно сделать
# Quest / QuestJournal
# SpellBook
# City
