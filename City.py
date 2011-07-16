import random

citiesName = [
    "Goldbrick",
    "Mordor",
    "Dark Woods",
    "Mapletown",
    "Milfort"
]

class City:
    def __init__(self,player):
        self.name = random.choice(citiesName)
