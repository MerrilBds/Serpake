import pygame #pygame documentation
from pygame.locals import *

def draw_block():
    surface.fill((110, 110, 5))
    surface.blit(block,(block_x,block_y))
    pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    #  taille de la fenêtre de jeu
    window_size = (1000, 500)
    # Fenêtre de jeu 500 px x 500px
    surface = pygame.display.set_mode((window_size))

    # Rempli la surface (fenêtre) avec une couleur
    surface.fill((110, 110, 5))

    # Ressources
    block = pygame.image.load("ressources/block.jpg").convert()
    block_x = 100 # position  du block axe X
    block_y = 100 # position  du block axe Y

     # Dessine le bloc sur la surface
    surface.blit(block,(block_x,block_y))

    # Mise à jour de l'écran
    pygame.display.flip()

    # Initialiser la variable "running" à True pour démarrer la boucle principale
    running = True

    # Boucle principale du jeu
    while running:
        # Gestion des événements Pygame
        for event in pygame.event.get():
            # Vérifier si l'événement est une  touche appuyée sur clavier pour rentrée dans la condition
            if event.type == KEYDOWN:
                # Vérifier si la touche pressée est la touche Échap (K_ESCAPE)
                if event.key == K_ESCAPE:
                    # Si c'est le cas, changer la valeur de "running" à False pour sortir de la boucle
                    running = False

                if event.key == K_UP:
                    block_y -= 10
                    draw_block()
                if event.key == K_DOWN:
                    block_y += 10
                    draw_block()
                if event.key == K_LEFT:
                    block_x -= 10
                    draw_block()
                if event.key == K_RIGHT:
                    block_x += 10
                    draw_block()

            # Vérifier si l'événement est la fermeture de la fenêtre
            elif event.type == QUIT:
                # Si c'est le cas, changer la valeur de "running" à False pour sortir de la boucle
                running = False
