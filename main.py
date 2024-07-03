import pygame
import os
click = False
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
pygame.init()
font = pygame.font.SysFont("times new roman", 32, bold=True)
running = True
screen_width = 700
screen_height = 700
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("goobse")

class button:   
    def __init__(self, centerx, centery, width, height, type = "text", text = "", image_path= "", bg_color = WHITE, text_color = BLACK):
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
    def draw(self, click_function):
        pygame.draw.rect(screen, self.bg_color, self.rect)
        if self.type == "text":
            surface = font.render(self.text, False, BLACK)
        elif self.type == "image":
            surface = pygame.image.load(self.image_path)
            surface = pygame.transform.scale(surface, (self.width,self.height))
        screen.blit(surface, (self.x, self.y))
        if self.rect.collidepoint(mouse_x, mouse_y) and click:
            click_function()
            

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True
        if event.type == pygame.MOUSEBUTTONUP:
            click = False
    mouse_x, mouse_y = pygame.mouse.get_pos()

    def on_play():
        print("play")
        pygame.quit()
        
    def on_quit():
        print("quit")
        pygame.quit()
    
    
    play_button = button(25, 25, 500, 125, "image", image_path=os.path.join('images', 'play.png'))
    quit_button = button(25, 150, 500, 125, "image", image_path=os.path.join('images', 'quit.png'))
    



    play_button.draw(on_play)
    quit_button.draw(on_quit)

    pygame.display.flip()