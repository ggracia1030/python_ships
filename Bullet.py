import pygame

from pygame.sprite import Sprite
from Settings import Settings
from Ship import Ship


class Bullet(Sprite):
    """Class to manage bullets fired from the ship"""
    def __init__(self, settings, screen, ship):
        """Create a bullet at the ship's position"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(ship.rect.centerx, ship.rect.top,  settings.bullet_width, settings.bullet_height)

    def update(self):
        self.rect.centery -= 1

    def draw(self):
        """Draw the ship at its current location."""
        pygame.draw.rect(self.screen, (255, 100, 50), self.rect)
