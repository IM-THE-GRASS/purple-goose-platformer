import pygame


class Block(pygame.sprite.Sprite):

    def __init__(self, color, width, height, left, top):
       pygame.sprite.Sprite.__init__(self)
       self.pos = (left,top)
       self.image = pygame.Surface([width, height])
       self.color = color
       self.image.fill(color)
       self.rect = self.image.get_rect()
    def update(self):
        self.rect.topleft = self.pos