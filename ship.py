import pygame
from settings import Settings 

class Ship:
    # A class to manage the players ship
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Ship settings
        self.settings = ai_game.settings

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # Load the ship and get its rect
        self.image = pygame.image.load("images/ship.bmp")
        self.image = pygame.transform.scale(self.image, (90, 130))
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value of the ships horizontal and vertical position
        self.x = float(self.rect.x)
        self.y = float (self.rect.y)
    
    def update(self):
        if self.moving_right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left:
            self.rect.x -= self.settings.ship_speed 
        if self.moving_up:
            self.rect.y -= self.settings.ship_speed
        if self.moving_down:
            self.rect.y += self.settings.ship_speed

    def blitme(self):
        # Draw the ship to the main screen (self.screen) at its current location
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
