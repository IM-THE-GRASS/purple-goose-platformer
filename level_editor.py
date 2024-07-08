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
    
    def generate_block(startpos, endpos):
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
        return width, height, x, y
    while running:
        clock.tick(60)
        mouse_pos = pygame.mouse.get_pos() 
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
                    startpos = current_block["start_pos"]
                    current_block["end_pos"] = endpos
                    width, height, x, y = generate_block(startpos, endpos)
                    platform = block.Block(WHITE,width,height,x,y)
                    platforms.add(platform)
                    current_block = {}
            
               
            
        screen.fill(BLACK)
        print(not "endpos" in current_block.keys())
        print(current_block.keys())
        if not "end_pos" in current_block.keys() and "start_pos" in current_block.keys():
            print("ADDA")
            width, height, x, y = generate_block(current_block["start_pos"], mouse_pos)
            s = pygame.Surface((width,height))
            s.set_alpha(128)
            s.fill((255,255,255))
            screen.blit(s, (x,y))
                    
        platforms.update()
        platforms.draw(screen)
        pygame.display.flip()