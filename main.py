import os

import pygame

from sys import exit

from core.screens import Screens
from ui.screens.field.field_1 import render_field_1, save_code, erase_code, line_break
from ui.screens.field.field_2 import render_field_2
from ui.screens.field.field_3 import render_field_3
from ui.screens.field.field_4 import render_field_4
from ui.screens.light_woods.light_woods_1 import render_light_woods_1
from ui.screens.light_woods.light_woods_2 import render_light_woods_2
from ui.screens.light_woods.light_woods_3 import render_light_woods_3
from ui.screens.light_woods.light_woods_4 import render_light_woods_4
from ui.screens.light_woods.light_woods_5 import render_light_woods_5
from ui.screens.light_woods.light_woods_6 import render_light_woods_6
from ui.screens.map.map_1 import render_map_1
from ui.screens.map.map_2 import render_map_2
from ui.screens.map.map_3 import render_map_3
from ui.screens.map.map_4 import render_map_4
from ui.screens.map.map_5 import render_map_5
from ui.screens.splash import render_splash, start_game
from ui.screens.water_woods.water_woods_1 import render_water_woods_1
from ui.screens.water_woods.water_woods_2 import render_water_woods_2
from ui.screens.water_woods.water_woods_3 import render_water_woods_3
from ui.screens.water_woods.water_woods_4 import render_water_woods_4
from ui.utils.resource_path_util import resource_path

# Setup
pygame.init()
PRODUCT_HEIGHT = 28
MARGIN = 130
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('PyEvolve')
clock = pygame.time.Clock()
game_active = True
running = True

screen_selected = Screens.SPLASH

button_font_manager = pygame.font.Font(resource_path('font\\White Storm.ttf'), 25)

def listen_to_key_binding():
    global running, screen_selected
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.TEXTINPUT:
            save_code(event.text)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            elif event.key == pygame.K_BACKSPACE:
                erase_code()
            elif event.key == pygame.K_RETURN:
                line_break()
            elif event.key == pygame.K_SPACE:
                start_game(go_to_field_1)

# MAP NAVIGATION #
def go_to_map_1():
    global screen_selected
    screen_selected = Screens.MAP_1
    print("Navigate to:", screen_selected)

def go_to_map_2():
    global screen_selected
    screen_selected = Screens.MAP_2
    print("Navigate to:", screen_selected)

def go_to_map_3():
    global screen_selected
    screen_selected = Screens.MAP_3
    print("Navigate to:", screen_selected)

def go_to_map_4():
    global screen_selected
    screen_selected = Screens.MAP_4
    print("Navigate to:", screen_selected)

def go_to_map_5():
    global screen_selected
    screen_selected = Screens.MAP_4
    print("Navigate to:", screen_selected)


# FIELD NAVIGATION #
def go_to_field_1():
    global screen_selected
    screen_selected = Screens.FIELD_1
    print("Navigate to:", screen_selected)

def go_to_field_2():
    global screen_selected
    screen_selected = Screens.FIELD_2
    print("Navigate to:", screen_selected)

def go_to_field_3():
    global screen_selected
    screen_selected = Screens.FIELD_3
    print("Navigate to:", screen_selected)

def go_to_field_4():
    global screen_selected
    screen_selected = Screens.FIELD_4
    print("Navigate to:", screen_selected)

# LIGHT WOODS NAVIGATION #
def go_to_light_woods_1():
    global screen_selected
    screen_selected = Screens.LIGHT_WOODS_1
    print("Navigate to:", screen_selected)

def go_to_light_woods_2():
    global screen_selected
    screen_selected = Screens.LIGHT_WOODS_2
    print("Navigate to:", screen_selected)

def go_to_light_woods_3():
    global screen_selected
    screen_selected = Screens.LIGHT_WOODS_3
    print("Navigate to:", screen_selected)

def go_to_light_woods_4():
    global screen_selected
    screen_selected = Screens.LIGHT_WOODS_4
    print("Navigate to:", screen_selected)

def go_to_light_woods_5():
    global screen_selected
    screen_selected = Screens.LIGHT_WOODS_5
    print("Navigate to:", screen_selected)

def go_to_light_woods_6():
    global screen_selected
    screen_selected = Screens.LIGHT_WOODS_6
    print("Navigate to:", screen_selected)

