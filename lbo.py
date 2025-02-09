import pygame
import random
from lbo_tree import Tree

# Initialisation de Pygame
pygame.init()

# Définition des paramètres généraux du labyrinthe
screen_w = 800
screen_h = 600

lbo_h=10
Tree.hauteur = lbo_h
lbo_w=20
Tree.largeur = lbo_w

box_h=screen_h//lbo_h
box_w=screen_w//lbo_w

# Définition de la police d’écriture
pygame.font.init()
font = pygame.font.Font(None, 12)  # Police par défaut, taille 40


WIDTH, HEIGHT = screen_w, screen_h

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Mon premier jeu grâce à Pygame !")

mylbo = Tree.initialise_arbre(lbo_h, lbo_w)
mylbo[0][0].isStartLeaf = True
mylbo[0][0].randomFinalLeaf()

# Définition des couleurs
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

actual_color = BLUE
current_pos_x = 0
current_pos_y = 0

lbo_ok = False

# Boucle principale
running = True
while running:
    screen.fill(WHITE)  # Remplit l'écran en blanc

    if not lbo_ok:
        nodepath = random.randint(0,Tree.hauteur*Tree.largeur-1)
        mylbo[nodepath//Tree.largeur][nodepath % Tree.largeur].clearOneWall()
        mylbo[0][0].colorie()
        if(Tree.compter_zones_uniques(mylbo) == 1):
            lbo_ok = True
        else:
            print("il reste ce nombre de zone : ", Tree.compter_zones_uniques(mylbo))

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Contour du labyrinthe
    pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, HEIGHT),1)
    # Dessiner le point de départ (0,0 par défaut)
    for i in range(0,lbo_h,1):
        for j in range(0,lbo_w,1):
            #Mur de droite
            if(mylbo[i][j].rightWall):
                pygame.draw.line(screen, BLACK, (current_pos_x+box_w, current_pos_y),(current_pos_x+box_w, current_pos_y+box_h),1)

            #Mur du bas
            if(mylbo[i][j].downWall):
                pygame.draw.line(screen, BLACK, (current_pos_x, current_pos_y+box_h),(current_pos_x+box_w, current_pos_y+box_h),1)
            
            #Affiche l'identifiant de case
            text_surface = font.render(str(mylbo[i][j].zoneID), True, BLACK)  # Rendu texte noir
            text_rect = text_surface.get_rect(center=(current_pos_x + box_w // 2, current_pos_y + box_h // 2))
            screen.blit(text_surface, text_rect)
            
            current_pos_x += box_w
            actual_color = WHITE
        current_pos_y += box_h
        current_pos_x = 0
    actual_color = BLUE
    current_pos_x = 0
    current_pos_y = 0
    # Mise à jour de l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
