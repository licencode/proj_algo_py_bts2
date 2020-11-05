"""

liste = ["vache", "souris", "levure", "bacterie"]

print (liste, "\n")

for i in liste:
    print(i)


"""
# Exercice 5
print("-------------------Exercice 5-----------------")
note_etud = [14, 9, 6, 8, 12]

note = 0

notes = len(note_etud)

for i in note_etud:
    note = note + i
print("Note moyenne", note / notes)


# Exercice 6
print("-------------------Exercice 6-----------------")

"""
soit la liste X contenant les nombres entiers de 0 à 10.
Calculez le produit des nombres consécutifs deux à deux de X en utilisant une boucle.
"""
liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#liste = [25,25,25]

liste_len = len(liste)

p = 0
produit = 0

while p < len(liste):
    produit = produit + liste[p]
    print(produit)
    p = p + 2



##for i in liste:
##    if p < liste_len:
##        produit = produit + liste[p]
##        print(produit)
##        p = p + 2



