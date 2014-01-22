__author__ = 'Patrick Thunstrom'

import pygame
import game

pygame.init()
pygame.mouse.set_cursor(*pygame.cursors.broken_x)
display = pygame.display.set_mode((600, 700))
handler = game.Game(display)

while True:
    handler.main_loop()