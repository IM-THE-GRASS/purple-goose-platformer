import pygame
pygame.init()
class player(pygame.sprite.Sprite):
    def __init__(self, x, y, player_img_path, width, height, color =(255,255,255)) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.color = color
        self.size = (width, height)
        self.mobile = True
        self.yvelocity = 0
        self.xvelocity = 0
        self.direction = "left"
        self.l_img = pygame.image.load(player_img_path).convert_alpha()
        self.l_img = pygame.transform.scale(self.l_img, self.size)
        self.r_img = pygame.transform.flip(self.l_img,True,False)
        self.rect = self.l_img.get_rect(topleft=(self.x, self.y))
    def update(self, screen):
        if self.mobile:
            self.x = self.x + self.xvelocity
            self.y = self.y + self.yvelocity
        if self.direction == "left":
            screen.blit(self.l_img, (self.x, self.y))
        else: 
            screen.blit(self.r_img, (self.x,self.y))
        self.rect = self.l_img.get_rect(topleft=(self.x, self.y))