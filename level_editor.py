import pygame
import player
import os
import block
import json
import pymunk
import ui
import level_editor
import main_menu
current_tool = "draw"


def main(level):
    def get_level_data(lvl):
        f = open(level)
        level_data = f.read()
        f.close()
        level_data = json.loads(level_data)
        return level_data
    def open_menu(_ = None):
        level_editor.running = False
        main_menu.main()  
    def exit(_ = None):
        pygame.quit()
        quit()
    
    # pygame stuff
    BLACK = (0, 0, 0)
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1200, 700))
    
    
    # fisics
    space = pymunk.Space()
    space.gravity = (0,0)
    
    
    #ui 
    cp = ui.colorpicker(50, 50, 400, 60)
    delete = ui.button(50,150,70,70,"image", os.path.join("images", "delete.png"))
    draw = ui.button(50,230,70,70,"image", os.path.join("images", "draw.png"))
    finish_button = ui.button(50,310,70,70,"image", os.path.join("images", "finish.png"))
    pause_screen = pygame.image.load(os.path.join("images", "paused.png")).convert_alpha()
    pause_button = ui.button(1090, 10, 100,100,"image",os.path.join('images', 'pause.png'),sound_path=os.path.join("sounds", "menu_select.wav"))
    main_menu_button = ui.button(300,341,573,142,"image",image_path=os.path.join('images', 'main menu.png'),sound_path=os.path.join("sounds", "menu_select.wav"))
    quit_button = ui.button(300,490,573,142,"image",image_path=os.path.join('images', 'quit.png'),sound_path=os.path.join("sounds", "menu_select.wav"))
    
    # variables to keep track of stuff
    global paused 
    paused = False
    click = False
    running = True
    
    
    # level data stuff
    level_data = get_level_data(level)
    platforms = []
    current_block = {}
    def load_data():
        for box in level_data:
            platforms.append(block.Block(box["color"],box["width"],box["height"],box["x"],box["y"], space))
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
    
    while running:
        print(current_block)
        current_color = cp.get_color()
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
                    print("AAA")
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
                                if rec == {"x":bloc.x,"y":bloc.y,"width":bloc.width,"height":bloc.height, "color":bloc.color, "type":"platform"}:
                                    print(rec)
                                    level_data.remove(rec)

        def on_delete(_):        
            level_editor.current_tool = "delete"   
            
        def on_draw(_):
            level_editor.current_tool = "draw"
        
        def on_place_finish(_):
            print("sajdjsaj")
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
        finish_button.draw(on_place_finish,click,screen,mouse_pos)
        draw.draw(on_draw,click,screen,mouse_pos)
        
        if not paused:
            pause_button.draw(level_editor.pause, click, screen, mouse_pos)
        if paused:
            screen.blit(pause_screen, (0,0)) 
            main_menu_button.draw(open_menu, click, screen, mouse_pos)
            quit_button.draw(exit, click, screen, mouse_pos)
        pygame.display.flip()
            
        
def pause(_ = None):
    level_editor.paused = True