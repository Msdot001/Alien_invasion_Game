import sys
import pygame



class AlienInvasion:
    """Overall class to manage game assest and behavior"""

    def __init__(self):
        """Initialize the game, and create game resourrce"""
        pygame.init()

        self.screen = pygame.display.set((1200, 800))
        pygame.disaplay.set_caption("Alien Invasion By Moshood")


    def run_game(selff):
        """Start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

        

