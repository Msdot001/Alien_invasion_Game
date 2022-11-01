import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet 

"""
The object we assigned to self.screen is called a surface.
A surface in Pygame is a part of the screen where a game element can be displayed
In this case, Game element is an alien or a ship,

- Refactoring simplifies the structure of the code youve already written, making it easier to build on.
- A helper method does work inside a class but isnt meant to be called through an instance. 
-  In Python, a single leading underscore indicates a helper method.

The run_game() is splitted into two helper method (_check_event() and _update_screen())

"""


class AlienInvasion:
    """Overall class to manage game assest and behavior"""

    def __init__(self):
        """Initialize the game, and create game resource"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))              # setting background screen with a dimension of 1200 * 800    
        pygame.display.set_caption("Alien Invasion By Moshood")
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()


    def run_game(self):             # run_game was refractor into _check_events() and _update_screen() method                                     
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()            
            self._update_screen()

    def _check_events(self):
        """Response to keypresses and mouse events"""
        for event in pygame.event.get():       
            if event.type == pygame.QUIT:                   # to quit the game once quit buttom is pressed
                sys.exit()
            elif event.type == pygame.KEYDOWN:             # Controll the movement of the ship
                self._check_keydown_events(event)                         
            elif event.type == pygame.KEYUP:               # Controll the movement of the ship
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):                 # This is a refactor from _check_events()
        """Respond to Keypresses"""
        if event.key == pygame.K_RIGHT:                     # pressing the key down set the moving right TRUE
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:                    
            self.ship.moving_left = True 
        elif event.key == pygame.K_q:                       #Another option of quitting the game 
            sys.exit()   
        elif event.key ==pygame.K_SPACE:                    # To fire bullet
            self._fire_bullet()

    def _check_keyup_events(self, event):               # This is a refactor from _check_events()
        if event.key == pygame.K_RIGHT:                 # releasing the key set the moving right False
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)    # The add() method is similar to append(), but it’s a method that’s written specifically for Pygame groups.


    def _update_screen(self):
       """Update images on the screen, and flip to the new screen.""" 
       self.screen.fill(self.settings.bg_color)
       self.ship.blitme()

       for bullet in self.bullets.sprites():
            bullet.draw_bullet()
       # Make the most recently drawn screen visible
       pygame.display.flip()
            

if __name__ == "__main__":
    #Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
