# This is the main entry script. See README

import sys

import random
import pygame
from pygame.time import Clock

from utils.spritedex import Spritedex
from elements.camel import Camel
from elements.parallax import Background, SnowConfig
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

# Setup of Objects
objects = []

BGSnowConfig = SnowConfig(40, 1, (128,128,128,255))
FGSnowConfig = SnowConfig(30, 2, (180, 180, 180, 250))
GroundSnowConfig = SnowConfig(20, 3, (230, 230, 230, 250))
GroundSnowConfig2 = SnowConfig(10, 3, (255, 255, 255, 245))

objects.append(Background("assets/BG_04/Layers/Sky.png", 1))
objects.append(Star(spritedex, (width - 200, 30)))
# Ugly moon thing
#objects.append(Background("assets/BG_04/Layers/BG_Decor.png", 4))
objects.append(Background("assets/BG_04/Layers/Middle_Decor.png", 8, BGSnowConfig))
objects.append(Background("assets/BG_04/Layers/Foreground.png", 10, FGSnowConfig))
objects.append(Background("assets/BG_04/Layers/Ground_01.png", 17, GroundSnowConfig))

objects.append(Camel(spritedex, (220, height-180), 0, "KING_ONE"))
objects.append(Camel(spritedex, (120, height-189), 4, "KING_TWO"))
objects.append(Camel(spritedex, (80, height-178), 2, "KING_THREE"))

objects.append(Background("assets/BG_04/Layers/Ground_02.png", 17, GroundSnowConfig2))

while alive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Bye Bye")
            pygame.display.quit()
            alive = False

    if alive:
        screen.fill((0,0,0))

        # Objects
        wind = random.choice((-2,-2,-1,-1,-1,0,0,0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4))

        for obj in objects:
            obj.render(screen, wind)

        pygame.display.flip()
        clock.tick(15)
