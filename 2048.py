import random


def creer_grille(taille):
    grille = []
    for _ in range(taille):
        ligne = [0] * taille
        grille.append(ligne)
    return grille

def ajouter_tuile(grille):
    cases_vides = []
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if grille[i][j] == 0:
                cases_vides.append((i, j))

    if len(cases_vides) > 0:
        i, j = random.choice(cases_vides)
        grille[i][j] = 2 if random.random() < 0.9 else 4

def afficher_grille(grille):
    for ligne in grille:
        texte = ""
        for case in ligne:
            if case == 0:
                texte += "    |"
            else:
                texte += f"{str(case).rjust(4)}|"
        print(texte)
        print("-" * (len(grille) * 5 - 1))

# Étape 2 : Interaction avec le joueur
def demander_direction():
    touches = {"z": "haut", "q": "gauche", "s": "bas", "d": "droite"}
    while True:
        touche = input("Déplacez avec Z (haut), Q (gauche), S (bas), D (droite) : ").strip().lower()
        if touche in touches:
            return touches[touche]
        print("Touche invalide. Utilisez Z, Q, S ou D.")

# Étape 3 : Déplacer une ligne
def deplacer_ligne(ligne):
    taille = len(ligne)
    resultat = [0] * taille
    position = 0

    for i in range(taille):
        if ligne[i] != 0:
            if resultat[position] == 0:
                resultat[position] = ligne[i]
            elif resultat[position] == ligne[i]:
                resultat[position] += ligne[i]
                position += 1
            else:
                position += 1
                resultat[position] = ligne[i]

    return resultat


def appliquer_mouvement(grille, direction):
    taille = len(grille)
    nouvelle_grille = creer_grille(taille)

    if direction == "gauche":
        for i in range(taille):
            nouvelle_grille[i] = deplacer_ligne(grille[i])

    elif direction == "droite":
        for i in range(taille):
            nouvelle_grille[i] = deplacer_ligne(grille[i][::-1])[::-1]

    elif direction == "haut":
        for j in range(taille):
            colonne = [grille[i][j] for i in range(taille)]
            nouvelle_colonne = deplacer_ligne(colonne)
            for i in range(taille):
                nouvelle_grille[i][j] = nouvelle_colonne[i]

    elif direction == "bas":
        for j in range(taille):
            colonne = [grille[i][j] for i in range(taille)][::-1]
            nouvelle_colonne = deplacer_ligne(colonne)[::-1]
            for i in range(taille):
                nouvelle_grille[i][j] = nouvelle_colonne[i]

    return nouvelle_grille


if __name__ == "__main__":
    taille = int(input("Choisissez la taille de la grille:"))
    grille = creer_grille(taille)
    ajouter_tuile(grille)
    ajouter_tuile(grille)

    while True:
        afficher_grille(grille)
        direction = demander_direction()
        nouvelle_grille = appliquer_mouvement(grille, direction)

        if nouvelle_grille != grille:
            ajouter_tuile(nouvelle_grille)
            grille = nouvelle_grille
        else:
            print("Impossible de bouger dans cette direction.")

        
        mouvement_possible = any(
            appliquer_mouvement(grille, d) != grille for d in ["haut", "bas", "gauche", "droite"]
        )
        if not mouvement_possible:
            print("Game Over ! Vous avez perdu.")
            afficher_grille(grille)
            break
