"""
Recherche la valeur dans la liste avec condition booléen 'vrai' ou 'faux'
"""

liste = [1,2,3,4,5]

entrer = int(input("input: "))

# Condition qu’une certaine valeur 'x' de variable 'entrer' est ou n’est pas dans une collection 'liste'
# liste.index(entrer) pour s'affiche le indice de valuer 'x' de variable 'entre'
if entrer in liste:
    print("La valeur de entrer est exist dans la liste, et son indice est: ", liste.index(entrer))
else:
    print("La valeur de entrer n'est exist pas dans la liste")

#if entrer not in liste:
    #print("Good")
#else:
    #print("not Good")
    
"""
Recherche la valeur dans la liste avec condition booléen 'vrai' ou 'faux' 
entre les indices 0 à 2 de la liste
"""


liste1 = [1,2,3,4,5]

entrer1 = int(input("input: "))

if entrer1 in liste1[0:2]:
    print("La valeur de entrer est exist dans la liste entre les indices 0 à 2, et son indice est: ", liste.index(entrer))
else:
    print("La valeur de entrer n'est exist pas dans la liste entre les indices 0 à 2")
    

""" Recherches dans une structure non triée
    Recherche fastidieuse
"""

liste2 = [1,2,3,4,5]

x = 2

for index_liste2 in range(0,3):
    print(index_liste2)
    if liste2[index_liste2] > x:
        trouve = True
    else:
        trouve = False        
print(trouve)

