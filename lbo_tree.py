import random

class Tree:
    # Variables statiques
    hauteur = 1
    largeur = 1

    def __init__(self):
        self.down = None
        self.downWall = True
        self.right = None
        self.rightWall = True
        self.zoneID = 0

    @staticmethod
    def initialise_arbre(hauteur: int, largeur: int):
        """ Initialise une grille d'arbres avec connexions entre cases """
        grille = [[Tree() for _ in range(largeur)] for _ in range(hauteur)]

        # Création des connexions et attribution des zones
        for i in range(hauteur):
            for j in range(largeur):
                grille[i][j].zoneID = largeur * i + j
                if i < hauteur - 1:
                    grille[i][j].down = grille[i + 1][j]  # Lien vers le bas
                if j < largeur - 1:
                    grille[i][j].right = grille[i][j + 1]  # Lien vers la droite
        return grille

    @staticmethod
    def compter_zones_uniques(grille):
        """ Compte le nombre de zones uniques """
        return len(set(arbre.zoneID for ligne in grille for arbre in ligne))

    @staticmethod
    def fusionner_zones(grille, i1, j1, i2, j2):
        """ Fusionne deux zones et casse un mur entre elles """
        if grille[i1][j1].zoneID != grille[i2][j2].zoneID:
            zone_a_remplacer = grille[i2][j2].zoneID
            nouvelle_zone = grille[i1][j1].zoneID

            for ligne in grille:
                for arbre in ligne:
                    if arbre.zoneID == zone_a_remplacer:
                        arbre.zoneID = nouvelle_zone
            
            # Supprime le mur
            if i1 == i2:  # Fusion horizontale
                grille[i1][j1].rightWall = False
            else:  # Fusion verticale
                grille[i1][j1].downWall = False
