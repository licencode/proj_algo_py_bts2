"""
Un autre avantage des listes est la possibilité de sélectionner une partie en utilisant
un indiçage construit sur le modèle [m:n+1] pour récuperer tous les éléments, du émième au
énième ( de l'élément m inclus à l'élément n+1 exlus).
On dit alors qu'on récupère une tranche de la liste, par exemple:
"""

animaux = ['girafe', 'tigre', 'singe', 'souris']

# affiche liste animaux entre 0 et 2
print(animaux [0:2])

# affiche liste animaux entre 0 et 3
print(animaux [0:3])

# affiche liste animaux entre 0 et tout
print(animaux [0:])

# affiche liste animaux entre tout et tout
print(animaux [:])

# affiche liste animaux entre 1 et tout
print(animaux [1:])

# signe moins signefique que la liste commence à la fin
print(animaux [1:-1])


numbres = [1,2,3,4,5]

# signe moins signefique que la liste commence à la fin
print(numbres[-2])

"""
Remarquez que lorsqu'aucun indice n'est indiqué à gauche ou à droite du symbole:
Python prend par défaut tous les éléments depuis le début ou tous les éléments jusqu'à la fin respectivement.
"""

enclos1 = ['girafe', 4]
enclos2 = ['tigre', 2]
enclos3 = ['singe', 5]

# liste dans liste. Magnifique !
zoo = [enclos1[0], enclos2, enclos3]

mammiferes = [zoo[1], animaux]
zoo_enfini = [mammiferes]
print(zoo)
print(mammiferes)
print(zoo_enfini)

"""
Dans cet exemple, chaque sous-liste contient une catégorie d'animal et le nombre d'animaux
pour chaque catégorie. Pour accéder à un élément de la sous-liste, un utilise un double indiçage.
"""

pieces_marque = []

pieces_auto = ['plaquette de frein', 'disque', 'embrayage', 'turbo', 'pompe']

auto_marque = ['VW', 'Audi', 'BMW', 'Renault', 'Citroen']

####################################################"
##################
### Exercice 1 ###
##################

semaine = ['Lundi', 'Mardi', 'Mercredi', 'Judi', 'Vendredi', 'Samedi', 'Dimanche']


print("Jours ouvrable: ", semaine[0:5])
print("Ya Hey week-end: ", semaine[5:7])

##################
### Exercice 2 ###
##################

print(semaine[6])
print(semaine[-1])

##################
### Exercice 3 ###
##################

semaine.reverse()
print(semaine)

##################
### Exercice 4 ###
##################

hiver = ['Decembre','Janvier','Fevrier']
printemps = ['Mars','Avril','Mai']
ete = ['Juin','Juillet','Auot']
automne = ['Septembre','Octobre','Novembre']

saisons = [hiver,printemps,ete,automne]

print(saisons[2]) # S'affiche tout de liste avec indice 2 est liste ete dans liste saison
print(saisons[1][0]) # S'affiche indice 0 (Mars) dans la liste avec indice 1 est printemps
print(saisons[1:2]) 
print(saisons[:][1]) # S'affiche tout dans la liste avec indice 1


###################
### Exercice 5.2 ###
###################


#select_saisons = int(input("Sélectionnez un saisons par numbre de la liste en-dessus: "))
select_saisons = input("Ecrit une saison souvent \n hiver \n printemps \n ete \n automne \n: ")

if select_saisons == 'hiver':
    print(saisons[0])

elif select_saisons == 'printemps':
    print(saisons[1])
    
elif select_saisons == 'ete':
    print(saisons[2])
    
elif select_saisons == 'automne':
    print("les mois de la saison sont:",saisons[3])


#if select_saisons == 0:
    #print(saisons[0])

#elif select_saisons == 1:
    #print(saisons[1])
    
#elif select_saisons == 2:
    #print(saisons[2])
    
#else:
    #print(saisons[3])

