from random import *

# Variable avec nombres aléatoires entre 1 et 100

nombreMystere = randint(1,100)

# Variable type int pour compter essais qui commence à 0
nombreEssais = 0

# Variable type int entiers pour saisir numbre 
nombrePropose = int(input("Saisir une nombre entre 1 et 100: "))

# Boucle TANT QUE nombrePropose pas égale à nombreMystere
while nombrePropose != nombreMystere:
    
    # A chaques fois nombreEssais ajoute +1 si nombrePropose pas égale à nombreMystere
    nombreEssais = nombreEssais+1
    
    # Conditions qui vérifie nombrePropose plus grand ou plus petit que nombreMystere
    if nombrePropose < nombreMystere:
        print("Le nombre propose est plus petit")
        
        # Pour arrêter la boucle et saisir nouveau nombre on doit ajoute nombrePropose après print
        nombrePropose = int(input("Saisir une nombre entre 1 et 100: "))
        
    elif nombrePropose > nombreMystere:
        print("Le nombre propose plus grand!")
        nombrePropose = int(input("Saisir une nombre entre 1 et 100: "))         
        
    else:
        nombrePropose == nombreMystere
print("BRAVO !!! Vous avez gagne !!!")
print(nombreEssais, " Coups!")