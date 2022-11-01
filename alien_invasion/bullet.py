import pygame
from pygame.sprite import Sprite



class Bullet(Sprite):
    """A class to manage the bullet fired from the ship"""

    def __init__(self, ai_game):
        """Craeting a bullet object at the ship current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.ettings
        self.color = self.settings.bullet_color

        # Creating a bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.react.midtop

        # Store the bullet position as a decimal value
        self.y = float(self.rect.y)


    def update(self):  # The update() method manages the bullet’s position.
        """Move the bullet up the screen"""
        # Update the decimal position of the bullet
        self.y -= self.settings.bullet_speed
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)