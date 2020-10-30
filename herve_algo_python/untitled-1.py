def getNumber (getTempNumber):
    while type:
        print ('Saisir un nombre: ', end = '')
        getTempNumber=input ()
        try:
            getTempNumber=int(getTempNumber)
        except ValueError:
            print ('"'+  getTempNumber + '"' + ' - pas de nombre')
        else:
            break
        
def soustraction():
    nb1 = input("Saisir 1er nombre: ")
    nb2 = getNumber(input("Saisir 2er nombre: "))
    print("----------------------------", '\n', "Résultat du calcul est: ", nb1 - nb2, '\n')
    
soustraction()