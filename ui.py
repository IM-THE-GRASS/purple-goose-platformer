import pygame
import os
pygame.init()
font = pygame.font.SysFont("times new roman", 32, bold=True)
BLACK = (0,0,0)
WHITE = (255,255,255)
class button:   
    def __init__(self, centerx, centery, width, height, type = "text", text = "", image_path= "", bg_color = WHITE, text_color = BLACK):
        pygame.init()
        self.x = centerx 
        self.y = centery
        self.width = width
        self.height = height
        self.text = text
        self.bg_color = bg_color
        self.text_color = text_color
        self.type = type
        self.image_path = image_path
        
        self.rect = pygame.Rect(0,0,0,0)
        self.rect.center = (centerx,centery)
        self.rect.width = width
        self.rect.height = height
    def draw(self, click_function, click_value, screen, mouse_pos):
        pygame.draw.rect(screen, self.bg_color, self.rect)
        if self.type == "text":
            surface = font.render(self.text, False, BLACK)
        elif self.type == "image":
            surface = pygame.image.load(self.image_path)
            
            surface = pygame.transform.scale(surface, (self.width,self.height))
            surface.convert_alpha()
            surface.set_colorkey((255,255,255))
        if self.rect.collidepoint(mouse_pos) and click_value:
            click_function()
        screen.blit(surface, (self.x, self.y))
        return surface, (self.x, self.y)