# Simple Animation with PyGame, Brandon flagg, 1/10/22, 2:33Pm, v0.8


import pygame, sys, time
from pygame.locals import *

# setup pygame
pygame.init()

#setup the window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),0, 32)
pygame.display.set_caption('Animation Example!')

# setup the direction variables
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4

# setup color values.
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# setu the box data 
b1 = {'rect':pygame.Rect(300, 80, 50, 100), 'color':RED, 'dir':UPRIGHT}
b2 = {'rect':pygame.Rect(200, 200, 20, 20), 'color':GREEN, 'dir':UPLEFT}
b3 = {'rect':pygame.Rect(100, 150, 60, 60), 'color':BLUE, 'dir':DOWNLEFT}
boxes = [b1, b2, b3]

# run the game loop
while True:
    #check for Quit event.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    windowSurface.fill(WHITE)

    for b in boxes:
        # move the box data structure 
        if b['dir'] == DOWNLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top += MOVESPEED 
        if b['dir'] == DOWNRIGHT:
            b['rect'].left -= MOVESPEED
            b['rect'].top += MOVESPEED 
        if b['dir'] == UPLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == UPRIGHT:
            b['rect'].left -= MOVESPEED
            b['rect'].top += MOVESPEED

        if b['rect'].top < 0:
            # the box has moved past the top
            if b['dir'] == UPLEFT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = DOWNRIGHT
            if b['rect'].bottom > WINDOWHEIGHT: # Move this line 4 spaces to the LEFT. 
                #the box has moved past the bottom.
                if b['dir'] == DOWNLEFT: # Move this line 4 spaces to the LEFT. 
                    b['dir'] = UPLEFT # Move this line 4 spaces to the LEFT. 
                if b['dir'] == DOWNRIGHT: # Move this line 4 spaces to the LEFT. 
                    b['dir'] = UPRIGHT # Move this line 4 spaces to the LEFT. 
            if b['rect'].left < 0: # Move this line 4 spaces to the LEFT. 
                #the box has moved past the left
                if b['dir'] == DOWNLEFT: # Move this line 4 spaces to the LEFT. 
                    b['dir'] = DOWNRIGHT # Move this line 4 spaces to the LEFT. 
                if b['dir'] == UPLEFT: # Move this line 4 spaces to the LEFT. 
                    b['dir'] = UPRIGHT # Move this line 4 spaces to the LEFT. 
            if b['rect'].right > WINDOWWIDTH: # Move this line 4 spaces to the LEFT. 
                #the box has moved past the right.
                if b['dir'] == DOWNRIGHT: # Move this line 4 spaces to the LEFT. 
                    b['dir'] = DOWNLEFT # Move this line 4 spaces to the LEFT. 
                if b['dir'] == UPRIGHT: # Move this line 4 spaces to the LEFT. 
                    b['dir'] = UPLEFT # Move this line 4 spaces to the LEFT. 
        # Draw the box onto the game surface.
        pygame.draw.rect(windowSurface, b['color'], b['rect'])

    # Draw the window to the screen
    pygame.display.update()
    time.sleep(0.02)
                