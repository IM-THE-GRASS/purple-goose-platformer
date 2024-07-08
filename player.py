import pygame
import pymunk
import pymunk.pygame_util
from pymunk.vec2d import Vec2d
pygame.init()
class player():
    def __init__(self, x, y, player_img_path, width, height,space) -> None:
        self.body =  pymunk.Body(100, 1000000000000000000000)
        self.shape = pymunk.Poly(self.body, [(0, 0), (width, 0), (width, height), (0, height)])
        space.add(self.body, self.shape)
        self.x = x
        self.y = y
        self.size = (width, height)
        
        self.img = pygame.image.load(player_img_path).convert_alpha()
        self.img = pygame.transform.scale(self.img, self.size)
        self.r_img = pygame.transform.flip(self.img,True,False)
        self.direction = "left"
        
        self.rect = self.img.get_rect(topleft=(self.x, self.y))
    def update(self, screen):
        self.x = self.body.position.x
        self.y = self.body.position.y
        if self.direction == "left":
            screen.blit(self.img, (self.x, self.y))
        else: 
            screen.blit(self.r_img, (self.x,self.y))
        self.rect = self.img.get_rect(topleft=(self.x, self.y))