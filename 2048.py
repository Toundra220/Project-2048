import random

def grille(x,y):
    grille1 = []
    for i in range(y):
        ligne = []
        for j in range(x):
            ligne.append(".")
        grille1.append(ligne)

def ajouter_tuile(grille1):
    x = random.randint(0, len(grille1)-1)
    y = random.randint(0, len(grille1)-1) 
    grille1[x][y] = random.randrange(2,4,2)
    return grille1

def afficher_grille():
    ma_grille = grille(4,4)
    ma_grille = ajouter_tuile(ma_grille)
    for ligne in ma_grille:
        print(ligne)
