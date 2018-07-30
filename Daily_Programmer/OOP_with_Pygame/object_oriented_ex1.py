# Generally, PEP8 suggests 1 line of white space between functions and 2 between classes.

import pygame
import random
from blob import Blob

STARTING_BLUE_BLOBS = 10
STARTING_RED_BLOBS = 3
STARTING_GREEN_BLOBS = 6

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


class BlueBlob(Blob):

    pass
"""
    def __init__(self, x_boundary, y_boundary):
        super().__init__()
        Blob.__init__(self, (0, 0, 255), x_boundary, y_boundary)

    def __add__(self, other_blob):
        if other_blob.color == RED:
            self.size -= other_blob.size
            other_blob.size -= self.size


class RedBlob(Blob):

    def __init__(self, x_boundary, y_boundary):
        Blob.__init__(self, (255, 0, 0), x_boundary, y_boundary)

    def __add__(self, other_blob):
        if other_blob.color == GREEN:
            self.size -= other_blob.size
            other_blob.size -= self.size


class GreenBlob(Blob):

    def __init__(self, x_boundary, y_boundary):
        Blob.__init__(self, (0, 255, 0), x_boundary, y_boundary)

    def __add__(self, other_blob):
        if other_blob.color == BLUE:
            self.size -= other_blob.size
            other_blob.size -= self.size
"""

def draw_environment(blob_list):
    # This will "clear" the frame
    game_display.fill(WHITE)
    for blob_dict in blob_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
            blob.move()
    # This sends the image to the screen to be displayed
    pygame.display.update()


def main():
    red_blobs = dict(enumerate([BlueBlob(RED, WIDTH, HEIGHT) for i in range(STARTING_RED_BLOBS)]))
    blue_blobs = dict(enumerate([BlueBlob(BLUE, WIDTH, HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))
    green_blobs = dict(enumerate([BlueBlob(GREEN, WIDTH, HEIGHT) for i in range(STARTING_GREEN_BLOBS)]))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_environment([red_blobs, blue_blobs, green_blobs])
        clock.tick(60)


if __name__ == '__main__':
    main()
