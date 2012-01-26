from Hero import *
from Monster import *
from Elements import *
from Potion import *
from Item import *
from Battle import *
from Stats import *
#TODO rewrite all import * (wild card)
#В городе может быть таверна в которой какраз можно бать квесты а заодно сыграть в азартные игры (место чтобы сделать кости(просто занести в отдельный файл чтобы можно было потом юзать) например в папку minigames/dice и тп
# Dice 1
# Если хотябы одна из 2ух костей = 1 то вы выкинули 0 очков, если вы выкинули 2 одинаковые кости - ваши очки умножаются на 2
# Давать выбор Карточные игры, игры с костями, а когда выбрал - предлагать опр.
"""
gameTypes = {"Dice": {
				"normal": "minigames/dice/normal.py",
				"specific": "minigames/dice/specific.py"},
			 "Cards": {
				"Black Jack": "minigames/cards/blackJack.py",
				"Texas Poker": "minigames.cards.poker.texas"} # так? а потом вызов hero.money = selectedGame(hero.money)
}
gameType = getChoice("Choose game type:", list(gameTypes.keys())
selectedGame = getChoice("Choose game:", list(gameTypes[gameType].keys())
exec(open(selectedGame).read()) # Нужно перепистаь так как я хочу передавать кол-во денег у игрока и получать сколько он выйграл или проиграл
"""

#TODO!! Сделать отмени в бою!
#TODO! Добавить canUse методы в другие классы (weapon,armor - может можно просто в ITEM)
#TODO! внутри spell.__str__() выводится имя спелла и Описани того что он делает( зависит от спелла )
#TODO Pet наследуется от Монстра наверно

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


bronzeHead = Armor("Bronze Helmet",Stats(Con=1),1,armorType.Head)
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
# Pet
