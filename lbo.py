import pygame

# Initialisation de Pygame
pygame.init()

# Définition des paramètres de la fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mon premier jeu Pygame")

# Définition des couleurs
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Boucle principale
running = True
while running:
    screen.fill(WHITE)  # Remplit l'écran en blanc

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dessiner un rectangle bleu
    pygame.draw.rect(screen, BLUE, (100, 100, 50, 50))

    # Mise à jour de l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
