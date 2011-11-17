from utils import getChoice as utils
## Отвечает за бой между героем и монстрами
class Battle:
#TODO вынести ход игрока и ход монстра в  отдельные методы
#TODO вынести функцию выбора хода в отдельную функцию
    ## Принемает монстра или список монстров( или одного монстра ) как противника
    def __init__(self,hero,enemies):
        enemyList = []
        enemyList.extend (enemies) # После этого даже если был всего 1 моб, всё будет работать
        if len(enemyList) >= 1:
            
            #print stats for hero and all enemies
            print ("Battle begins between\n{0}\nand".format(hero))
            for enemy in enemyList:
                print(enemy)

            victory = False
            deadEnemies = []
            while True:
                print ()
            # ХОД ИГРОКА
                print (hero) # чтобы игрок мог видеть свои hp
            	# getBattleChoice возвращает только те варианты которые осуществимы - например есть хотыбы один potion
                choice = hero.getBattleChoice()

				#TODO! переписать используя это : http://stackoverflow.com/questions/8141165/how-to-dynamically-select-a-method-call-in-python
                if choice[0] == 'A': #Attack #TODO заменить на функцию так как тоже самое вызывается и для enemy (тогда перенести проверку на убийство моба дальше)
                    if len(enemyList) > 1:
                        choosedEnemy = utils.getChoice("Choose your target:", enemyList, cancel = True)
                        if choosedEnemy == 0:
                            # Если была выбрана отмена
                            continue
                    else: # Если один противник - его бьёт автоматически
                        choosedEnemy = enemyList[0]
                    hero.simpleAttack(choosedEnemy)
                    # проверка на то не умер ли моб , если умер - то его запихиваем в deadEmenies чтобы потом получить с них нагруду (Loot) если игрок выйграет
                    #TODO перенести дальше так как spell тоже может убить
                    if choosedEnemy.isDead():
                        enemyList.remove(choosedEnemy)
                        deadEnemies.append(choosedEnemy)

                if choice[0] == 'U': #Use Potion
                    choosedPotion = utils.getChoice("What potion to use?", hero.potionsPocket.items(), cancel = True)
                    if not choosedPotion:
						# Выбрали Отмену
                        continue
                    else:
                        hero.use(choosedPotion)
                    
                # проверка на выйгрыш игрока
                if len(enemyList) == 0:
                    victory = True
                    break

                # ХОД ПРОТИВНИКОВ
                for enemy in enemyList:
                    choice = enemy.getBattleChoice()
                    if choice[0] == 'A': #Attack
                        enemy.simpleAttack(hero)

                # проверка на выйгрыш мобов
                if hero.isDead():
                    victory = False
                    break

            if victory == True:
                #TODO Дать лут и бабло
                for enemy in deadEnemies:
                    enemy.giveLoot(hero)
                print ("You win!")
                #return True
            else:
                print ("You loose!")
                #return False

 
 #   def getOrder(self,hero,enemyList): #TODO Определить последовательность хода в зависимости от Dex
 #      Потом в основной функции цели предлагается ударить того кого нету... ой ну хз
 #      pass