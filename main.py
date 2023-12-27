import pygame
from pygame.locals import *
import time
import random

SIZE = 40
BACKGROUND_COLOR = (110, 110, 5)

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
        self.x = random.randint(1, 24) * SIZE
        self.y = random.randint(1, 19) * SIZE

class Snake:
    def __init__(self, parent_screen):
        # Constructeur de la classe Snake
        # Paramètres :
        #   parent_screen : La surface sur laquelle le serpent sera dessiné.
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/block.jpg").convert()
        self.direction = 'down'

        self.length = 1
        self.x = [40]
        self.y = [40]

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
        pygame.display.set_caption("MerriSnake")

        # Initialisation de la musique de fond
        pygame.mixer.init()
        self.play_background_music()

        self.surface = pygame.display.set_mode((1000, 800))
        self.snake = Snake(self.surface)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def play_background_music(self):
        # Charge et joue la musique de fond en boucle
        pygame.mixer.music.load('resources/bg_music_1.mp3')
        pygame.mixer.music.play(-1, 0)

    def play_sound(self, sound_name):
        # Joue des effets sonores en fonction du nom du son
        if sound_name == "crash":
            sound = pygame.mixer.Sound("resources/crash.mp3")
        elif sound_name == 'ding':
            sound = pygame.mixer.Sound("resources/ding.mp3")

        pygame.mixer.Sound.play(sound)

    def reset(self):
        # Réinitialise le jeu en créant un nouveau serpent et une nouvelle pomme
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)

    def is_collision(self, x1, y1, x2, y2):
        # Vérifie si deux objets rectangulaires se chevauchent
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def render_background(self):
        # Charge et affiche l'image de fond
        bg = pygame.image.load("resources/background.jpg")
        self.surface.blit(bg, (0, 0))

    def play(self):
        # Fonction principale du jeu
        self.render_background()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        # Scenario où le serpent mange la pomme
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.play_sound("ding")
            self.snake.increase_length()
            self.apple.move()

        # Scenario où le serpent entre en collision avec lui-même
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.play_sound('crash')
                raise Exception("Collision Occurred")

    def display_score(self):
        # Affiche le score à l'écran
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (200, 200, 200))
        self.surface.blit(score, (850, 10))

    def show_game_over(self):
        # Affiche l'écran de fin de jeu
        self.surface.fill(BACKGROUND_COLOR)
        font = pygame.font.SysFont('arial', 30)

        # Première ligne avec le score
        line1 = font.render(f"Game over! Ton Score est {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))

        # Deuxième ligne avec les instructions de redémarrage
        line2 = font.render("Restart le jeu appuyez sur la touche 'Enter'.", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))

        # Troisième ligne avec les instructions de sortie
        line3 = font.render("Pour quitter appuyez sur la touche 'Escape'!", True, (255, 255, 255))
        self.surface.blit(line3, (200, 400))

        pygame.display.flip()

    def run(self):
        # Boucle principale du jeu
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False

                    if not pause:
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
            try:

                if not pause:
                    self.play()

            except Exception as e:
                # En cas de collision, affiche l'écran de fin de jeu, met le jeu en pause et réinitialise le jeu
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(.25)

if __name__ == '__main__':
    game = Game()
    game.run()
