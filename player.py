import pygame
from constants import *


class Player():
    def __init__(self):
        self.width = BLOCK_SIZE
        self.x = GAME_WIDTH // 2


    def update(self):
        pass

    def move_right(self):
        if self.x < GAME_WIDTH - self.width * 2:
            self.x += self.width


    def move_left(self):
        if self.x > self.width:
            self.x -= self.width


    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), (self.x, GAME_HEIGHT - self.width, self.width, self.width))
