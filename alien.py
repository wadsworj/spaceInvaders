import pygame

import config


class Alien():
    def __init__(self, screen, x_position, y_position, speed):
        self.screen = screen
        self.position = [x_position, y_position]
        self.image = pygame.image.load("imgs/alien.png")
        self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))
        self.speed = speed
        self.killed = False

    def render(self):
        self.rect = pygame.Rect(self.position[0], self.position[1], round(config.SCALE), round(config.SCALE))
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.position[0] = self.position[0] + self.speed

    def drop(self):
        self.position[1] = self.position[1] + config.SCALE
        self.speed = -self.speed

    def collide(self, x, y):
        if self.killed:
            return False

        if x <= (self.position[0] + config.SCALE) and x > self.position[0] and y <= (self.position[1] + config.SCALE) and y > self.position[1]:
            return True
        return False