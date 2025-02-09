import pygame
import lbo_tree

# Initialisation de Pygame
pygame.init()

# Définition des paramètres généraux du labyrinthe
screen_w = 800
screen_h = 600
lbo_h=10
lbo_w=20
box_h=screen_h//lbo_h
box_w=screen_w//lbo_w

WIDTH, HEIGHT = screen_w, screen_h

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Mon premier jeu grâce à Pygame !")

# Définition des couleurs
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

actual_color = BLUE
current_pos_x = 0
current_pos_y = 0

# Boucle principale
running = True
while running:
    screen.fill(WHITE)  # Remplit l'écran en blanc

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dessiner le point de départ (0,0 par défaut)
    for i in range(0,lbo_h,1):
        for j in range(0,lbo_w,1):
            pygame.draw.rect(screen, actual_color, (current_pos_x, current_pos_y, box_w, box_h))
            pygame.draw.rect(screen, BLACK, (current_pos_x, current_pos_y, box_w, box_h),3)
            current_pos_x += box_w
            actual_color = WHITE
            print("passage 1 : ",current_pos_x)
        current_pos_y += box_h
        current_pos_x = 0
    actual_color = BLUE
    current_pos_x = 0
    current_pos_y = 0
    # Mise à jour de l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
