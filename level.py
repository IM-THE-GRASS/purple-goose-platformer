import pygame
import player
import os
import block
import json
import pymunk
import pymunk.pygame_util
from pymunk.vec2d import Vec2d
import ui
import main_menu
import level as lvl



def main(level):
    global paused
    paused = False
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
    space = pymunk.Space()
    space.damping = 0.01 
    options = pymunk.pygame_util.DrawOptions(screen)
    space.gravity= (0, 10000)
    player_img = os.path.join("images", "goose.png")
    current_player = player.player(25,25,player_img, 50,50, space)
    current_player.body.color = pygame.Color("pink")
    w = pygame.K_w
    a = pygame.K_a
    s = pygame.K_s
    d = pygame.K_d
    death_screen = pygame.image.load(os.path.join("images", "die.png")).convert_alpha()
    pause_screen = pygame.image.load(os.path.join("images", "paused.png")).convert_alpha()
    winner_screen = pygame.image.load(os.path.join("images", "winner.png")).convert_alpha()
    jump_enabled = True
    jump_counter = 0 
    jump_cooldown = 10
    dash_counter = 0
    dash_cooldown = 50
    dash_enabled = True
    space_key = pygame.K_SPACE
    winner = False
    clock = pygame.time.Clock()
    f = open(level)
    level_data = f.read()
    f.close()
    level_data = json.loads(level_data)
    platforms = []
    flags = []
    def menu(_ = None):
        lvl.running = False
        main_menu.main()
        
    def end(_ = None):
        pygame.quit()
        quit()
    def draw_menu(bg):
        screen.blit(bg, (0,0))
        main_menu_button.draw(menu, click, screen, mouse_pos)
        quit_button.draw(end, click, screen, mouse_pos)
    flag_size = 60
    pause_button = ui.button(1090, 10, 100,100,"image",os.path.join('images', 'pause.png'),sound_path=os.path.join("sounds", "menu_select.wav"))
    main_menu_button = ui.button(300,341,573,142,"image",image_path=os.path.join('images', 'main menu.png'),sound_path=os.path.join("sounds", "menu_select.wav"))
    quit_button = ui.button(300,490,573,142,"image",image_path=os.path.join('images', 'quit.png'),sound_path=os.path.join("sounds", "menu_select.wav"))
    for box in level_data:
        if box["type"] == "platform":
            platforms.append(block.Block(box["color"],box["width"],box["height"],box["x"],box["y"], space))
        elif box["type"] == "finish":
            flags.append(pygame.Rect(box["x"], box["y"], flag_size, flag_size))
    while running:
        clock.tick(60)
        click = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = "down"
            if event.type == pygame.MOUSEBUTTONUP:
                click = "up"
                if dash_enabled:
                    if current_player.direction == "right":
                        current_player.body.apply_force_at_world_point(( 9999999, -6000000), current_player.body.position)
                    if current_player.direction == "left":
                        current_player.body.apply_force_at_world_point(( -9999999, -6000000), current_player.body.position)
                    dash_enabled = False
                    dash_counter = 0
            if event.type == pygame.KEYUP:
                if event.key == a and not current_player.is_dead:
                    current_player.direction = "left"
                if event.key == d and not current_player.is_dead:
                    current_player.direction = "right"
        if dash_counter > dash_cooldown:
            dash_enabled = True
        mouse_pos = pygame.mouse.get_pos()     
        keys_pressed = pygame.key.get_pressed()
        dash_counter+=1
        jump_counter+=1
        if not current_player.is_dead:
            if keys_pressed[w]:
                pass
            if keys_pressed[a]:
                current_player.body.apply_impulse_at_world_point(( -8000, 0), current_player.body.position)
                current_player.direction = "left"
            if keys_pressed[s]:
                pass
            if keys_pressed[d]:
                current_player.body.apply_impulse_at_world_point(( 8000, 0), current_player.body.position)
                current_player.direction = "right"
            if keys_pressed[space_key] and jump_enabled and jump_counter > jump_cooldown:
                pygame.mixer.Sound(os.path.join("sounds", "jump.wav")).play()
                current_player.body.apply_impulse_at_world_point(( 0, -251111), current_player.body.position)
                jump_enabled = False
                jump_counter = 0
        if current_player.y > screen.get_height():
            current_player.is_dead = True

        screen.fill(BLACK)
        fps = 60
        space.step(1 / fps)
        current_player.update(screen)
        for platform in platforms:
            platform.update(screen)
            player_bottom = current_player.rect.centerx,current_player.rect.bottom
            player_right = current_player.rect.right,current_player.rect.centery
            player_left = current_player.rect.left,current_player.rect.centery
            if platform.rect.collidepoint(player_bottom) or platform.rect.collidepoint(player_right) or platform.rect.collidepoint(player_left):
                jump_enabled = True
        for flag in flags:
            image = pygame.image.load(os.path.join("images", "flag.png")).convert_alpha()
            screen.blit(image, flag.topleft)
        if current_player.rect.collidelist(flags) > -1:
            winner = True
        if not current_player.is_dead and not paused:
            pause_button.draw(lvl.pause, click, screen, mouse_pos)
        if current_player.is_dead:
            draw_menu(death_screen)
        elif paused:
            draw_menu(pause_screen)
        elif winner:
            draw_menu(winner_screen)
        #current_player.update(screen)
        pygame.display.flip()

def pause(_ = None):
    lvl.paused = True