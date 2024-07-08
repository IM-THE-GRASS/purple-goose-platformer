import pygame
import player
import os
import block
import json
import pymunk
import pymunk.pygame_util
from pymunk.vec2d import Vec2d


def main(level):
    
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
    space.damping = 0.1
    options = pymunk.pygame_util.DrawOptions(screen)
    space.gravity= (0, 10000)
    player_img = os.path.join("images", "goose.png")
    current_player = player.player(25,25,player_img, 50,50, space)
    current_player.body.color = pygame.Color("pink")
    w = pygame.K_w
    a = pygame.K_a
    s = pygame.K_s
    d = pygame.K_d
    space_key = pygame.K_SPACE
    clock = pygame.time.Clock()
    f = open(level)
    level_data = f.read()
    f.close()
    level_data = json.loads(level_data)
    platforms = []
    for box in level_data:
        platforms.append(block.Block(box["color"],box["width"],box["height"],box["x"],box["y"], space))
    JumpCounter = 999
    print(a)
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = "down"
            if event.type == pygame.MOUSEBUTTONUP:
                click = "up"
            if event.type == pygame.KEYUP:
                if event.key == w:
                    pass
                if event.key == a:
                    
                    current_player.direction = "left"
                if event.key == s:
                    pass
                if event.key == d:
                    
                    current_player.direction = "right"
                if event.key == space_key:
                    current_player.yvelocity = 0
        JumpCounter = JumpCounter + 1
        mouse_pos = pygame.mouse.get_pos()        
        keys_pressed = pygame.key.get_pressed()
        
        if keys_pressed[w]:
            print("asdsdadas")
        if keys_pressed[a]:
            current_player.body.apply_impulse_at_world_point(( -4000, 0), current_player.body.position)
            print("A")
            current_player.direction = "left"
        if keys_pressed[s]:
            pass
        if keys_pressed[d]:
            current_player.body.apply_impulse_at_world_point(( 4000, 0), current_player.body.position)
            current_player.direction = "right"
        if keys_pressed[space_key] and JumpCounter > 100:
            print(JumpCounter)
            current_player.body.apply_impulse_at_world_point(( 0, -251111), current_player.body.position)
            JumpCounter = 1

        screen.fill(BLACK)
        fps = 60
        space.step(1 / fps)
        current_player.update(screen)
        
        for platform in platforms:
            platform.update(screen)
            if platform.rect.collidepoint(current_player.rect.centerx,current_player.rect.bottom  - 5):
                JumpCounter = 999
        #current_player.update(screen)
        pygame.display.flip()