import random      #for generating random numbers
import sys        #to exit the game we have to use sys.exit
import pygame
import pygame.locals import *     #basic pygame imports

#global variables for the game
FPS = 32                                   #frames per second
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))   #initialize the display
GROUNDY = SCREENWIDTH * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = ''
BACKGROUND = ''
PIPE = ''
