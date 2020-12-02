import os
import pygame  # PyGame 1.9.6

pygame.display.init()
pygame.display.set_mode()

maze_x = 15
maze_y = 16
sprite_size = 40
window_x = maze_x * sprite_size
window_y = maze_y * sprite_size


image_bg = pygame.image.load(os.path.join("images", "bg.png")).convert()
image_title = pygame.image.load(os.path.join("images", "title.png")).convert()
image_button_1_idle = pygame.image.load(os.path.join("images", "button1_idle.png")).convert()
image_button_1_press = pygame.image.load(os.path.join("images", "button1_press.png")).convert()
image_wall = pygame.image.load(os.path.join("images", "wall.png")).convert()
image_floor = pygame.image.load(os.path.join("images", "floor.png")).convert()
image_player = pygame.image.load(os.path.join("images", "MacGyver.png")).convert_alpha()
image_guardian = pygame.image.load(os.path.join("images", "guardian.png")).convert_alpha()
image_coin1 = pygame.image.load(os.path.join("images", "coin1.png")).convert_alpha()
image_coin2 = pygame.image.load(os.path.join("images", "coin2.png")).convert_alpha()
image_coin3 = pygame.image.load(os.path.join("images", "coin3.png")).convert_alpha()
