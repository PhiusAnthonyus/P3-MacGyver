from images import ressource
import random


class Character:
    """Generate the character and add attributes."""
    def __init__(self, maze):
        # Set parameters for character
        # pos_x/y = case number * size sprite
        self.pos_x = 0
        self.pos_y = 0
        # Initial position
        self.x = 0
        self.y = 0
        self.maze = maze

    def move(self, direction):
        if direction == "right":
            if self.pos_x < 14 and self.maze[self.pos_y][self.pos_x + 1] != "0" \
                    and self.pos_x + 1 <= ressource.maze_x - 1:
                self.pos_x += 1
                self.x = self.pos_x * ressource.sprite_size
        if direction == "left":
            if self.pos_x >= 0 and self.maze[self.pos_y][self.pos_x - 1] != "0" \
                    and self.pos_x - 1 >= 0:
                self.pos_x -= 1
                self.x = self.pos_x * ressource.sprite_size
        if direction == "up":
            if self.pos_y >= 0 and self.maze[self.pos_y - 1][self.pos_x] != "0" \
                    and self.pos_y - 1 >= 0:
                self.pos_y -= 1
                self.y = self.pos_y * ressource.sprite_size
        if direction == "down":
            if self.pos_y < 14 and self.maze[self.pos_y + 1][self.pos_x] != "0" \
                    and self.pos_y + 1 <= ressource.maze_x - 1:
                self.pos_y += 1
                self.y = self.pos_y * ressource.sprite_size


class Object:
    """Generate objects and add attributes."""
    def __init__(self, maze):
        # Set parameters for object
        self.maze = maze
        # Cases
        self.pos_x = 0
        self.pos_y = 0
        self.x = 0
        self.y = 0

    def random_position(self):
        # Generate a random position for objects.
        while self.maze[self.pos_y][self.pos_x] != "1":
            self.pos_x = random.randint(1, 13)
            self.pos_y = random.randint(1, 13)
        self.x = self.pos_x * ressource.sprite_size
        self.y = self.pos_y * ressource.sprite_size


def init_items(maze):
    """Generate multiple objects at different positions"""
    obj1 = Object(maze)
    obj1.random_position()
    obj2 = Object(maze)
    obj2.random_position()

    while obj1.pos_y == obj2.pos_y and obj1.pos_x == obj2.pos_x:
        obj2.random_position()
    obj3 = Object(maze)
    obj3.random_position()
    while (obj1.pos_y == obj3.pos_y and obj1.pos_x == obj3.pos_x) \
            or (obj2.pos_y == obj3.pos_y and obj2.pos_x == obj3.pos_x):
        obj3.random_position()
    return obj1, obj2, obj3
