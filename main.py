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
background = ressource.image_bg
window.blit(background, (0, 0))
player_x = 30
player_y = 0

# Start infinite loop
Main = True
while Main:
    # frame rate: 60 frames per second
    pygame.time.Clock().tick(60)
    pygame.display.flip()
    Menu = True
    Game = True
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
        button_1_2_desc = font_button_bold.render(str("Options"), 1, (0, 0, 0))
        credits_desc = font_credits.render(str("Réalisé par Anthony Phu"), 1, (255, 255, 255))

        # Loading objects
        title = ressource.image_title
        button1_idle = ressource.image_button_1_idle
        button1_press = ressource.image_button_1_press
        # Display objects
        window.blit(background, (0, 0))
        window.blit(title, (50, 50))
        window.blit(title_desc_1, (65, 65))
        window.blit(title_desc_2, (95, 135))
        window.blit(button1_idle, (200, 300))
        if (200 < mouse_x < 400) and (300 < mouse_y < 350):
            window.blit(button1_press, (200, 300))
        window.blit(button_1_1_desc, (255, 300))
        window.blit(button1_idle, (200, 400))
        if (200 < mouse_x < 400) and (400 < mouse_y < 450):
            window.blit(button1_press, (200, 400))
        window.blit(button_1_2_desc, (235, 400))
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
                        pygame.display.flip()
            # Quit game when pressing key escape
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                Menu = False
                Main = False
                Game = False
                pygame.display.quit()
            # Quit game when closing window
            if event.type == QUIT:
                Menu = False
                Main = False
                Game = False
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
        '''# Loading objects
        wall = ressource.image_wall
        floor = ressource.image_floor
        player = ressource.image_player
        guardian = ressource.image_guardian

        # Maze content
        maze = open("Maze.txt", "r")
        maze_content = maze.read()
        maze_list = []
        # Conversion from txt file in list
        for i in maze_content:
            if i != '\n':
                maze_list.append(int(i, base=10))
        maze.close()
        # Maze creation
        i = 0
        k = 0
        for i in maze_list:
            # Coordinate calculation
            maze_x = k % 15
            maze_y = k / 15
            maze_y = int(maze_y)
            # Texture attribution in each coordinate
            if i == 0:
                window.blit(wall, (maze_x * 40, maze_y * 40))
            elif i == 1:
                window.blit(floor, (maze_x * 40, maze_y * 40))
            k += 1

        window.blit(player, (player_x, player_y))
        window.blit(guardian, (524, 562))
        pygame.display.flip()'''

        # Events
        for event in pygame.event.get():
            # Quit game when closing window
            if event.type == QUIT:
                Game = False
                Main = False
                Menu = False
                pygame.display.quit()

            # Keyboard
            elif event.type == KEYDOWN:
                # Quit game when pressing key escape
                if event.key == K_ESCAPE:
                    Game = False
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

            # display
            Maze.maze_display(window)
            window.blit(ressource.image_player, (player.x, player.y))
            window.blit(ressource.image_coin1, (obj1.pos_x * ressource.sprite_size, obj1.pos_y * ressource.sprite_size))
            window.blit(ressource.image_coin2, (obj2.pos_x * ressource.sprite_size, obj2.pos_y * ressource.sprite_size))
            window.blit(ressource.image_coin3, (obj3.pos_x * ressource.sprite_size, obj3.pos_y * ressource.sprite_size))
            pygame.display.flip()

        # Conditions for win
        if Maze.maze[player.pos_x][player.pos_y] == "A" and obj_count == 3:
            print('win')
            '''window.blit(ressource.image_bg, (0, 0))
            font_title_bold = pygame.font.SysFont('Arial', 75, True)
            win = font_title_bold.render(str("Vous avez gagné !"), 1, (255, 255, 255))
            window.blit(win, (300, 300))'''
            pygame.display.flip()
            Game = False
            Menu = True
        elif Maze.maze[player.pos_x][player.pos_y] == "A" and obj_count != 3:
            print('lose')
            '''window.blit(ressource.image_bg, (0, 0))
            font_title_bold = pygame.font.SysFont('Arial', 75, True)
            lose = font_title_bold.render(str("Vous avez perdu !"), 1, (255, 255, 255))
            window.blit(lose, (300, 300))'''
            Game = False
            Menu = True
