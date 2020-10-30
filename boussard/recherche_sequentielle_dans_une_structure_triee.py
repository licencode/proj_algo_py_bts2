"""
Recherche séquentielle dans une structure triée

#########
Psedo-code

i = a
TQ i < b et x < l[i]
  i = i + 1
Fin TQ
Si i < b et x == l[i]
  Renvoyer : Vrai
Sinon
  Renvoyer : Faux
Fin Si

"""

def recharche_seq_triee(l,a,b,x):
    i = a
    print("Tant que", i, "moins que", b, "et", x, "moins que", l[i])
    print(i, "+ 1")
    print("Si", i, "moins que", b, "et", x, "==", l[i])
    while i < b and x < l[i]:
        i = i + 1
    if i < b and x == l[i]:
        return True
    else:
        return False
    
liste = [1,2,3,4,5,6]

affiche = recharche_seq_triee(liste, 0, 9, 8)
print(affiche)