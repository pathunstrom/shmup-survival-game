__author__ = 'Patrick'

import pygame
from pygame.locals import K_w, K_a, K_s, K_d
from math import cos, sin, atan2, floor


class Player(object):
    """Handle player attributes and weapons fire."""

    def __init__(self, area, surface):
        """Return Player"""
        # References
        self.surface = surface
        self.rect = pygame.Rect(0, 0, 20, 20)
        self.color = (200, 110, 10)
        # Weapons and attacks
        self.weapons = []
        self.equipped = Weapon(area)
        # Movement and Location
        self.x, self.y = area.centerx * 1000, area.centery * 1000
        self.speed = 60

    def move(self, time):
        """Move player"""
        key_state = pygame.key.get_pressed()
        if key_state[K_w]:
            self.y -= self.speed * time
        if key_state[K_a]:
            self.x -= self.speed * time
        if key_state[K_s]:
            self.y += self.speed * time
        if key_state[K_d]:
            self.x += self.speed * time
        self.rect.centerx = self.x / 1000
        self.rect.centery = self.y / 1000
        return None

    def animate(self):
        """Update surface with player location"""
        radius = self.rect.width / 2
        pygame.draw.circle(self.surface, self.color, self.rect.center, radius)
        return None

    def trigger(self, target):
        self.equipped.shoot(self.rect.center, target)

    def update(self, time):
        self.move(time)
        self.equipped.update(self.surface, time)
        self.animate()
        return None


class Bullet(object):
    """Bullet class. Pew pew."""

    def __init__(self, origin, target):
        self.color = (255, 255, 255)
        # Variables to calculate movement
        rise = target[1] - origin[1]
        run = target[0] - origin[0]
        atan = atan2(rise, run)
        self.run = cos(atan)
        self.rise = sin(atan)
        self.x, self.y = origin[0] * 1000, origin[1] * 1000
        self.speed = 200

    def move(self, time):
        delta = time * self.speed
        self.x += delta * self.run
        self.y += delta * self.rise

    def animate(self, surface):
        radius = 2
        x = int(floor(self.x / 1000))
        y = int(floor(self.y /1000))
        z = (x, y)
        pygame.draw.circle(surface, self.color, z, radius)

    def update(self, surface, time):
        self.move(time)
        self.animate(surface)


class Weapon(object):
    """Basic weapon class."""

    def __init__(self, area):
        self.shots = []
        self.wait = 1000
        self.limit = area

    def shoot(self, origin, target):
        self.shots.append(Bullet(origin, target))

    def update(self, surface, time):
        for s in self.shots:
            s.update(surface, time)
            if not self.limit.collidepoint(s.x / 1000, s.y / 1000):
                self.shots.remove(s)