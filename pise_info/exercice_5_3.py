# http://pise.info/algo/enonces5.htm
# Exercice 5.3

"""
Ecrire un algorithme qui demande un nombre de départ,
et qui ensuite affiche les dix nombres suivants.
Par exemple, si l'utilisateur entre le nombre 17,
le programme affichera les nombres de 18 à 27.
""" 

"""
Corection en psedo-code

Variables N, i en Entier
Debut
Ecrire "Entrez un nombre : "
Lire N
Stop ← N+10
Ecrire "Les 10 nombres suivants sont : "
TantQue N < Stop
   N ← N+1
   Ecrire N
FinTantQue
Fin
"""

### Code cloner de corection en Python avec boucle while

n = int(input("Saisissez un nombre: "))
stop = n + 10

while n < stop:
    n = n + 1
    print(n)

###ma décision en Python avec boucle for et range

nombre_choix = int(input("Saisissez un nombre: "))

for i in range(0,10):
    nombre_choix = nombre_choix + 1
    print(nombre_choix)

