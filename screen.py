import pygame, sys
from pygame import *
import initial
from consts import *


def grass_screen():
    screen = initial.creating_empty_board()
    screen.fill(GREEN)
    display.flip()
    initial.random_bush_bomb('grass', screen)
    initial.placement(screen, 'soldier', SOLDIER_START)
    initial.placement(screen, 'flag', FLAG)


running = True

while running:
    # screen.fill(green)
    grass_screen()
    display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# sys.exit()
quit()

























#
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# green= (64,200,45)
# screen = display.set_mode((800, 600))

#
# running = True
#
# while running:
#     # screen.fill(green)
#     display.flip()
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
# # sys.exit()
# quit()
