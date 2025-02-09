import pygame
import random
import time
from lbo_tree import Tree

# Initialisation de Pygame
pygame.init()

# Définition des paramètres du labyrinthe
screen_w, screen_h = 1024, 768

lbo_h, lbo_w = 10, 20  # Taille du labyrinthe

Tree.hauteur = lbo_h
Tree.largeur = lbo_w

box_h = screen_h // lbo_h
box_w = screen_w // lbo_w

# Définition des couleurs
WHITE, BLACK, BLUE, RED = (255, 255, 255), (0, 0, 0), (0, 0, 255), (255, 0, 0)

# Charger les images du sprite
player_images = {
    "idle": pygame.image.load("idle.png"),  # Image statique
    "left": pygame.image.load("left.png"),
    "right": pygame.image.load("right.png"),
    "up": pygame.image.load("up.png"),
    "down": pygame.image.load("down.png")
}
# Redimensionner les images
for key in player_images:
    player_images[key] = pygame.transform.scale(player_images[key], (box_h//3, box_w//3))
    
# Position initiale
player_x, player_y = 5, 0
player_speed = min(5, box_w // 4)

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
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Position dans la grille    
    grid_x = round(player_x / box_w)
    grid_y = round(player_y / box_h)

    # Détection des touches pressées
    keys = pygame.key.get_pressed()

    # Détection des collisions AVANT de bouger
    # Vérifier les murs autour de la position actuelle
    if keys[pygame.K_LEFT] and player_x > 0:  # Mur à gauche
        current_image = player_images["left"]
        if not mylbo[grid_y-1][grid_x].rightWall:
            player_x -= player_speed

    elif keys[pygame.K_RIGHT] and player_x < screen_w - box_w:  # Mur à droite
        current_image = player_images["right"]
        if not mylbo[grid_y][grid_x].rightWall:
            player_x += player_speed

    elif keys[pygame.K_UP] and player_y > 0:  # Mur en haut
        current_image = player_images["up"]
        if not mylbo[grid_y][grid_x-1].downWall:
            player_y -= player_speed

    elif keys[pygame.K_DOWN] and player_y < screen_h - box_h:  # Mur en bas
        current_image = player_images["down"]
        if not mylbo[grid_y][grid_x].downWall:
            player_y += player_speed
    else:
        current_image = player_images["idle"]  # Image neutre quand aucune touche pressée        
    
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
     # Afficher le sprite
    screen.blit(current_image, (player_x, player_y))

    pygame.display.flip()  # Mettre à jour l’écran
    pygame.time.delay(20) 
    print("case actuelle : ",grid_x, grid_y)
pygame.quit()