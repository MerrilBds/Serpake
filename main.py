import pygame
from pygame.locals import *

class Snake:
    def __init__(self, surface):
        # Constructeur de la classe Snake
        # Paramètres :
        #   surface : La surface sur laquelle le serpent sera dessiné.
        self.parent_screen = surface
        self.block = pygame.image.load("ressources/block.jpg").convert()
        self.x = 100
        self.y = 100

    def move_left(self):
        # Déplace le serpent vers la gauche
        self.x -= 10
        self.draw()

    def move_right(self):
        # Déplace le serpent vers la droite
        self.x += 10
        self.draw()

    def move_up(self):
        # Déplace le serpent vers le haut
        self.y -= 10
        self.draw()

    def move_down(self):
        # Déplace le serpent vers le bas
        self.y += 10
        self.draw()

    def draw(self):
        # Dessine le serpent sur la surface avec sa position actuelle
        # Effet :
        #   Remplit la surface avec une couleur,
        #   blit l'image du bloc à la position actuelle,
        #   met à jour l'écran.
        self.parent_screen.fill((110, 110, 5))
        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()

class Game:
    def __init__(self):
        # Constructeur de la classe Game
        # Effet :
        #   Initialise Pygame,
        #   crée une surface de jeu,
        #   crée une instance de la classe Snake.
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 500))
        self.snake = Snake(self.surface)
        self.snake.draw()

    def run(self):
        # Boucle principale du jeu
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                elif event.type == QUIT:
                    running = False

if __name__ == '__main__':
    # Fonction principale
    # Effet :
    #   Crée une instance de la classe Game,
    #   lance la boucle principale du jeu.
    game = Game()
    game.run()
