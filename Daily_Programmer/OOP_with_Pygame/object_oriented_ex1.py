import pygame
import random

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()

# Classes to be used my Pygame

class BlobClass:

    def __init__(self, color):
        self.x = random.randrange(0, WIDTH)
        self.y = random.randrange(0, HEIGHT)
        self.size = random.randrange(4, 8)
        self.color = color

    def move(self):
        self.move_x = random.randrange(-1, 2)
        self.move_y = random.randrange(-1, 2)
        self.x += self.move_x
        self.y += self.move_y

        # May not be PEP8, but its easier to read
        if self.x < 0: self.x = 0
        elif self.x > WIDTH: self.x = WIDTH

        if self.y < 0: self.y = 0
        elif self.y > HEIGHT: self.y = HEIGHT


def draw_environment():
    # This will "clear" the frame
    game_display.fill(WHITE)
    # This sends the image to the screen to be displayed
    pygame.display.update()


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_environment()
        clock.tick(60)


if __name__ == '__main__':
    main()
