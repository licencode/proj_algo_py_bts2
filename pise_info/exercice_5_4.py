# http://pise.info/algo/enonces5.htm
# Exercice 5.4

"""
Réécrire l'algorithme précédent,
en utilisant cette fois l'instruction Pour
""" 

"""
Corection en psedo-code

Variables N, i en Entier
Debut
Ecrire "Entrez un nombre : "
Lire N
Ecrire "Les 10 nombres suivants sont : "
Pour i ← 1 à 10
  Ecrire N + i
i Suivant
Fin
"""

###ma décision en Python avec boucle for et range

nombre_choix = int(input("Saisissez un nombre: "))

for i in range(0,10):
    nombre_choix = nombre_choix + 1
    print(nombre_choix)