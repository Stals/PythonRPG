import sys
import random
#TODO так как рандом в питоне такойже как в с++ по умолчанию то не возможно быстро сгенерировать несколько разных чисел
#Соответственно нужно найти способ это обойти, так как мне бы хотелось достаточно быстро генерировать полностью случайное подземелье
#http://stackoverflow.com/questions/817705/pythons-random-what-happens-if-i-dont-use-seedsomevalue



#размер Подземелья
#TODO Для отдельной версии нужно сделать так чтобы можно было задать размер из консоли
x=100
y=10
#Координаты входа в подземелье
entranceLocationX=0
entranceLocationY=0

#создаём подземелье 100 на 10 (x=100,y=10)
dungeon=[["*"]*x for i in range(y)]#сделано так а не [["*"]*100]*10 чтобы они не ссылись на одни и теже элементы.
# потому что без этого если бы я сделал dungeon[0][0]=" " , то во всех строках первый элемент стал бы пробелос.

def printDungeon():
    #Для каждого списка в списке выводится каждый элемент, а когода список кончается делается перевод строки и выводится следущий список
    for i in dungeon:
        for j in i:
            sys.stdout.write(j)#такой вывод используется для того чтобы после вывода одного символа сразу не ставился перево строки
        sys.stdout.write("\n")



#определим на какой из сторон будет вход
entranceWall=random.randint(0,3)
#Где 0 - Север 1 - Восток 2 - Юг 3 - Запад
#Нарисуем E - Entrance на случайном месте той стророны что выбрали
if entranceWall == 0 :
    entranceLocationX=0
    entranceLocationY=random.randint(0,x-1)
elif entranceWall == 1 :
    entranceLocationX=random.randint(0,y-1)
    entranceLocationY=x-1
elif entranceWall == 2:
    entranceLocationX=y-1
    entranceLocationY=random.randint(0,x-1)
elif entranceWall == 3:
    entranceLocationX=random.randint(0,y-1)
    entranceLocationY=0
dungeon[entranceLocationX][entranceLocationY]="E"

#С этого места мы уже начнём создавать подземелье

printDungeon()