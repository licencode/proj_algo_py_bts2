# http://pise.info/algo/enonces5.htm
# Exercice 5.5

"""
Ecrire un algorithme qui demande un nombre de départ,
et qui ensuite écrit la table de multiplication de ce nombre,
présentée comme suit (cas où l'utilisateur entre le nombre 7) :

Table de 7 :
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
…
7 x 10 = 70
"""

"""
Corection en psedo-code

Variables N, i en Entier
Debut
Ecrire "Entrez un nombre : "
Lire N
Ecrire "La table de multiplication de ce nombre est : "
Pour i ← 1 à 10
  Ecrire N, " x ", i, " = ", n*i
i Suivant
Fin
"""

###ma décision en Python avec boucle for et range code pas cloner de corection

nombre_choix = int(input("Saisissez un nombre: "))

for i in range (1,11):
    result = nombre_choix * i
    print(nombre_choix, 'x', i, '=', result)
