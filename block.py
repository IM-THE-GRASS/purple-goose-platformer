import pygame


class Block(pygame.sprite.Sprite):

    def __init__(self, color, width, height, centerx, centery):
       pygame.sprite.Sprite.__init__(self)
       self.pos = (centerx,centery)
       self.image = pygame.Surface([width, height])
       self.color = color
       self.rect = self.image.get_rect(centerx = centerx, centery = centery)
       self.image.fill(color)
    def update(self, screen):
        pygame.Surface.blit(screen, self.image, self.pos)