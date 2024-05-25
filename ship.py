import pygame

class Ship:
    # A class to manage the players ship
    def __init__(self, ai_game):
        print(ai_game)
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship and get its rect
        self.image = pygame.image.load("images/ship.bmp")
        self.image = pygame.transform.scale(self.image, (120, 160))
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
    def blitme(self):
        # Draw the ship to the main screen (self.screen) at its current location
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
