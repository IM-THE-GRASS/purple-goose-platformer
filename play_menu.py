import pygame
import os
import ui
import time
import level
import level_editor
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
pygame.init()
click = False
mouse_pos = pygame.mouse.get_pos()
mouse_info = [click, mouse_pos]
running = True
screen = pygame.display.set_mode((1200, 700))
font = pygame.font.SysFont("times new roman", 80, bold=True)
levels = []
menu = ui.menu(click, mouse_pos,screen,(25, 25))
def on_play(lvl):
    
    menu.enabled = False
    print("play")
    level.main(os.path.join("levels", lvl))

for x in os.listdir("levels"):
    if x.endswith(".goose"):
        levels.append(x)
for lvl in levels:
    button = menu.add_button(500, 125,"image",os.path.join('images', 'button.png'),"button", on_play, os.path.join("sounds", "start_game.ogg"), text=lvl)


text_surface = font.render("button", False, BLACK)


def main():
    menu.enabled = True
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
        menu.set_mouse_info(click, mouse_pos)

        
        
        screen.fill(BLACK)
        
        menu.draw()
        #screen.blit(text_surface, (button.rect.topleft[0] + 25, button.rect.topleft[1] + 13))
        pygame.display.flip()