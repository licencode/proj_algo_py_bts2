
mdp_choisi = "toto1"
compteur = 0
is_mdp_ok = 0

while compteur <=3 and is_mdp_ok == 0:
    mdp = input("Entrez le mot de passe : ")
    compteur + 1
    if mdp == mdp_choisi:
        print("Mot sz passe OK ...")
        is_mdp_ok = 1
    else:
        print("MDP errone essaye encore !!!")