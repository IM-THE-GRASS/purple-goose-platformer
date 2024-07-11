import pygame
import player
import os
import block
import json
import pymunk
import ui
import level_editor
current_tool = "draw"


def main(level):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    pygame.init()
    space = pymunk.Space()
    space.gravity = (0,0)
    cp = ui.colorpicker(50, 50, 400, 60)
    delete = ui.button(50,150,70,70,"image", os.path.join("images", "delete.png"))
    draw = ui.button(50,250,70,70,"image", os.path.join("images", "draw.png"))
    click = False
    font = pygame.font.SysFont("times new roman", 32, bold=True)
    running = True
    screen = pygame.display.set_mode((1200, 700))
    f = open(level)
    level_data = f.read()
    f.close()
    level_data = json.loads(level_data)
    platforms = []
    clock = pygame.time.Clock()
    current_block = {}
    for box in level_data:
        platforms.append(block.Block(box["color"],box["width"],box["height"],box["x"],box["y"], space))
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
        color = cp.get_color()
        clock.tick(60)
        mouse_pos = pygame.mouse.get_pos() 
        click = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = "down"
                if current_tool == "draw":
                    current_block["start_pos"] = mouse_pos
                    
            if event.type == pygame.MOUSEBUTTONUP:
                click = "up"
                if current_tool == "draw":
                    if current_block:
                        endpos = mouse_pos
                        startpos = current_block["start_pos"]
                        current_block["end_pos"] = endpos
                        width, height, x, y = generate_block(startpos, endpos)
                        platforms.append(block.Block(color,width,height,x,y, space))

                        rec = {"x":x,"y":y,"width":width,"height":height, "color":(color.r,color.g,color.b)}
                        level_data.append(rec)
                        
                        current_block = {}
                elif current_tool == "delete":
                    
                    for bloc in platforms:
                        print({"x":bloc.x,"y":bloc.y,"width":bloc.width,"height":bloc.height, "color":bloc.color})
                        rect = pygame.Rect(bloc.x,bloc.y,bloc.width,bloc.height)
                        if rect.collidepoint(mouse_pos):
                            platforms.remove(bloc)
                            for rec in level_data:
                                if rec == {"x":bloc.x,"y":bloc.y,"width":bloc.width,"height":bloc.height, "color":bloc.color}:
                                    print(rec)
                                    level_data.remove(rec)

        def on_delete(_):        
            level_editor.current_tool = "delete"   
            
        def on_draw(_):
            level_editor.current_tool = "draw"
        f = open(level, "w")
        f.write(json.dumps(level_data))
        f.close()
        # drawing stuff
        screen.fill(BLACK)
        if not "end_pos" in current_block.keys() and "start_pos" in current_block.keys():
            width, height, x, y = generate_block(current_block["start_pos"], mouse_pos)
            s = pygame.Surface((width,height))
            s.set_alpha(128)
            s.fill((255,255,255))
            screen.blit(s, (x,y))
        
        for platform in platforms:
            platform.update(screen)
        cp.update()
        cp.draw(screen)
        delete.draw(on_delete,click,screen,mouse_pos)
        draw.draw(on_draw,click,screen,mouse_pos)
        pygame.display.flip()
        