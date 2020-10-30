"""
Controle de flux: instructions itératives conditionnelles.
(séquence) BOUCLE FOR

Imaginez que vous ayez une liste de quatre éléments dont vous voulez afficher les éléments
les   après les autres. Dans l'état actuel de vos connaissances,
il faudrait taper quelque chose de style
"""

"""
Si votre liste ne contient que quatre éléments, ceci est ecore faisable mais imaginez
qu'elle en contienne 100 voire 1000! Pour remédier à cela,
il faut utiliser les boucles. Regardez l'example suivent:
"""

animaux = ['girafe', 'tigre', 'singe', 'souris']

for animal in animaux:
    print(animal , end = '  ') 
    
for animal in animaux[1:3]:
    print(animal)


"""
On a vu que les boucles for pouvaint utiliser une liste contenant des chaînes de caractère,
mais elles peuvent tout aussi bien utiliser des listes numériques.
En utilisant l'instruction range on peut facilement accéder à une liste d'entiers.
"""

for i in range(4):
    print(i)
    


for i in range (4):
    print(animaux[i], end = '  ')
    
#for index, name_animal in enumerate(animaux):
    #print(index, name_animal)
    
#for t in enumerate('hello world'):
    #print(t[0], t[1])