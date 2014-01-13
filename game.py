__author__ = 'Patrick Thunstrom'

import pygame
from pygame import *
import sys
import player


w = ord("w")
a = ord("a")
s = ord("s")
d = ord("d")


class Game(object):
    """Read the pygame event queue and call necessary methods."""

    def __init__(self, display):
        """Return Null"""
        self.display = display
        self.gamearea = pygame.Rect(0, 0, 600, 600)
        self.surface = pygame.Surface((600, 600))
        self.clock = pygame.time.Clock()
        self.player = player.Player(self.gamearea.center)
        self.spawner = NotImplemented

    @staticmethod
    def quit():
        """Quit pygame and exit."""
        pygame.quit()
        sys.exit()

    def handler(self):
        """Handle the event queue."""
        for e in pygame.event.get():
            if e.type == QUIT:
                self.quit()

    def update(self):
        frames = self.clock.tick()
        delta = float(frames) / float(1000.0000)
        print delta
        self.handler()
        self.display.blit(self.surface)
        pygame.display.update()

    def main_loop(self):
        while True:
            self.update()
