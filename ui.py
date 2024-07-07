import pygame
import os
pygame.init()
font = pygame.font.SysFont("times new roman", 24, bold=True)
BLACK = (0,0,0)
WHITE = (255,255,255)

class button:   
    def __init__(self, centerx, centery, width, height, type = "text",image_path= "", text = None, text_color = BLACK, sound_path = None):
        pygame.init()
        self.text_padding = 25
        self.x = centerx 
        self.y = centery
        self.width = width
        self.height = height
        self.text = text
        self.text_color = text_color
        self.type = type
        self.image_path = image_path
        self.sound_path = sound_path
        
        self.rect = pygame.Rect(0,0,0,0)
        self.rect.center = (centerx,centery)
        self.rect.width = width
        self.rect.height = height
    def draw(self, click_function, click_value, screen, mouse_pos):
        ogwidth = self.width
        ogheight = self.height
        if self.type == "text":
            surface = font.render(self.text, False, BLACK)
        elif self.type == "image":
            surface = pygame.image.load(self.image_path).convert_alpha()
            surface = pygame.transform.scale(surface, (self.width,self.height))
        if self.text and not self.type == "text":
            text_surf = font.render(self.text, False, BLACK)
            text_surf = pygame.transform.scale(text_surf, (self.width - (2 * self.text_padding),self.height - (2 * self.text_padding)))
        else:
            text_surf = None
        if self.rect.collidepoint(mouse_pos) and click_value == "up":
            sfx = pygame.mixer.Sound(self.sound_path)
            sfx.play()
            click_function(self.text)
        elif self.rect.collidepoint(mouse_pos) and click_value == None:
            if self.width == ogwidth and self.height == ogheight: 
                surface = pygame.transform.scale(surface, (self.width * 1.1, self.height* 1.1))
                if text_surf:
                    text_surf = pygame.transform.scale(text_surf, ((self.width  - (2 * self.text_padding)) * 1.1, (self.height  - (2 * self.text_padding)) * 1.1))
        elif self.rect.collidepoint(mouse_pos) == False and click_value == None:
            self.width = ogwidth
            self.height = ogheight
        screen.blit(surface, (self.x, self.y))
        if text_surf:
            screen.blit(text_surf, (self.x + self.text_padding, self.y + self.text_padding))
        return surface, (self.x, self.y)
class menu:
    def __init__(self, mouse_down, mouse_pos, screen, starting_pos):
        self.enabled = True
        self.mouse_pos = mouse_pos
        self.mouse_down = mouse_down
        self.screen = screen
        self.bg = None
        self.gap = 125
        self.starting_pos = starting_pos
        self.buttons = []
    
    def add_button(self, width, height, type, path, name, on_click, sound_path = None, text = None):
        if not self.enabled:
            return
        the_button = button(self.starting_pos[0],self.starting_pos[1] + self.gap * len(self.buttons), width, height, type, path, sound_path=sound_path, text=text)
        self.buttons.append({"button": the_button, "on_click":on_click, "name": name})
        return the_button
    def remove_button(self):
        pass
    def set_mouse_info(self, mouse_down, mouse_pos):
        if not self.enabled:
            return
        self.mouse_down = mouse_down
        self.mouse_pos = mouse_pos
    def draw(self):
        if not self.enabled:
            return
        for thebutton in self.buttons:
            thebutton["button"].draw(thebutton["on_click"], self.mouse_down, self.screen, self.mouse_pos)