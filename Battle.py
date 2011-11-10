from usefullFunctions import getChoice as func
#todo сделать битву против нескольких противников, например наследуется от battle или battle принемает как противника только лист

## Отвечает за бой между героем и монстрами
class Battle: #TODO Сделать чтобы при выборе вещи/противника/заклинания можно было нажать отмена и выбирать действие снова

    ## Принемает монстра или список монстров( или одного монстра ) как противника
    def __init__(self,hero,enemies):
        enemyList = []
        enemyList.extend (enemies) # После этого даже если был всего 1 моб, всё будет работать
        if len(enemyList) >= 1:
            
            #print stats of hero and all enemies
            print ("Battle begins between\n{0}\nand".format(hero))
            for enemy in enemyList:
                print(enemy)

            victory = False
            deadEnemies = []
            while True:
                print ()
            # ХОД ИГРОКА
                print (hero) # чтобы игрок мог видеть свои hp
            #Так как getBattleChoice возвращает только те варианты которые осуществимы - например есть хоты один potion
                choice = hero.getBattleChoice()

                if choice[0] == 'A': #Attack #TODO заменить на функцию так как тоже самое вызывается и для enemy (тогда перенести проверку на убийство моба дальше)
                    if len(enemyList) > 1:
                        choosedEnemy = func.getChoice("Choose your target:",enemyList)
                    else: # Если один противник - его бьёт автоматически
                        choosedEnemy = enemyList[0]
                    hero.simpleAttack(choosedEnemy)
                    #проверка на то не умер ли моб , если умер - то его запихиваем в deadEmenies чтобы потом получить с них нагруду (Loot) если игрок выйграет
                    #TODO перенести дальше так как spell тоже может убить
                    if choosedEnemy.isDead():
                        enemyList.remove(choosedEnemy)
                        deadEnemies.append(choosedEnemy)

                if choice[0] == 'U': #Use Potion
                    choosedPotion = func.getChoice("What potion to use?", hero.potionsPocket.items(), cancel = True)
                    if choosedPotion == 0:
						#Выбрали Отмену
                        continue
                    else:
                        hero.use(choosedPotion)
                    
                #проверка на выйгрыш игрока
                if len(enemyList)==0:
                    victory = True
                    break

                # ХОД ПРОТИВНИКОВ
                for enemy in enemyList:
                    choice = enemy.getBattleChoice()
                    if choice[0] == 'A': #Attack
                        enemy.simpleAttack(hero)

                #проверка на выйгрыш мобов
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