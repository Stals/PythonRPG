#Допустим есть список Монстров, вы кидаете его в это функцию и получаете список всех монстров
def printList(list):
    if len(list)>=1:
        for i in range(1,len(list)+1):
            print("{0}. {1}".format(i,list[i-1]))


monsters=["Dragon","Mighty Wizard","Black Knight"]
printList(monsters)