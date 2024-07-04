import pygame
import os
import ui

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
pygame.init()
click = False
mouse_pos = pygame.mouse.get_pos()
mouse_info = [click, mouse_pos]
font = pygame.font.SysFont("times new roman", 32, bold=True)
running = True
screen_width = 700
screen_height = 700
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("goobse")
def on_play():
    print("play")
    pygame.quit()
    
def on_quit():
    print("quit")
    pygame.quit()

def on_settings():
    print("settings")

menu = ui.menu(click, mouse_pos,screen,(25, 25))
menu.add_button(500, 125,"image",os.path.join('images', 'play.png'),"play", on_play)
menu.add_button(500, 125,"image",os.path.join('images', 'settings.png'),"settings", on_play)
menu.add_button(500, 125,"image",os.path.join('images', 'quit.png'),"quit", on_play)
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
    menu.set_mouse_info(click, mouse_pos)

    
    
    screen.fill(BLACK)
    
    #play_button = ui.button(25, 25, 500, 125, "image", image_path=os.path.join('images', 'play.png'))
    #settings_button = ui.button(25, 150, 500, 125, "image", image_path=os.path.join("images", "settings.png"))
    #quit_button = ui.button(25, 275, 500, 125, "image", image_path=os.path.join('images', 'quit.png'))
    
    menu.draw()
    

    #play_button.draw(on_play, click, screen, mouse_pos)
    #settings_button.draw(on_settings, click, screen, mouse_pos)
    #quit_button.draw(on_quit, click, screen, mouse_pos)

    pygame.display.flip()