import pygame
import os
pygame.init()
font = pygame.font.SysFont("times new roman", 24, bold=True)
BLACK = (0,0,0)
WHITE = (255,255,255)
class colorpicker:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.image = pygame.image.load(os.path.join("images", "colors.png"))
        self.image = pygame.transform.scale(self.image, (w,h / 3))
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.circle_rad = h/2
        self.pwidth = w-self.circle_rad*2
        self.clicked = False
        self.p = 0

    def get_color(self):
        color = pygame.Color(0)
        color.hsla = (int(self.p * self.pwidth), 100, 50, 100)
        return color

    def update(self):
        moude_buttons = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        if moude_buttons[0] and self.rect.collidepoint(mouse_pos):
            self.clicked =  True
            self.p = (mouse_pos[0] - self.rect.x - self.circle_rad) / self.pwidth
            self.p = (max(0, min(self.p, 1)))
        else:self.clicked = False

    def draw(self, screen):
        screen.blit(self.image, (self.x,self.y + (self.h/ 2) - 8))
        center = self.rect.left + self.circle_rad + self.p * self.pwidth, self.rect.centery
        pygame.draw.circle(screen, self.get_color(), center, self.circle_rad)
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
            if self.sound_path:
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