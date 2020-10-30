#O(log(n))

def recherche_binaire (liste, valeur):
    debut_de_gamme = 0
    fin_de_gamme = len(liste) -1
    
    while debut_de_gamme <= fin_de_gamme:
        centre_de_gamme = (debut_de_gamme + fin_de_gamme) // 2
        
        if liste[centre_de_gamme] == valeur:
            return centre_de_gamme
        
        elif liste[centre_de_gamme] > valeur:
            fin_de_gamme = centre_de_gamme -1
            
        elif liste[centre_de_gamme] < valeur:
            debut_de_gamme = centre_de_gamme +1
        

    return -1


liste_non_triee = [7,4,3,2,8,1,9,6,5]


affiche_liste2 = recherche_binaire(liste_non_triee,6)
print(liste_non_triee)
print(affiche_liste2)