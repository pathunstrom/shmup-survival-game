__author__ = 'Patrick'

import pygame
import random


class Mobile(object):

    def __init__(self, (width, height), (red, green, blue), surface):
        """Return mobile"""
        self.rect = pygame.Rect(0, 0, width, height)
        self.color = (red, green, blue)
        self.xy = [float(self.rect.centerx), float(self.rect.centery)]
        self.surface = surface

    def move(self):
        """Move mobile"""
        return None

    def animate(self):
        """Update surface"""
        radius = self.rect.width / 2
        pygame.draw.circle(self.surface, self.color, self.rect.center, radius)

    def update(self):
        self.move()
        self.animate()


class Spawner(object):
    """Spawner keeps track of and spawns enemies."""

    def __init__(self, area, surface, player):
        self.children = []
        self.area = area
        self.surface = surface
        self.player = player
        self.timer = 0
        self.spawn(Mobile)

    def update(self, time):
        self.timer += time
        self.damage()
        for m in self.children:
            m.update()
        self.spawn_clock()

    def spawn_clock(self):
        """Check clock interval. Call spawn() when appropriate."""
        if self.timer >= 3000:
            self.spawn(Mobile)
            self.timer = 0

    def spawn(self, mob):
        """Spawn new enemies into the game."""
        new_children = []
        for i in range(random.randint(3, 6)):
            new_children.append(mob((20, 20), (0, 255, 0), self.surface))
        for c in new_children:
            c.rect.center = (random.randint(10, 590), random.randint(10, 590))
        self.children.extend(new_children)

    def damage(self):
        for w in self.player.weapons:
            for s in w.shots:
                for c in self.children:
                    if c.rect.collidepoint(int(s.x / 1000), int(s.y / 1000)):
                        self.children.remove(c)
                        w.shots.remove(s)
                        break