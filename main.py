import pygame

from sys import exit

from core.screens import Screens
from ui.screens.splash import render_splash

# Setup
pygame.init()
PRODUCT_HEIGHT = 28
MARGIN = 130
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
screen = pygame.display.set_mode((SCREEN_WIDTH,
                                  SCREEN_HEIGHT))
pygame.display.set_caption('PyEvolve')
clock = pygame.time.Clock()
game_active = True
running = True

screen_selected = Screens.SPLASH

button_font_manager = pygame.font.Font('font/Alkhemikal.ttf', 25)

def listen_to_key_binding():
    global event, running, screen_selected
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

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

while running:
    listen_to_key_binding()
    if game_active:
        if screen_selected == Screens.SPLASH:
            render_splash(screen, go_to_map_1)
        elif screen_selected == Screens.MAP_1:
            render_main(screen, go_to_map_2, go_to_map_3, go_to_map_4, go_to_map_5)
        elif screen_selected == Screens.MAP_2:
            render_main(screen, go_to_map_1, go_to_field_1)
        elif screen_selected == Screens.MAP_3:
            render_main(screen, go_to_map_1, go_to_field_1)
        elif screen_selected == Screens.MAP_4:
            render_main(screen, go_to_map_1, go_to_field_1)
        elif screen_selected == Screens.MAP_5:
            render_main(screen, go_to_map_1, go_to_field_1)
        elif screen_selected == Screens.FIELD_1:
            render_main(screen, go_to_field_2)
        elif screen_selected == Screens.FIELD_2:
            render_main(screen, go_to_field_1, go_to_field_3)
        elif screen_selected == Screens.FIELD_3:
            render_main(screen, go_to_field_2, go_to_field_4)
        elif screen_selected == Screens.FIELD_4:
            render_main(screen, go_to_field_3, go_to_light_woods_1)
        elif screen_selected == Screens.LIGHT_WOODS_1:
            render_main(screen, go_to_light_woods_2, go_to_light_woods_3, go_to_light_woods_4, go_to_light_woods_5)
        elif screen_selected == Screens.LIGHT_WOODS_2:
            render_main(screen, go_to_light_woods_1)
        elif screen_selected == Screens.LIGHT_WOODS_3:
            render_main(screen, go_to_light_woods_1)
        elif screen_selected == Screens.LIGHT_WOODS_4:
            render_main(screen, go_to_light_woods_1)
        elif screen_selected == Screens.LIGHT_WOODS_5:
            render_main(screen, go_to_light_woods_1, go_to_light_woods_6)
        elif screen_selected == Screens.LIGHT_WOODS_6:
            render_main(screen, go_to_light_woods_5, go_to_water_woods_1)
        elif screen_selected == Screens.WATER_WOODS_1:
            render_main(screen, go_to_water_woods_2)
        elif screen_selected == Screens.WATER_WOODS_2:
            render_main(screen, go_to_water_woods_1, go_to_water_woods_2, go_to_water_woods_3, go_to_water_woods_4)
        elif screen_selected == Screens.WATER_WOODS_3:
            render_main(screen, go_to_water_woods_2, go_to_finish_screen)
        elif screen_selected == Screens.WATER_WOODS_4:
            render_main(screen, go_to_water_woods_2, go_to_finish_screen)


        else:
            print("HOLA")

    pygame.display.update()
    clock.tick(60)