import sys
import pygame
from settings import Settings
from ship import Ship



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

        self.ship = Ship(self)

    """
      - Refactoring simplifies the structure of the code youve already written, making it easier to build on.
      - A helper method does work inside a class but isnt meant to be called through an instance. 
      -  In Python, a single leading underscore indicates a helper method.

      The run_game() is splitted into two helper method (_check_event() and _update_screen())

    """  

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_event()
            self._update_screen()

    def _check_events(self):
        """Response to keypresses and mouse events"""
        for event in pygame.event.get():       
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
       """Updqate images on the screen, and flip to the new screen.""" 
       self.screen.fill(self.settings.bg_color)
       self.ship.blitme()
       # Make the most recently drawn screen visible
       pygame.display.flip()
            

if __name__ == "__main__":
    #Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
