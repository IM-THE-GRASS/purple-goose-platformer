import pygame
class player:
    def __init__(self, x, y, player_img_path) -> None:
        self.x = x
        self.y = y
        self.player_img = pygame.image.load(player_img_path).convert_alpha()
    def draw(self, screen):
        screen.blit(self.player_img, (self.x, self.y))