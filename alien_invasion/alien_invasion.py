import sys
import pygame
from settings import Settings



class AlienInvasion:
    """Overall class to manage game assest and behavior"""

    def __init__(self):
        """Initialize the game, and create game resourrce"""
        pygame.init()
        self.settings = Settings()
        """
        The object we assigned to self.screen is called a surface.
        A surface in Pygame is a part of the screen where a game element can be displayed
        In this case, Game element is an alien or a ship,
        """

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))              # setting background screen with a dimension of 1200 * 800         
        pygame.display.set_caption("Alien Invasion By Moshood")


    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse event
            for event in pygame.event.get():        # An event is an action that the user performs while playing the game, such as pressing a key or moving the mouse.
                if event.type == pygame.QUIT:
                    """sys module to exit the game when the player quits."""
                    sys.exit()

            # redrawn thew screen during each pass throught the loop
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == "__main__":
    #Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
