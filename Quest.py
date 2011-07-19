class Quest:
    def __int__(self):
        pass
    def __str__(self):
        pass

class QuestJournal:
    def __int__(self):
        self.journal = []
    def __str__(self):
        pass
    #Убирает квест из journal (не приносит награды)
    def removeQuest(self,quest):
        pass
    #Даёт награду за выполненный квест и вызывает remove чтобы убрать его
    def finishQuest(self,quest):
        pass