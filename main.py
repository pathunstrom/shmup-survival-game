__author__ = 'Patrick Thunstrom'

import pygame
import game

pygame.init()
display = pygame.display.set_mode((600, 700))
handler = game.Game()

while True:
    handler.main_loop()