import pygame
import pymunk
import pymunk.pygame_util
from pymunk.vec2d import Vec2d

class Block():

    def __init__(self, color, width, height, x, y, space):
        self.body =  pymunk.Body(10, 1000000000000000000000, pymunk.Body.STATIC)
        self.body.position =Vec2d(x,y)
        self.shape = pymunk.Poly(self.body, [(0, 0), (width, 0), (width, height), (0, height)])
        space.add(self.body, self.shape)
        
        self.pos = (x,y)
        self.image = pygame.Surface([width, height])
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect()
    def update(self, screen):
        self.x = self.body.position.x
        self.y = self.body.position.y
        self.rect.topleft = self.pos
        screen.blit(self.image, (self.x, self.y))