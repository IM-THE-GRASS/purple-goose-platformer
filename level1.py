import pygame
import player
import os
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
pygame.init()
click = False
mouse_pos = pygame.mouse.get_pos()
mouse_info = [click, mouse_pos]
font = pygame.font.SysFont("times new roman", 32, bold=True)
running = True
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("goobse")

player_img = os.path.join("images", "goose.png")
theplayer = player.player(25,25,player_img)

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
        print("sfhaiudfhiu")
        
        
        screen.fill(BLACK)
        theplayer.draw(screen)
        pygame.display.flip()