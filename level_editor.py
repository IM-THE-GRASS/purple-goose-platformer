import pygame
import player
import os
import block
import json
import pymunk
import ui
import level_editor
import main_menu

def main(level):
    def get_level_data(lvl):
        f = open(level)
        level_data = f.read()
        f.close()
        level_data = json.loads(level_data)
        return level_data
    
    
    # pygame stuff
    BLACK = (0, 0, 0)
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1200, 700))
    
    
    # fisics
    space = pymunk.Space()
    space.gravity = (0,0)
    
    
    #ui 
    ui_rects = []
    colorpicker = ui.colorpicker(50, 50, 400, 60)
    ui_rects.append(colorpicker.rect)
    delete = ui.button(50,150,70,70,"image", os.path.join("images", "delete.png"))
    ui_rects.append(delete.rect)
    draw = ui.button(50,230,70,70,"image", os.path.join("images", "draw.png"))
    ui_rects.append(draw.rect)
    finish_button = ui.button(50,310,70,70,"image", os.path.join("images", "finish.png"))
    ui_rects.append(finish_button.rect)
    pause_button = ui.button(1090, 10, 100,100,"image",os.path.join('images', 'pause.png'),sound_path=os.path.join("sounds", "menu_select.wav"))
    ui_rects.append(pause_button.rect)
    main_menu_button = ui.button(300,341,573,142,"image",image_path=os.path.join('images', 'main menu.png'),sound_path=os.path.join("sounds", "menu_select.wav"))
    #ui_rects.append(main_menu_button.rect)
    quit_button = ui.button(300,490,573,142,"image",image_path=os.path.join('images', 'quit.png'),sound_path=os.path.join("sounds", "menu_select.wav"))
    #ui_rects.append(quit_button.rect)
    
    
    pause_screen = pygame.image.load(os.path.join("images", "paused.png")).convert_alpha()
    # variables to keep track of stuff
    global paused 
    global current_tool
    paused = False
    click = None
    running = True
    current_tool = "draw"
    finish_flag_size = 60
    
    # level data stuff
    level_data = get_level_data(level)
    platforms = []
    flags = []
    current_block = {}
    def load_data():
        for box in level_data:
            if box["type"] == "platform":
                platforms.append(block.Block(box["color"],box["width"],box["height"],box["x"],box["y"], space))
            elif box["type"] == "finish":
                
                flags.append(pygame.Rect(box["x"], box["y"], finish_flag_size, finish_flag_size))
    load_data()
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
    
    def convert_to_level_data(bloc, bloc_type):
        if type(bloc) == block.Block:
            return {"x":bloc.x,"y":bloc.y,"width":bloc.width,"height":bloc.height, "color":bloc.color, "type":bloc_type}
        elif type(bloc) == pygame.Rect:
            return {"x":bloc.x,"y":bloc.y,"width":bloc.width,"height":bloc.height, "color":[0,0,0, 255], "type":bloc_type}
        
    while running:
        current_color = colorpicker.get_color()
        mouse_pos = pygame.mouse.get_pos() 
        click = None
        
        clock.tick(60)
        if any(rect.collidepoint(mouse_pos) for rect in ui_rects):
            touching_ui = True
        else:
            touching_ui = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                level_editor.exit()
                
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = "down"
                if current_tool == "draw" and not touching_ui and not paused:
                    current_block["start_pos"] = mouse_pos
            elif event.type == pygame.MOUSEBUTTONUP:
                click = "up"
                
                if not touching_ui and not paused:
                    if current_tool == "draw":
                        if current_block:
                            
                            endpos = mouse_pos
                            startpos = current_block["start_pos"]
                            current_block["end_pos"] = endpos
                            width, height, x, y = generate_block(startpos, endpos)
                            platforms.append(block.Block(current_color,width,height,x,y, space))
                            
                            rec = {"x":x,"y":y,"width":width,"height":height, "color":tuple(current_color), "type":"platform"}
                            level_data.append(rec)
                            current_block = {}
                            
                    elif current_tool == "delete":
                        for bloc in platforms:
                            rect = pygame.Rect(bloc.x,bloc.y,bloc.width,bloc.height)
                            if rect.collidepoint(mouse_pos):
                                platforms.remove(bloc)
                                for rec in level_data:
                                    if rec == convert_to_level_data(bloc, "platform"):
                                        level_data.remove(rec)
                        for flag in flags:
                            if flag.collidepoint(mouse_pos):
                                flags.remove(flag)
                                for rec in level_data:
                                    new_flag = convert_to_level_data(flag, "finish")
                                    if rec == new_flag:
                                        level_data.remove(new_flag)
                                        
                    elif current_tool == "place_flag":
                        rec = pygame.Rect(mouse_pos[0], mouse_pos[1], finish_flag_size, finish_flag_size)
                        level_data.append(convert_to_level_data(rec, "finish"))
                        flags.append(rec)

        def on_delete(_): 
            level_editor.current_tool = "delete" 
            
        def on_draw(_):
            level_editor.current_tool = "draw"
        
        def on_place_finish(_):
            level_editor.current_tool = "place_flag"
            
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
        for flag in flags:
            image = pygame.image.load(os.path.join("images", "flag.png")).convert_alpha()
            screen.blit(image, flag.topleft)
        colorpicker.update()
        colorpicker.draw(screen)
        delete.draw(on_delete,click,screen,mouse_pos)
        finish_button.draw(on_place_finish,click,screen,mouse_pos)
        draw.draw(on_draw,click,screen,mouse_pos)
        if paused:
            screen.blit(pause_screen, (0,0)) 
            main_menu_button.draw(open_menu, click, screen, mouse_pos)
            quit_button.draw(exit, click, screen, mouse_pos)
        else:
            pause_button.draw(level_editor.pause, click, screen, mouse_pos)
        pygame.display.flip()
            
        
def pause(_ = None):
    level_editor.paused = True
def open_menu(_ = None):
        level_editor.running = False
        main_menu.main()  
def exit(_ = None):
    pygame.quit()
    quit()