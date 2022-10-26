from telnetlib import AO
import pygame


class Ship:
    """A class to manipulate the ship"""

    def __init__(self, ai_game):
        """initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()                # allows us to place the ship in the correct location on the screen.

        # load the ship image and get its react

        self.image = pygame.image.load(r"C:\Users\masud\Documents\Alien_invasion_Game\alien_invasion\Image\ship1.bmp")
        self.rect = self.image.get_rect()

        # start each new screen at the buttom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)


        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag"""
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x


    def blitme(self):
        """Draw the screen at its current location"""
        self.screen.blit(self.image, self.rect)


