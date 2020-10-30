def puissance(n,e):
    produit = 1
    for i in range(1,e+1): # besion ajouter pour "e" +1
        produit = produit * n
    return produit

nb = int(input("Saisir un nombre: "))
exposant = int(input("Saisir exposant: "))

res = puissance(nb,exposant)

print(res)
