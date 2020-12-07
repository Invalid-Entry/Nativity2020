# This is the main entry script. See README

import sys

import pygame
from pygame.time import Clock

from utils.spritedex import Spritedex
from elements.camel import Camel
from elements.parallax import Background
from elements.star import Star

pygame.init()

# args!
# FIXME: use  argparse
display_id = 0
if len(sys.argv) > 1:
    display_id = int(sys.argv[1])

# 1920 x 1080,
width = 1920//2
height = 1080//2

screen = pygame.display.set_mode((width,height), display=display_id)

# Setup objects and flags

alive = True
clock = Clock()
spritedex = Spritedex()

# FIXME - lots of background bits to go in here

objects = []


#objects.append(
# Background("assets/BG_02/BG_02.png", 17))


objects.append(Background("assets/BG_04/Layers/Sky.png", 1))
objects.append(Star(spritedex, (width - 200, 30)))
#objects.append(Background("assets/BG_04/Layers/BG_Decor.png", 4))
objects.append(Background("assets/BG_04/Layers/Middle_Decor.png", 8))
objects.append(Background("assets/BG_04/Layers/Foreground.png", 10))
objects.append(Background("assets/BG_04/Layers/Ground_01.png", 17))

objects.append(Camel(spritedex, (220, height-180), 0, "KING_ONE"))
objects.append(Camel(spritedex, (120, height-189), 4, "KING_TWO"))
objects.append(Camel(spritedex, (80, height-178), 2, "KING_THREE"))

objects.append(Background("assets/BG_04/Layers/Ground_02.png", 17))

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
