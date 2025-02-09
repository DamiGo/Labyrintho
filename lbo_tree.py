import random

class Tree:
    #Variables statiques
    hauteur = 1
    largeur = 1

    def __init__(self):
        self.down = None
        self.downWall = True
        self.right = None
        self.rightWall = True
        self.isFinalLeaf = False
        self.isStartLeaf = False
        self.zoneID = 0

    def colorie(self):
        if self.down and self.down.zoneID != self.zoneID and not self.downWall:
            self.down.zoneID = self.zoneID
        if self.right and self.right.zoneID != self.zoneID and not self.rightWall:
            self.right.zoneID = self.zoneID
        if self.down:
            self.down.colorie()
        if self.right:
            self.right.colorie()
    
    def randomFinalLeaf(self):
        if (self.down == None) or (self.right == None):
            self.isFinalLeaf = True
        else:
            nodepath = random.randint(0,1)
            if nodepath == 0:
                self.down.randomFinalLeaf()
            else:
                self.right.randomFinalLeaf()

    def clearOneWall(self):
        nodepath = random.randint(0, 1)
        if nodepath == 0 and self.down and self.down.zoneID != self.zoneID:
            self.downWall = False
        elif self.right and self.right.zoneID != self.zoneID:
            self.rightWall = False
    
    @staticmethod
    def initialise_arbre(hauteur: int, largeur: int):
        """
        Initialise une grille d'arbres avec les connexions entre cases.
        Retourne un tableau 2D de Tree.
        """
        grille = [[Tree() for _ in range(largeur)] for _ in range(hauteur)]

        # Création des connexions entre les nœuds
        for i in range(hauteur):
            for j in range(largeur):
                grille[i][j].zoneID = largeur*i + j

                if i < hauteur - 1:
                    grille[i][j].down = grille[i + 1][j]  # Lier en bas
                if j < largeur - 1:
                    grille[i][j].right = grille[i][j + 1]  # Lier à droite

        return grille  # Retourne la grille d'arbres

    @staticmethod
    def compter_zones_uniques(grille):
        """
        Compte le nombre de zoneID uniques dans une grille d'arbres.
        :param grille: Liste 2D contenant les instances de Tree.
        :return: Nombre de zones uniques.
        """
        zone_ids = set()  # Utilisation d'un ensemble pour éviter les doublons

        for ligne in grille:
            for arbre in ligne:
                zone_ids.add(arbre.zoneID)  # Ajoute chaque zoneID unique

        return len(zone_ids)  # Retourne le nombre de zones distinctes