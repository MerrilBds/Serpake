import pygame
from pygame.locals import *
import time
import random

SIZE = 40

class Apple:
    def __init__(self, parent_screen):
        # Constructeur de la classe Apple
        # Paramètres :
        #   parent_screen : La surface sur laquelle la pomme sera dessinée.
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/apple.png").convert()
        self.x = 120
        self.y = 120

    def draw(self):
        # Dessine la pomme sur la surface avec sa position actuelle
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        # Déplace la pomme à une position aléatoire sur la surface
        self.x = random.randint(1, 25) * SIZE
        self.y = random.randint(1, 20) * SIZE

class Snake:
    def __init__(self, parent_screen, length):
        # Constructeur de la classe Snake
        # Paramètres :
        #   parent_screen : La surface sur laquelle le serpent sera dessiné.
        #   length : Longueur initiale du serpent.
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/block.jpg").convert()
        self.direction = 'down'

        self.length = length
        self.x = [40] * length
        self.y = [40] * length

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
        # Met à jour la position du serpent
        # Met à jour le corps du serpent
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        # Met à jour la tête du serpent en fonction de la direction
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()

    def draw(self):
        # Dessine le serpent sur la surface avec sa position actuelle
        self.parent_screen.fill((110, 110, 5))

        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))
        pygame.display.flip()

    def increase_length(self):
        # Augmente la longueur du serpent
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

class Game:
    def __init__(self):
        # Constructeur de la classe Game
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 800))
        self.snake = Snake(self.surface, 2)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def is_collision(self, x1, y1, x2, y2):
        # Vérifie si deux objets rectangulaires se chevauchent
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def display_score(self):
        # Affiche le score à l'écran
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (200, 200, 200))
        self.surface.blit(score, (850, 10))

    def play(self):
        # Fonction principale du jeu
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        # Si le serpent touche la pomme, augmente la longueur du serpent et déplace la pomme
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()

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

            self.play()

            time.sleep(.2)

if __name__ == '__main__':
    game = Game()
    game.run()
