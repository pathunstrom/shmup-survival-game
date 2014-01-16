__author__ = 'Patrick'

import pygame


class Player(object):
    """Handle player attributes and weapons fire."""

    def __init__(self, spawn_point):
        """Return Player"""
        self.rect = pygame.Rect(0, 0, 20, 20)
        self.weapon = None
        self.location = [float(spawn_point[0]), float(spawn_point[1])]

    def move(self):
        """Move player"""
        return None


    def animate(self):
        """Update surface with player location"""
        return None

    def update(self):
        self.update()
        self.animate()
        return None