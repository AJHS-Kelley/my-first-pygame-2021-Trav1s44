#my first pygame, brandon flagg, 11/30/21, 2:46pm, v0.4

import pygame, sys
from pygame.locals import *

#start pygame
pygame.init()

#setup the game window.
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello, World!')

# setup color values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLABLU = (55, 150, 255)

# setup fount 
basicfont = pygame.font.SysFont(None, 48) 

# setup text
text = basicfont.render('Hello, world!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery
