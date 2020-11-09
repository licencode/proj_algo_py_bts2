# http://pise.info/algo/enonces5.htm
# Exercice 5.2

"""
Ecrire un algorithme qui demande un nombre compris entre 10 et 20,
jusqu’à ce que la réponse convienne. En cas de réponse supérieure à 20,
on fera apparaître un message :
« Plus petit ! », et inversement, « Plus grand ! » si le nombre est inférieur à 10.
"""

"""
Corection en psedo-code

Variable N en Entier
Debut
N ← 0
Ecrire "Entrez un nombre entre 10 et 20"
TantQue N < 10 ou N > 20
  Lire N
  Si N < 10 Alors
    Ecrire "Plus grand !"
  SinonSi N > 20 Alors
    Ecrire "Plus petit !"
  FinSi
FinTantQue
Fin
"""

nombre_choix = int(input("Saisez un nombre: "))

while nombre_choix >= 10 or nombre_choix <= 20:
    if nombre_choix <= 10:
        print("Plus")
        nombre_choix = int(input("Saisez un nombre: "))
    elif nombre_choix >= 20:
        print("mois")
        nombre_choix = int(input("Saisez un nombre: "))        
    else:
        print("bon")
    break