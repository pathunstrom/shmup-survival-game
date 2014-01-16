__author__ = 'Patrick Thunstrom'

import pygame
from pygame.locals import *
import sys
import player


w = ord("w")
a = ord("a")
s = ord("s")
d = ord("d")


class Game(object):
    """Read the pygame event queue and call necessary methods."""

    def __init__(self, main_display):
        """Return Game"""
        self.display = main_display
        self.gamearea = pygame.Rect(0, 0, 600, 600)
        self.surface = pygame.Surface((600, 600))
        self.clock = pygame.time.Clock()
        self.player = player.Player(self.gamearea.center)
        self.spawner = None

    @staticmethod
    def quit():
        """Quit pygame and exit."""
        pygame.quit()
        sys.exit()

    def handler(self):
        """Handle the event queue. Return None"""
        for e in pygame.event.get():
            if e.type == QUIT:
                self.quit()

        return None

    def update(self):
        """Call game logic, redraw frame, return None"""
        frames = self.clock.tick()
        delta = float(frames) / float(1000.0000)
        print delta
        self.handler()
        self.display.blit(self.surface)
        pygame.display.update()
        return None

    def main_loop(self):
        """Game loop. No return value."""
        while True:
            self.update()
