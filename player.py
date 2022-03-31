import pygame

import config


class Player():
    def __init__(self, screen):
        self.screen = screen
        self.position = round(config.SCREEN_WIDTH / 2)
        self.image = pygame.image.load("imgs/player.png")
        self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))

    def render(self):
        self.rect = pygame.Rect(self.position, config.SCREEN_HEIGHT - config.SCALE, config.SCALE, config.SCALE)
        self.screen.blit(self.image, self.rect)