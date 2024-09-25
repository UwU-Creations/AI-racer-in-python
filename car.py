import pygame
from constants import *
import random
class Car(object):


    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = BLOCK_SIZE
        self.speed = 5
        self.score = 0


    def update(self):
        self.y += self.speed
        if self.y > GAME_HEIGHT:
            self.reset()


    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, self.width, self.width))



    def reset(self):

        self.y = random.randint(self.width, GAME_WIDTH) * -1
        self.x = random.randint(0, GAME_WIDTH)
        self.score += 1
