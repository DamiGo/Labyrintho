import pygame
import random
import time
from lbo_tree import Tree

# Initialisation de Pygame
pygame.init()

# Définition des paramètres du labyrinthe
screen_w, screen_h = 800, 600
lbo_h, lbo_w = 10, 20  # Taille du labyrinthe

Tree.hauteur = lbo_h
Tree.largeur = lbo_w

box_h = screen_h // lbo_h
box_w = screen_w // lbo_w

# Définition des couleurs
WHITE, BLACK, BLUE, RED = (255, 255, 255), (0, 0, 0), (0, 0, 255), (255, 0, 0)

# Création de la fenêtre
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Génération du Labyrinthe en Temps Réel")

# Générer une grille d'arbres (labyrinthe vide)
mylbo = Tree.initialise_arbre(lbo_h, lbo_w)

# Liste de tous les murs à briser (algorithme de Kruskal)
walls = []
for i in range(lbo_h):
    for j in range(lbo_w):
        if i < lbo_h - 1:
            walls.append((i, j, i + 1, j))  # Mur du bas
        if j < lbo_w - 1:
            walls.append((i, j, i, j + 1))  # Mur de droite

random.shuffle(walls)  # Mélanger les murs pour un effet aléatoire

mylbo[0][0].randomFinalLeaf()

# Boucle de fusion avec affichage progressif
while Tree.compter_zones_uniques(mylbo) > 1:
    i1, j1, i2, j2 = walls.pop()  # Sélectionner un mur aléatoire
    Tree.fusionner_zones(mylbo, i1, j1, i2, j2)

    # 🎨 Dessiner le labyrinthe après chaque fusion
    screen.fill((255, 255, 255))

    for i in range(lbo_h):
        for j in range(lbo_w):
            x, y = j * box_w, i * box_h
            #On dessine le départ & l'arrivée
            if(i==0 and j==0):
                pygame.draw.rect(screen,BLUE , (0, 0, box_w, box_h))
            else:
                if(mylbo[i][j].isFinalLeaf):
                    pygame.draw.rect(screen,RED , (x, y, x+box_w, y+box_h))
            # Mur de droite
            if mylbo[i][j].rightWall:
                pygame.draw.line(screen, (0, 0, 0), (x + box_w, y), (x + box_w, y + box_h), 1)

            # Mur du bas
            if mylbo[i][j].downWall:
                pygame.draw.line(screen, (0, 0, 0), (x, y + box_h), (x + box_w, y + box_h), 1)

    pygame.draw.rect(screen, (0, 0, 0), (0, 0, screen_w, screen_h), 1)  # Contour

    pygame.display.flip()  # Mettre à jour l'affichage
    pygame.time.delay(30)  # 🎯 Ajuste la vitesse de génération (réglable)

# Boucle principale de jeu après la génération
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
