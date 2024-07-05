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
gravity = 0.6
player_img = os.path.join("images", "goose.png")
player = player.player(25,25,player_img)
player.yvelocity = 0
w = pygame.K_w
a = pygame.K_a
s = pygame.K_s
d = pygame.K_d
space = pygame.K_SPACE
clock = pygame.time.Clock()
def main():
    JumpCounter = 999
    print(a)
    while running:
        clock.tick(60)
        player.yvelocity = player.yvelocity + gravity
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
                    player.xvelocity = player.xvelocity + 10
                if event.key == s:
                    pass
                if event.key == d:
                    player.xvelocity = player.xvelocity - 10
                if event.key == space:
                    player.yvelocity = 0
        JumpCounter = JumpCounter + 1
        mouse_pos = pygame.mouse.get_pos()        
        keys_pressed = pygame.key.get_pressed()
        
        if keys_pressed[w]:
            print("asdsdadas")
        if keys_pressed[a]:
            player.xvelocity = -10
        if keys_pressed[s]:
            pass
        if keys_pressed[d]:
            player.xvelocity = 10
        if keys_pressed[space] and JumpCounter > 200:
            JumpCounter = 1
            player.yvelocity = gravity - 24
            
        screen.fill(BLACK)
        print(player.yvelocity)
        platform = pygame.Rect(0,500,500,50)
        pygame.draw.rect(screen,(255,255,255),platform)
        if player.rect.colliderect(platform):
            JumpCounter = 999
            print(player.yvelocity)
            if player.yvelocity > 0:
                
                player.yvelocity = 0
        player.draw(screen)
        pygame.display.flip()