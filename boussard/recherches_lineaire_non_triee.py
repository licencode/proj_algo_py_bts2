def recherche_lineaire_non_triee(liste,nombre):
    i = 0
    for i in range(len(liste)):
        if liste[i] == nombre: # Test si oui print et retourn
            print("valeur", nombre, "égal à", liste[i], "avec d'indice de valeur est:", i)
            return i
        else: # Test sinon print 
            print("valeur",nombre, "pas égal à", i)
    return -1


liste_non_triee = [7,4,3,2,8,1,9,6,5]


affiche_liste2 = recherche_lineaire_non_triee(liste_non_triee,3)
