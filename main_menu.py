import pygame
import os
import ui
import time
import level
import levels_menu
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
pygame.init()
click = False
mouse_pos = pygame.mouse.get_pos()
mouse_info = [click, mouse_pos]
font = pygame.font.SysFont("times new roman", 54, bold=True)
running = True
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("goobse")


main_menu = ui.menu(click, mouse_pos,screen,(25, 25))
def on_play(_):
    
    main_menu.enabled = False
    print("play")
    level.main("_")

def on_levels(_):
    main_menu.enabled = False
    levels_menu.main()

def on_quit(_):
    time.sleep(0.5)
    pygame.quit()
    quit()
    


main_menu.add_button(500, 125,"image",os.path.join('images', 'play.png'),"play", on_play, os.path.join("sounds", "v"))
main_menu.add_button(500, 125,"image",os.path.join('images', 'levels.png'),"levels", on_levels, os.path.join("sounds", "menu_select.wav"))
main_menu.add_button(500, 125,"image",os.path.join('images', 'quit.png'),"quit", on_quit, os.path.join("sounds", "death.wav"))

def main():
    while running:
        click = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = "down"
            if event.type == pygame.MOUSEBUTTONUP:
                click = "up"
        mouse_pos = pygame.mouse.get_pos()
        main_menu.set_mouse_info(click, mouse_pos)

        
        
        screen.fill(BLACK)
        
        main_menu.draw()

        pygame.display.flip()