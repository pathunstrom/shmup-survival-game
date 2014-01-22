__author__ = 'Patrick Thunstrom'

import pygame
from pygame.locals import *
import sys
import player
import enemy


FPS = []


class Game(object):
    """Read the pygame event queue and call necessary methods."""

    def __init__(self, main_display):
        """Return Game"""
        self.display = main_display
        self.gamearea = pygame.Rect(0, 0, 600, 600)
        self.surface = pygame.Surface((600, 600))
        self.clock = pygame.time.Clock()
        self.player = player.Player(self.gamearea, self.surface)
        self.spawner = enemy.Spawner(self.gamearea, self.surface, self.player)

    @staticmethod
    def quit():
        """Quit pygame and exit."""
        print("Average FPS: %f" % (sum(FPS) / len(FPS)))
        pygame.quit()
        sys.exit()

    def handler(self):
        """Handle the event queue. Return None"""
        for e in pygame.event.get():
            if e.type == MOUSEBUTTONUP:
                self.player.trigger(e.pos)
            if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                self.quit()

    def update(self):
        """Call game logic, redraw frame, no return value."""
        time = self.clock.tick()
        #debug code to track FPS
        FPS.append(self.clock.get_fps())
        self.surface.fill((0, 0, 0))
        # Store all location data as pixel location * 1000.
        self.handler()
        self.spawner.update(time)
        self.player.update(time)
        self.display.blit(self.surface, (0, 0))
        pygame.display.update()

    def main_loop(self):
        """Game loop. No return value."""
        while True:
            self.update()
