import pygame, sys
from pygame import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
green = (64, 200, 45)
screen = display.set_mode((800, 600))

running = True

while running:
    screen.fill(green)
    display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

sys.exit()
quit()
