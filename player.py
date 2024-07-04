import pygame
class player:
    def __init__(self, x, y, player_img_path) -> None:
        self.x = x
        self.y = y
        self.yvelocity = 0
        self.xvelocity = 0
        self.player_img = pygame.image.load(player_img_path).convert_alpha()
        self.rect = self.player_img.get_rect(topleft=(self.x, self.y))
    def draw(self, screen):
        self.x = self.x + self.xvelocity
        self.y = self.y + self.yvelocity
        screen.blit(self.player_img, (self.x, self.y))
        self.rect = self.player_img.get_rect(topleft=(self.x, self.y))