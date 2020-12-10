import pygame  # PyGame 1.9.6
from pygame.locals import *
import classes
import maze
from images import ressource


pygame.init()

# Displaying window
window = pygame.display.set_mode((ressource.window_x, ressource.window_y))
# Window description
pygame.display.set_caption('Labyrinthe')
background = pygame.image.load(ressource.image_bg).convert()
window.blit(background, (0, 0))

# Start infinite loop
Main = True
while Main:
    # frame rate: 60 frames per second
    pygame.time.Clock().tick(60)
    pygame.display.flip()
    Menu = True
    Game = True
    Ending = True
    win = False
    while Menu:
        # Get mouse position
        mouse = pygame.mouse.get_pos()
        mouse_x = mouse[0]
        mouse_y = mouse[1]

        # Loading font
        font_title_bold = pygame.font.SysFont('Arial', 75, True)
        font_button_bold = pygame.font.SysFont('Arial', 40, True)
        font_credits = pygame.font.SysFont('Arial', 15)
        # Create text
        title_desc_1 = font_title_bold.render(str("Aidez MacGyver"), 1, (255, 255, 255))
        title_desc_2 = font_title_bold.render(str("à s'échapper !"), 1, (255, 255, 255))
        button_1_1_desc = font_button_bold.render(str("Jouer"), 1, (0, 0, 0))
        credits_desc = font_credits.render(str("Réalisé par Anthony Phu"), 1, (255, 255, 255))

        # Loading objects
        title = pygame.image.load(ressource.image_title).convert()
        button1_idle = pygame.image.load(ressource.image_button_1_idle).convert()
        button1_press = pygame.image.load(ressource.image_button_1_press).convert()
        # Display objects
        window.blit(background, (0, 0))
        window.blit(title, (50, 50))
        window.blit(title_desc_1, (65, 65))
        window.blit(title_desc_2, (95, 135))
        window.blit(button1_idle, (200, 300))
        if (200 < mouse_x < 400) and (300 < mouse_y < 350):
            window.blit(button1_press, (200, 300))
        window.blit(button_1_1_desc, (255, 300))
        window.blit(credits_desc, (400, 550))

        # Refresh frame
        pygame.display.flip()

        # Window events
        for event in pygame.event.get():
            # Mouse position
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    Position = pygame.mouse.get_pos()
                    pos_x = Position[0]
                    pos_y = Position[1]
                    if (200 < pos_x < 400) and (300 < pos_y < 350):
                        Menu = False
                        Game = True
                        Ending = False
                        pygame.display.flip()
            # Quit game when pressing key escape
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                Menu = False
                Main = False
                Game = False
                Ending = False
                pygame.display.quit()
            # Quit game when closing window
            if event.type == QUIT:
                Menu = False
                Main = False
                Game = False
                Ending = False
                pygame.display.quit()

    # Maze creation
    Maze = maze.Maze()
    Maze.maze_content()
    # Object initialization
    obj1, obj2, obj3 = classes.init_items(Maze.maze)
    obj_count = 0
    # Player initialization
    player = classes.Character(Maze.maze)

    while Game:
        # Events
        for event in pygame.event.get():
            # Quit game when closing window
            if event.type == QUIT:
                Game = False
                Main = False
                Menu = False
                Ending = False
                pygame.display.quit()

            # Keyboard
            elif event.type == KEYDOWN:
                # Quit game when pressing key escape
                if event.key == K_ESCAPE:
                    Game = False
                    Ending = False
                    Menu = True
                elif event.key == K_UP or event.key == K_w:
                    player.move("up")
                elif event.key == K_DOWN or event.key == K_s:
                    player.move("down")
                elif event.key == K_LEFT or event.key == K_a:
                    player.move("left")
                elif event.key == K_RIGHT or event.key == K_d:
                    player.move("right")
            if player.pos_x == obj1.pos_x and player.pos_y == obj1.pos_y:
                obj1.pos_x = 0
                obj1.pos_y = 15
                obj_count += 1
            if player.pos_x == obj2.pos_x and player.pos_y == obj2.pos_y:
                obj2.pos_x = 1
                obj2.pos_y = 15
                obj_count += 1
            if player.pos_x == obj3.pos_x and player.pos_y == obj3.pos_y:
                obj3.pos_x = 2
                obj3.pos_y = 15
                obj_count += 1

            # Loading objects
            image_player = pygame.image.load(ressource.image_player).convert_alpha()
            coin1 = pygame.image.load(ressource.image_coin1).convert_alpha()
            coin2 = pygame.image.load(ressource.image_coin2).convert_alpha()
            coin3 = pygame.image.load(ressource.image_coin3).convert_alpha()
            # Display objects
            window.blit(background, (0, 0))
            Maze.maze_display(window)
            window.blit(image_player, (player.x, player.y))
            window.blit(coin1, (obj1.pos_x * ressource.sprite_size, obj1.pos_y * ressource.sprite_size))
            window.blit(coin2, (obj2.pos_x * ressource.sprite_size, obj2.pos_y * ressource.sprite_size))
            window.blit(coin3, (obj3.pos_x * ressource.sprite_size, obj3.pos_y * ressource.sprite_size))
            pygame.display.flip()

        # Conditions for win
        if Maze.maze[player.pos_x][player.pos_y] == "A" and obj_count == 3:
            win = True
            pygame.display.flip()
            Game = False
            Ending = True
        elif Maze.maze[player.pos_x][player.pos_y] == "A" and obj_count != 3:
            win = False
            Game = False
            Ending = True

    while Ending:
        # Get mouse position
        mouse = pygame.mouse.get_pos()
        mouse_x = mouse[0]
        mouse_y = mouse[1]
        # Loading objects
        title = pygame.image.load(ressource.image_title).convert()
        button1_idle = pygame.image.load(ressource.image_button_1_idle).convert()
        button1_press = pygame.image.load(ressource.image_button_1_press).convert()
        # Create text
        font_ending_bold = pygame.font.SysFont('Arial', 60, True)
        font_button_bold = pygame.font.SysFont('Arial', 40, True)
        win_desc = font_ending_bold.render(str("Vous avez gagné !"), 1, (255, 255, 255))
        lose_desc = font_ending_bold.render(str("Vous avez perdu !"), 1, (255, 255, 255))
        button_1_1_desc = font_button_bold.render(str("Menu"), 1, (0, 0, 0))
        # Display objects
        window.blit(background, (0, 0))
        if win:
            window.blit(win_desc, (100, 200))
        elif not win:
            window.blit(lose_desc, (100, 200))
        window.blit(button1_idle, (200, 300))
        if (200 < mouse_x < 400) and (300 < mouse_y < 350):
            window.blit(button1_press, (200, 300))
        window.blit(button_1_1_desc, (255, 300))
        pygame.display.flip()

        # Window events
        for event in pygame.event.get():
            # Mouse position
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    Position = pygame.mouse.get_pos()
                    pos_x = Position[0]
                    pos_y = Position[1]
                    if (200 < pos_x < 400) and (300 < pos_y < 350):
                        Ending = False
                        Menu = True
                        Game = False
                        pygame.display.flip()
            # Quit game when pressing key escape
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                Menu = False
                Main = False
                Game = False
                Ending = False
                pygame.display.quit()
            # Quit game when closing window
            if event.type == QUIT:
                Menu = False
                Main = False
                Game = False
                Ending = False
                pygame.display.quit()
