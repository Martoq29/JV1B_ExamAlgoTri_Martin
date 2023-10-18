#2/ Lors d’une seule itération, l'algorithme du tri à bulles parcourt le tableau, et compare les
#éléments consécutifs. Lorsque deux éléments consécutifs ne sont pas dans l'ordre, ils sont
#échangés. Par conséquent, à l’issue d’une itération (et donc, d’un parcours entier du
#tableau), le plus grand élément est systématiquement déplacé en fin de tableau ; comme s’il
#s’agissait d’une bulle qui remonte à la surface.
#Écrire un programme permettant le parcours du tableau au cours d’une itération du tri à
#bulles. On pourra se servir de la permutation définie dans l’exercice précédent

myTable=[1,2,5,4]
for i in range(len(myTable)):
    if (myTable[0] > i):
        stock = myTable[2]
        myTable[2] = myTable[3]
        myTable[3] = stock
        print(myTable)