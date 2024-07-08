import pygame
import player
import os
import block

def main(level):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    pygame.init()
    click = False
    font = pygame.font.SysFont("times new roman", 32, bold=True)
    running = True
    screen = pygame.display.set_mode((1200, 700))

    platforms = pygame.sprite.Group()
    clock = pygame.time.Clock()
    current_block = {}
    while running:
        clock.tick(60)
        click = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                current_block["start_pos"] = mouse_pos
            if event.type == pygame.MOUSEBUTTONUP:
                if current_block:
                    endpos = mouse_pos
                    current_block["end_pos"] = endpos
                    startpos = current_block["start_pos"]
                    width =  endpos[0] - startpos[0]
                    height = endpos[1] - startpos[1]
                    x = startpos[0]
                    y = startpos[1]
                    if width < 0:
                        x = x + width
                        width = width * -1
                        
                    if height < 0:
                        y = y + height
                        height = height * -1
                        
                        
                    
                    
                    platform = block.Block(WHITE,width,height,x,y)
                    platforms.add(platform)
            
        mouse_pos = pygame.mouse.get_pos()        
            
        screen.fill(BLACK)

        
        
        platforms.update()
        platforms.draw(screen)
        pygame.display.flip()