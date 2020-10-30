"""
nom de jeu: "Game good luck calculation"
Version: 0.01

С'est un jeu qui doit générer deux chiffres entre 1 à 100 et faire un calcul.

Pour compter les chiffre il doit utiliser les signes suivent:
addition, soustraction, multiplication, division.

Après le jeu doit proposer pour le jeueur devine le resultat de comptage.
Pour le jeueur il y a dis l'essais pour deviner le resultat avec differents combinaisons.
"""


from random import * # Importer le bibliothéque pour function randint qui générer le nombre aleat

nb1 = randint(1,10) # Variable numbre aleat. Pour premier numbre de jeu.
nb2 = randint(1,10) # Variable numbre aleat. Pour second numbre de jeu.

signe = ["+","-","*","/"] # Les signes pour poser entre les variables "nb1" et "nb2"

import random # le bibliothéque pour function random

random_signe = random.choice(signe) # La variable aleat pour les signes de liste "signe"

print("random item from list is: ", random.choice(random_signe)) # pour verifier la variable "random_signe"

# reponse = int(input("Votre réponse: ")) # La variable pour prendre la réponse de jeueur.


result = nb1, random_signe, nb2 # Test

print(result) # Test

