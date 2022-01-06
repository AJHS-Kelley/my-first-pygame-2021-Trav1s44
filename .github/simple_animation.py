# Simple Animation with PyGame, Brandon flagg, 1/6/22, 1:55Pm, v0.1

import PyGame, sys, time
from PyGame.locals import *

# setup pygame
pygame.init()

#setup the window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),0, 32)
PyGame.display.set_caption('Animation Example!')