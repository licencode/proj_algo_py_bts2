"""
Recherche séquentielle dans une structure non triée

#########
psedo-code

trouve = Faux
i = a
TQ non trouve et i < b
  Si l[i] == x
    trouve = Vrai
  Fin Si
  i = i + 1
Fin TQ
Renvoyer : trouve

"""

def recharche_seq_non_triee (l,a,b,x):
    trouve = False
    i = a
    while not trouve and i < b:
        print("premier indice est:", i, "dernier indice est:", b, "Valeur souhaitée est:", x)
        if l[i] == x:
            trouve = True
        else:
            i = i + 1
    return trouve


liste =  [3,5,8,1,4]

affiche = recharche_seq_non_triee(liste,0,4,10)

print(affiche)