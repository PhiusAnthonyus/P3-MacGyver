import pygame
from images import ressource


class Maze:
    """Creates the maze based on the text file and use the double entry table to display each sprite. """
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
        floor = pygame.image.load(ressource.image_floor).convert()
        wall = pygame.image.load(ressource.image_wall).convert()
        guardian = pygame.image.load(ressource.image_guardian).convert()
        nb_y = 0
        for line in self.maze:
            nb_x = 0
            for element in line:
                x = nb_x * ressource.sprite_size
                y = nb_y * ressource.sprite_size
                if element == "1":
                    window.blit(floor, (x, y))
                elif element == "0":
                    window.blit(wall, (x, y))
                elif element == "A":
                    window.blit(guardian, (x, y))
                elif element == "D":
                    window.blit(floor, (x, y))

                nb_x += 1
            nb_y += 1

