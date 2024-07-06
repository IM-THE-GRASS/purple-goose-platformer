import pygame
pygame.init()
class player(pygame.sprite.Sprite):
    def __init__(self, x, y, player_img_path, width, height, color =(255,255,255)) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.color = color
        self.size = (width, height)
        self.yvelocity = 0
        self.xvelocity = 0
        self.player_img = pygame.image.load(player_img_path).convert_alpha()
        self.player_img = pygame.transform.scale(self.player_img, self.size)
        self.rect = self.player_img.get_rect(topleft=(self.x, self.y))
    def update(self, screen):
        self.x = self.x + self.xvelocity
        self.y = self.y + self.yvelocity
        screen.blit(self.player_img, (self.x, self.y))
        self.rect = self.player_img.get_rect(topleft=(self.x, self.y))