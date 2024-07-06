import pygame
import player
import os
import block
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
gravity = 2
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
def main():
    platform = block.Block(WHITE, 500, 50 ,0, 500)
    platforms.add(platform)
    JumpCounter = 999
    print(a)
    while running:
        clock.tick(60)
        current_player.yvelocity = current_player.yvelocity + gravity
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
                    current_player.xvelocity = current_player.xvelocity + 10
                    pygame.transform.flip(current_player.player_img, True, False)
                if event.key == s:
                    pass
                if event.key == d:
                    current_player.xvelocity = current_player.xvelocity - 10
                    pygame.transform.flip(current_player.player_img, True, False)
                if event.key == space:
                    current_player.yvelocity = 0
        JumpCounter = JumpCounter + 1
        mouse_pos = pygame.mouse.get_pos()        
        keys_pressed = pygame.key.get_pressed()
        
        if keys_pressed[w]:
            print("asdsdadas")
        if keys_pressed[a]:
            current_player.xvelocity = -10
        if keys_pressed[s]:
            pass
        if keys_pressed[d]:
            current_player.xvelocity = 10
        if keys_pressed[space] and JumpCounter > 200:
            JumpCounter = 1
            current_player.yvelocity = gravity - 24
            
        screen.fill(BLACK)
        
        
        spritecollided = pygame.sprite.spritecollideany(current_player, platforms)
        if spritecollided != None:
            sprite_pos = spritecollided.rect.topleft
            print(current_player.rect.y, sprite_pos[1])
            print(current_player.rect.y < sprite_pos[1])
            if current_player.y < sprite_pos[1]:
                current_player.y = 500 - spritecollided.rect.h
                print(spritecollided.rect.h)
            JumpCounter = 999
            if current_player.yvelocity > 0:
                
                current_player.yvelocity = 0
        current_player.update(screen)
        platforms.update()
        platforms.draw(screen)
        pygame.display.flip()