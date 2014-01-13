__author__ = 'Patrick'

import pygame


class Mobile(object):

    def __init__(self, (width, height), (red, green, blue), surface):
        self.rect = pygame.Rect(0, 0, width, height)
        self.color = (red, green, blue)
        self.xy = [float(self.rect.centerx), float(self.rect.centery)]
        self.surface = surface

    def move(self):
        return

    def animate(self):
        radius = self.rect.width / 2
        pygame.draw.circle(self.surface, self.color, self.rect.center, radius)

    def update(self):
        self.move()
        self.animate()