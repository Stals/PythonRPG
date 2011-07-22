## Квест на монстра
class Quest:
    def __int__(self):
        pass
    def __str__(self):
        pass
## Журнал квестов - хранить текущие квесты игрока
class QuestJournal:
    def __int__(self):
        self.journal = []
    ## Убирает квест из journal (не приносит награды)
    def removeQuest(self,quest):
        pass
    ## Даёт награду за выполненный квест и вызывает remove чтобы убрать его
    def finishQuest(self,quest):
        pass
    ## Возвращает список всех квестов в журнале
    def items(self):
        return self.journal
    def __str__(self):
        pass