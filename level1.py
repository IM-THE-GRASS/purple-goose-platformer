import pygame
import player
import os
import block

def main():
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
    gravity_enabled = True
    gravity = 1
    movement_speed = 5
    jump_height = 15
    player_img = os.path.join("images", "goose.png")
    current_player = player.player(25,25,player_img, 50,50)

    current_player.yvelocity = 0
    w = pygame.K_w
    a = pygame.K_a
    s = pygame.K_s
    d = pygame.K_d
    platforms = pygame.sprite.Group()
    space = pygame.K_SPACE
    clock = pygame.time.Clock()
    platform = block.Block(WHITE, 500, 50 ,0, 500)
    platforms.add(platform)
    JumpCounter = 999
    print(a)
    while running:
        print(current_player.xvelocity, current_player.yvelocity )
        clock.tick(60)
        if gravity_enabled:current_player.yvelocity = current_player.yvelocity + gravity
        click = None
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
                    current_player.xvelocity = current_player.xvelocity + movement_speed
                    current_player.direction = "left"
                if event.key == s:
                    pass
                if event.key == d:
                    current_player.xvelocity = current_player.xvelocity - movement_speed
                    current_player.direction = "right"
                if event.key == space:
                    current_player.yvelocity = 0
        JumpCounter = JumpCounter + 1
        mouse_pos = pygame.mouse.get_pos()        
        keys_pressed = pygame.key.get_pressed()
        
        if keys_pressed[w]:
            print("asdsdadas")
        if keys_pressed[a]:
            current_player.xvelocity = -movement_speed
            current_player.direction = "left"
        if keys_pressed[s]:
            pass
        if keys_pressed[d]:
            current_player.xvelocity = movement_speed
            current_player.direction = "right"
        if keys_pressed[space] and JumpCounter > 200:
            JumpCounter = 1
            current_player.yvelocity = gravity - jump_height
            
        screen.fill(BLACK)
        
        
        spritecollided = pygame.sprite.spritecollideany(current_player, platforms)
        if spritecollided != None:
            gravity_enabled = False
            print(spritecollided)
            new_pos = None
            right = (current_player.rect.right, current_player.y)
            left = (current_player.rect.left, current_player.y)
            bottom = (current_player.x, current_player.rect.bottom)
            if spritecollided.rect.collidepoint(bottom):
                print(spritecollided.rect.top - current_player.rect.height)
                new_pos=(current_player.x, spritecollided.rect.top - current_player.rect.height)
            if spritecollided.rect.collidepoint(left):
                print(spritecollided.rect.top - current_player.rect.height)
                new_pos=(spritecollided.rect.right + current_player.rect.width, current_player.y)
                new_pos = (25,25)
            #if spritecollided.rect.collidepoint(right):
            #    print(spritecollided.rect.top - current_player.rect.height)
            #    new_pos=(current_player.x, spritecollided.rect.top - current_player.rect.height)
            
            if new_pos: current_player.y = new_pos[1]
            #current_player.mobile = False
            JumpCounter = 999
            if current_player.yvelocity > 0:
                
                current_player.yvelocity = 0
        else:
            gravity_enabled = True
        current_player.update(screen)
        platforms.update()
        platforms.draw(screen)
        #current_player.update(screen)
        pygame.display.flip()