# WATER WOODS NAVIGATION #
def go_to_water_woods_1():
    global screen_selected
    screen_selected = Screens.WATER_WOODS_1
    print("Navigate to:", screen_selected)

def go_to_water_woods_2():
    global screen_selected
    screen_selected = Screens.WATER_WOODS_2
    print("Navigate to:", screen_selected)

def go_to_water_woods_3():
    global screen_selected
    screen_selected = Screens.WATER_WOODS_3
    print("Navigate to:", screen_selected)

def go_to_water_woods_4():
    global screen_selected
    screen_selected = Screens.WATER_WOODS_4
    print("Navigate to:", screen_selected)

def go_to_finish_screen():
    #global screen_selected
    #screen_selected = Screens.WATER_WOODS_4
    #print("Navigate to:", screen_selected)
    print("FINISH!")

def play_music():
    pygame.mixer.music.set_volume(0.6)
    mp3_file = resource_path("assets\\sounds\\background_music.mp3")
    if not os.path.exists(mp3_file):
        raise FileNotFoundError(f"File '{mp3_file}' not found.")
    try:
        pygame.mixer.music.load(mp3_file)
        pygame.mixer.music.play(loops=-1)
    except KeyboardInterrupt:
        pygame.mixer.music.stop()
        pygame.quit()

play_music()
while running:
    listen_to_key_binding()
    if game_active:
        if screen_selected == Screens.SPLASH:
            render_splash(screen)
        elif screen_selected == Screens.MAP_1:
            render_map_1(screen, go_to_map_2, go_to_map_3, go_to_map_4, go_to_map_5)
        elif screen_selected == Screens.MAP_2:
            render_map_2(screen, go_to_map_1, go_to_field_1)
        elif screen_selected == Screens.MAP_3:
            render_map_3(screen, go_to_map_1, go_to_field_1)
        elif screen_selected == Screens.MAP_4:
            render_map_4(screen, go_to_map_1, go_to_field_1)
        elif screen_selected == Screens.MAP_5:
            render_map_5(screen, go_to_map_1, go_to_field_1)
        elif screen_selected == Screens.FIELD_1:
            render_field_1(screen, go_to_field_2)
        elif screen_selected == Screens.FIELD_2:
            render_field_2(screen, go_to_field_1, go_to_field_3)
        elif screen_selected == Screens.FIELD_3:
            render_field_3(screen, go_to_field_2, go_to_field_4)
        elif screen_selected == Screens.FIELD_4:
            render_field_4(screen, go_to_field_3, go_to_light_woods_1)
        elif screen_selected == Screens.LIGHT_WOODS_1:
            render_light_woods_1(screen, go_to_light_woods_2, go_to_light_woods_3, go_to_light_woods_4, go_to_light_woods_5)
        elif screen_selected == Screens.LIGHT_WOODS_2:
            render_light_woods_2(screen, go_to_light_woods_1)
        elif screen_selected == Screens.LIGHT_WOODS_3:
            render_light_woods_3(screen, go_to_light_woods_1)
        elif screen_selected == Screens.LIGHT_WOODS_4:
            render_light_woods_4(screen, go_to_light_woods_1)
        elif screen_selected == Screens.LIGHT_WOODS_5:
            render_light_woods_5(screen, go_to_light_woods_1, go_to_light_woods_6)
        elif screen_selected == Screens.LIGHT_WOODS_6:
            render_light_woods_6(screen, go_to_light_woods_5, go_to_water_woods_1)
        elif screen_selected == Screens.WATER_WOODS_1:
            render_water_woods_1(screen, go_to_water_woods_2)
        elif screen_selected == Screens.WATER_WOODS_2:
            render_water_woods_2(screen, go_to_water_woods_1, go_to_water_woods_2, go_to_water_woods_3, go_to_water_woods_4)
        elif screen_selected == Screens.WATER_WOODS_3:
            render_water_woods_3(screen, go_to_water_woods_2, go_to_finish_screen)
        elif screen_selected == Screens.WATER_WOODS_4:
            render_water_woods_4(screen, go_to_water_woods_2, go_to_finish_screen)
        else:
            print("HOLA")

    pygame.display.update()
    clock.tick(60)