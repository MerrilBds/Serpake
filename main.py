import pygame
from pygame.locals import *
import time

class Snake:
    def __init__(self, surface):
        # Constructeur de la classe Snake
        # Paramètres :
        #   surface : La surface sur laquelle le serpent sera dessiné.
        self.parent_screen = surface
        self.block = pygame.image.load("ressources/block.jpg").convert()
        self.x = 100
        self.y = 100
        self.direction = 'down'

    def move_left(self):
        # Change la direction du serpent vers la gauche
        self.direction = 'left'

    def move_right(self):
        # Change la direction du serpent vers la droite
        self.direction = 'right'

    def move_up(self):
        # Change la direction du serpent vers le haut
        self.direction = 'up'

    def move_down(self):
        # Change la direction du serpent vers le bas
        self.direction = 'down'

    def walk(self):
        # Fonction pour faire avancer le serpent dans la direction actuelle
        if self.direction == 'left':
            self.x -= 10
        if self.direction == 'right':
            self.x += 10
        if self.direction == 'up':
            self.y -= 10
        if self.direction == 'down':
            self.y += 10

        self.draw()

    def draw(self):
        # Dessine le serpent sur la surface avec sa position actuelle
        self.parent_screen.fill((110, 110, 5))
        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()


class Game:
    def __init__(self):
        # Constructeur de la classe Game
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

            self.snake.walk()

            time.sleep(.2)  # Ajout d'une pause pour ralentir le déplacement du serpent

if __name__ == '__main__':
    game = Game()
    game.run()
