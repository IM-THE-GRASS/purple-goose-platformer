
def main():
    import pygame
    import os
    import ui
    import time
    import level1
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    pygame.init()
    click = False
    mouse_pos = pygame.mouse.get_pos()
    mouse_info = [click, mouse_pos]
    running = True
    screen = pygame.display.set_mode((1200, 700))


    menu = ui.menu(click, mouse_pos,screen,(25, 25))
    def on_play():
        
        menu.enabled = False
        print("play")
        level1.main()

    def on_settings():
        print("settings")

    def on_quit():
        time.sleep(0.5)
        pygame.quit()
        quit()
        


    menu.add_button(500, 125,"image",os.path.join('images', 'play.png'),"play", on_play, os.path.join("sounds", "start_game.ogg"))
    menu.add_button(500, 125,"image",os.path.join('images', 'levels.png'),"settings", on_settings, os.path.join("sounds", "menu_select.wav"))
    menu.add_button(500, 125,"image",os.path.join('images', 'quit.png'),"quit", on_quit, os.path.join("sounds", "death.wav"))

    def main():
        while running:
            click = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = "down"
                if event.type == pygame.MOUSEBUTTONUP:
                    click = "up"
            mouse_pos = pygame.mouse.get_pos()
            menu.set_mouse_info(click, mouse_pos)

            
            
            screen.fill(BLACK)
            
            menu.draw()

            pygame.display.flip()