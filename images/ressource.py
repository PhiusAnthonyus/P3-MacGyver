import pygame  # PyGame 1.9.6

pygame.display.init()
pygame.display.set_mode()

maze_x = 15
maze_y = 16
sprite_size = 40
window_x = maze_x * sprite_size
window_y = maze_y * sprite_size


image_bg = "images/bg.png"
image_title = "images/title.png"
image_button_1_idle = "images/button1_idle.png"
image_button_1_press = "images/button1_press.png"
image_wall = "images/wall.png"
image_floor = "images/floor.png"
image_player = "images/MacGyver.png"
image_guardian = "images/guardian.png"
image_coin1 = "images/coin1.png"
image_coin2 = "images/coin2.png"
image_coin3 = "images/coin3.png"
