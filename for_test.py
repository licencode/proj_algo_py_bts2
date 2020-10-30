demande = int(input("Entrez les chifres entre 1 et 3: "))


while demande <= 1 or demande >= 3:
    if demande <= 1 or demande >= 3:
        print("good")
        break
    else:
        print("non good")
        break