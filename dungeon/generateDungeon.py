import os

os.system(r"dungeonGenerator.exe > map.txt")

f = open('map.txt','r')
numberOfMonsters=f.readline()
entranceX=f.readline()
entranceY=f.readline()
map=f.readlines()

f.close()
os.remove("map.txt")
