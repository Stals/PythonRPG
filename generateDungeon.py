import sys
import random
x=100;
y=10;
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

if entranceWall==0 :
    dungeon[0][random.randint(0,x-1)]="E"
elif entranceWall==1 :
    dungeon[random.randint(0,y-1)][x-1]="E"
elif entranceWall==2:
    dungeon[y-1][random.randint(0,x-1)]="E"
elif entranceWall==3:
    dungeon[random.randint(0,y-1)][0]="E"
printDungeon()