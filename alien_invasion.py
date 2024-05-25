import pygame
import sys
from settings import Settings
from ship import Ship

class MainGame():
    def __init__(self):
        # Initialise the game and specify game resources
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        
    def run_game(self):
        # Start the main loop for the game
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()
            
    def _check_events(self):
        # Watch for keyboard and mouse events as user input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit 
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        # Move the ship to the right
                        self.ship.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        # Move the ship to the left
                        self.ship.moving_left = True
                    elif event.key == pygame.K_UP:
                        self.ship.moving_up = True
                    elif event.key == pygame.K_DOWN:
                        self.ship.moving_down = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        # Move the ship to the right
                        self.ship.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        # Move the ship to the left
                        self.ship.moving_left = False
                    elif event.key == pygame.K_UP:
                        # Move the ship up (Forward)
                        self.ship.moving_up = False
                    elif event.key == pygame.K_DOWN:
                        # Move the ship down (Reverse)
                        self.ship.moving_down = False

    
    def _update_screen(self):
        # Redraw the screen during each pass through the loop to maintain bg color
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()            
        
        # Make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == "__main__":
    # Make a game instance and run the game
    main_game = MainGame()
    main_game.run_game()



