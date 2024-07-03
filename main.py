import pygame
import  time
click = False
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
pygame.init()
font = pygame.font.SysFont("times new roman", 32)
running = True
screen_width = 700
screen_height = 700
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("goobse")

class button:   
    def __init__(self, centerx, centery, width, height, text, bg_color = WHITE, text_color = BLACK):
        self.x = centerx 
        self.y = centery
        self.width = width
        self.height = height
        self.text = text
        
        self.rect = pygame.rect(0,0,0,0)
        self.rect.center = (centerx,centery)
        self.rect.width = width
        self.rect.height = height
    def draw(self, text, x, y):
        text_surface = font.render(text, True, BLACK)
        screen.blit(text_surface, (x - text_surface.get_width() / 2, y - text_surface.get_height() / 2))

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

    play_button = button(50, 100, 200, 50)
    quit_button = button(50, 200, 200, 50)

    if play_button.rect.collidepoint(mouse_x, mouse_y):
        if click:
            running = False

    if quit_button.rect.collidepoint(mouse_x, mouse_y):
        if click:
            running = False
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, play_button_rect)
    draw_text("Play Game", play_button_rect.centerx, play_button_rect.centery)

    pygame.draw.rect(screen, WHITE, quit_button_rect)
    draw_text("Quit", quit_button_rect.centerx, quit_button_rect.centery)

    pygame.display.flip()