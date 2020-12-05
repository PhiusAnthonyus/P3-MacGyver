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

