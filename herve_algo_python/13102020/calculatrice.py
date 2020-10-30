def afficher_menu():
    print("     -1 Addition")
    print("     -2 Soustraction")
    print("     -3 Multiplication")
    print("     -4 Division")
    print("     -5 Puissance")
    print("     -6 Modulo")
    print("     -7 Carre")
    print("     -0 Quitter")
    while type:
        choix = input("Choisissez une operation parmi: ")
        try:
            choix =int(choix)
        except ValueError:
            print ('"'+  choix + '"' + ' - pas de nombre')
        else:
            break
        
    return choix

def addition():
    print('\n', "Vous avez choisir Addition",'\n')
    while type: # boucle pour vérifier si input est nombre
        nb1 = input("Saisir 1er nombre: ")
        try:
            nb1 = int(nb1)
        except ValueError:
            print ('"'+  nb1 + '"' + ' - pas de nombre')
        else:  # si le input est numbre alors sortie
            break

    while type: # boucle pour vérifier si input est nombre
        nb2 = input("Saisir 2er nombre: ")
        try:
            nb2 = int(nb2)
        except ValueError:
            print ('"'+  nb2 + '"' + ' - pas de nombre')
        else:  # si le input est numbre alors sortie
            break        
        
    print("----------------------------", '\n', "Résultat du calcul est: ", nb1 + nb2, '\n')
    #return

def soustraction():
    nb1 = int(input("Saisir 1er nombre: "))
    nb2 = int(input("Saisir 2er nombre: "))
    print("----------------------------", '\n', "Résultat du calcul est: ", nb1 - nb2, '\n')
    #return



def multiplication():
    nb1 = int(input("Saisir 1er nombre: "))
    nb2 = int(input("Saisir 2er nombre: "))
    print("----------------------------", '\n', "Résultat du calcul est: ", nb1 * nb2, '\n')
    #return
    

def division():
    nb1 = int(input("Saisir 1er nombre: "))
    nb2 = int(input("Saisir 2er nombre: "))
    if nb2 == 0:
        print("----------------------------", '\n', "Division par 0 zero est impossible", '\n')
    else:
        print("----------------------------", '\n', "Résultat du calcul est: ", nb1 / nb2, '\n')
    #return
    
def puissance():
    nb = int(input("Saisir un nombre: "))
    exposant = int(input("Saisir exposant: "))    
    produit = 1
    for i in range(1,exposant+1): # besion ajouter pour "e" +1
        produit = produit * nb
    print("----------------------------", '\n', "Résultat du calcul est: ", produit, '\n')
    #return produit
    
def modulo():
    nb = int(input("Saisir un nombre: "))
    if nb % 2 == 0:
        print("----------------------------", '\n', "Ce nombre est pair", '\n')
    else:
        print("----------------------------", '\n', "Ce nombre est impair", '\n')
        
def carre():
    nb = int(input("Saisir un nombre: "))
    print("----------------------------", '\n', "Résultat du calcul est: ", nb * nb, '\n')


quitter = 0
while quitter == 0:
    choix_menu = afficher_menu()
    if choix_menu == 0:
        quitter = 1
        
    elif choix_menu == 1:
        addition()
        
    elif choix_menu == 2:
        soustraction()
        
    elif choix_menu == 3:
        multiplication()
        
    elif choix_menu == 4:
        division()
        
    elif choix_menu == 5:
        puissance()
        
    elif choix_menu == 6:
        modulo()
        
    elif choix_menu == 7:
        carre()
    

