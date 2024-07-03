import pygame
import os
import ui
click = False
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
pygame.init()
font = pygame.font.SysFont("times new roman", 32, bold=True)
running = True
screen_width = 700
screen_height = 700
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("goobse")


            

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True
        if event.type == pygame.MOUSEBUTTONUP:
            click = False
    mouse_pos = pygame.mouse.get_pos()

    def on_play():
        print("play")
        pygame.quit()
        
    def on_quit():
        print("quit")
        pygame.quit()
    
    def on_settings():
        print("settings")
    
    screen.fill(BLACK)
    
    play_button = ui.button(25, 25, 500, 125, "image", image_path=os.path.join('images', 'play.png'))
    settings_button = ui.button(25, 150, 500, 125, "image", image_path=os.path.join("images", "settings.png"))
    quit_button = ui.button(25, 275, 500, 125, "image", image_path=os.path.join('images', 'quit.png'))
    


    play_button.draw(on_play, click, screen, mouse_pos)
    settings_button.draw(on_settings, click, screen, mouse_pos)
    quit_button.draw(on_quit, click, screen, mouse_pos)

    pygame.display.flip()