from images import ressource


class Maze:
    def __init__(self):
        self.maze = []

    def maze_content(self):
        with open("Maze.txt") as txt:
            content = []
            # Conversion from txt file in list
            for line in txt:
                line_map = []
                for element in line:
                    if element != '\n':
                        line_map.append(element)
                content.append(line_map)
            self.maze = content

    def maze_display(self, window):
        nb_y = 0
        for line in self.maze:
            nb_x = 0
            for element in line:
                x = nb_x * ressource.sprite_size
                y = nb_y * ressource.sprite_size
                if element == "1":
                    window.blit(ressource.image_floor, (x, y))
                elif element == "0":
                    window.blit(ressource.image_wall, (x, y))
                elif element == "A":
                    window.blit(ressource.image_guardian, (x, y))
                elif element == "D":
                    window.blit(ressource.image_floor, (x, y))

                nb_x += 1
            nb_y += 1


'''class Maze:

    # Displaying window
    window = pygame.display.set_mode((600, 600))
    # Window description
    pygame.display.set_caption('Maze')
    player_x = 4
    player_y = 0

    # Start main loop
    Main = True
    while Main:

        # frame rate: 60 frames per second
        pygame.time.Clock().tick(60)

        # Background image
        background = ressource.image_bg
        window.blit(background, (0, 0))

        # Loading objects
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
                window.blit(wall, (maze_x*40, maze_y*40))
            elif i == 1:
                window.blit(floor, (maze_x*40, maze_y*40))
            k += 1

        window.blit(player, (player_x, player_y))
        window.blit(guardian, (524, 562))

        # Refresh frame
        pygame.display.flip()

        # Events
        for event in pygame.event.get():
            # Keyboard
            if event.type == KEYDOWN:
                if event.key == K_UP or event.key == K_w:
                    player_y -= 40
                if event.key == K_DOWN or event.key == K_s:
                    player_y += 40
                if event.key == K_LEFT or event.key == K_a:
                    player_x -= 40
                if event.key == K_RIGHT or event.key == K_d:
                    player_x += 40
            # Mouse
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    # Mouse position
                    Position = pygame.mouse.get_pos()
                    pos_x = Position[0]
                    pos_y = Position[1]
                    print(Position)
            # Quit game when pressing key escape
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                Main = False
                pygame.display.quit()
            # Quit game when closing window
            if event.type == QUIT:
                Main = False
                pygame.display.quit()'''
