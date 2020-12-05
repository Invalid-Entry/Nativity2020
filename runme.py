# This is the main entry script. See README

import sys

import pygame
from pygame.time import Clock

from utils.spritedex import Spritedex
from elements.camel import Camel

pygame.init()

# args!
# FIXME: use  argparse
display_id = 0
if len(sys.argv) > 1:
    display_id = int(sys.argv[1])

width = 500
height = 500

screen = pygame.display.set_mode((width,height), display=display_id)

# Setup objects and flags

alive = True
clock = Clock()
spritedex = Spritedex()

# FIXME - lots of background bits to go in here

objects = []

objects.append(Camel(spritedex, (220, 220), 0, "KING_ONE"))
objects.append(Camel(spritedex, (120, 220), 4, "KING_TWO"))
objects.append(Camel(spritedex, (80, 220), 2, "KING_THREE"))

while alive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Bye Bye")
            pygame.display.quit()
            alive = False

    if alive:
        screen.fill((0,0,0))

        # Background

        # Objects
        for obj in objects:
            obj.render(screen)

        pygame.display.flip()
        clock.tick(15)
