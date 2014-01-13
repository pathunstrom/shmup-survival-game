__author__ = 'Patrick'

import pygame


class Player(object):
    """Handle player attributes and weapons fire."""

    def __init__(self, spawn_point):
        self.rect = pygame.Rect(0, 0, 20, 20)
        self.weapon = NotImplemented
        self.location = [float(spawn_point[0]), float(spawn_point[1])]

    def move(self):
        return


    def animate(self):
        return

    def update(self):
        return