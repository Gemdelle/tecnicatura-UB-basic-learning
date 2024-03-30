import pygame

from core.regions_status import RegionsStatus
from ui.utils.resource_path_util import resource_path

region_selection_status = RegionsStatus.MAP

def move_forward():
    global region_selection_status

    if region_selection_status == RegionsStatus.MAP:
        region_selection_status = RegionsStatus.MAP_COMPLETED
    elif region_selection_status == RegionsStatus.MAP_COMPLETED:
        region_selection_status = RegionsStatus.VARIABLES_COMPLETED
    elif region_selection_status == RegionsStatus.VARIABLES_COMPLETED:
        region_selection_status = RegionsStatus.IF_COMPLETED
    elif region_selection_status == RegionsStatus.IF_COMPLETED:
        region_selection_status = RegionsStatus.WHILE_COMPLETED


def render_map(screen):
    # BACKGROUND #
    background_image = pygame.image.load(resource_path("assets\\region_selection\\maps\\original.png")).convert_alpha()
    background_rect = background_image.get_rect()
    scaled_image = pygame.transform.scale(background_image, (1920, 1080))
    screen.blit(scaled_image, background_rect)

    # ACCESS
    map_enabled_access = pygame.image.load(
        resource_path("assets\\region_selection\\characters\\Map.png")).convert_alpha()
    map_enabled_access_rect = pygame.Rect(80, 650, 318, 392)
    screen.blit(map_enabled_access, map_enabled_access_rect)

    # VARIABLES
    variables_access = pygame.image.load(
        resource_path("assets\\region_selection\\characters\\Variables-dark.png")).convert_alpha()
    variables_access_rect = pygame.Rect(350, 50, 318, 392)
    screen.blit(variables_access, variables_access_rect)

    # IF
    if_access = pygame.image.load(
        resource_path("assets\\region_selection\\characters\\If-dark.png")).convert_alpha()
    if_access_rect = pygame.Rect(870, 510, 318, 392)
    screen.blit(if_access, if_access_rect)

    # WHILE
    while_access = pygame.image.load(
        resource_path("assets\\region_selection\\characters\\While-dark.png")).convert_alpha()
    while_access_rect = pygame.Rect(1380, 190, 318, 392)
    screen.blit(while_access, while_access_rect)

def render_map_completed(screen):
    # BACKGROUND #
    background_image = pygame.image.load(resource_path("assets\\region_selection\\maps\\map.png")).convert_alpha()
    background_rect = background_image.get_rect()
    scaled_image = pygame.transform.scale(background_image, (1920, 1080))
    screen.blit(scaled_image, background_rect)

    # ACCESS
    map_enabled_access = pygame.image.load(
        resource_path("assets\\region_selection\\characters\\Map.png")).convert_alpha()
    map_enabled_access_rect = pygame.Rect(80, 650, 318, 392)
    screen.blit(map_enabled_access, map_enabled_access_rect)

    # VARIABLES
    variables_access = pygame.image.load(
        resource_path("assets\\region_selection\\characters\\Variables.png")).convert_alpha()
    variables_access_rect = pygame.Rect(350, 50, 318, 392)
    screen.blit(variables_access, variables_access_rect)

    # IF
    if_access = pygame.image.load(
        resource_path("assets\\region_selection\\characters\\If-dark.png")).convert_alpha()
    if_access_rect = pygame.Rect(870, 510, 318, 392)
    screen.blit(if_access, if_access_rect)

    # WHILE
    while_access = pygame.image.load(
        resource_path("assets\\region_selection\\characters\\While-dark.png")).convert_alpha()
    while_access_rect = pygame.Rect(1380, 190, 318, 392)
    screen.blit(while_access, while_access_rect)

def render_variables_completed(screen):
    # BACKGROUND #
    background_image = pygame.image.load(resource_path("assets\\region_selection\\maps\\variables.png")).convert_alpha()
    background_rect = background_image.get_rect()
    scaled_image = pygame.transform.scale(background_image, (1920, 1080))
    screen.blit(scaled_image, background_rect)

    # ACCESS
    map_enabled_access = pygame.image.load(
        resource_path("assets\\region_selection\\characters\\Map.png")).convert_alpha()
    map_enabled_access_rect = pygame.Rect(80, 650, 318, 392)
    screen.blit(map_enabled_access, map_enabled_access_rect)

    # VARIABLES
    variables_access = pygame.image.load(
        resource_path("assets\\region_selection\\characters\\Variables.png")).convert_alpha()
    variables_access_rect = pygame.Rect(350, 50, 318, 392)
    screen.blit(variables_access, variables_access_rect)

    # IF
    if_access = pygame.image.load(
        resource_path("assets\\region_selection\\characters\\If.png")).convert_alpha()
    if_access_rect = pygame.Rect(870, 510, 318, 392)
    screen.blit(if_access, if_access_rect)

    # WHILE
    while_access = pygame.image.load(
        resource_path("assets\\region_selection\\characters\\While-dark.png")).convert_alpha()
    while_access_rect = pygame.Rect(1380, 190, 318, 392)
    screen.blit(while_access, while_access_rect)


def render_if_completed(screen):
    # BACKGROUND #
    background_image = pygame.image.load(resource_path("assets\\region_selection\\maps\\if.png")).convert_alpha()
    background_rect = background_image.get_rect()
    scaled_image = pygame.transform.scale(background_image, (1920, 1080))
    screen.blit(scaled_image, background_rect)

    # ACCESS
    map_enabled_access = pygame.image.load(
        resource_path("assets\\region_selection\\characters\\Map.png")).convert_alpha()
    map_enabled_access_rect = pygame.Rect(80, 650, 318, 392)
    screen.blit(map_enabled_access, map_enabled_access_rect)

    # VARIABLES
    variables_access = pygame.image.load(
        resource_path("assets\\region_selection\\characters\\Variables.png")).convert_alpha()
    variables_access_rect = pygame.Rect(350, 50, 318, 392)
    screen.blit(variables_access, variables_access_rect)

    # IF
    if_access = pygame.image.load(
        resource_path("assets\\region_selection\\characters\\If.png")).convert_alpha()
    if_access_rect = pygame.Rect(870, 510, 318, 392)
    screen.blit(if_access, if_access_rect)

    # WHILE
    while_access = pygame.image.load(
        resource_path("assets\\region_selection\\characters\\While.png")).convert_alpha()
    while_access_rect = pygame.Rect(1380, 190, 318, 392)
    screen.blit(while_access, while_access_rect)


def render_while_completed(screen):
    # BACKGROUND #
    background_image = pygame.image.load(resource_path("assets\\region_selection\\maps\\while.png")).convert_alpha()
    background_rect = background_image.get_rect()
    scaled_image = pygame.transform.scale(background_image, (1920, 1080))
    screen.blit(scaled_image, background_rect)

    # ACCESS
    map_enabled_access = pygame.image.load(
        resource_path("assets\\region_selection\\characters\\Map.png")).convert_alpha()
    map_enabled_access_rect = pygame.Rect(80, 650, 318, 392)
    screen.blit(map_enabled_access, map_enabled_access_rect)

    # VARIABLES
    variables_access = pygame.image.load(
        resource_path("assets\\region_selection\\characters\\Variables.png")).convert_alpha()
    variables_access_rect = pygame.Rect(350, 50, 318, 392)
    screen.blit(variables_access, variables_access_rect)

    # IF
    if_access = pygame.image.load(
        resource_path("assets\\region_selection\\characters\\If.png")).convert_alpha()
    if_access_rect = pygame.Rect(870, 510, 318, 392)
    screen.blit(if_access, if_access_rect)

    # WHILE
    while_access = pygame.image.load(
        resource_path("assets\\region_selection\\characters\\While.png")).convert_alpha()
    while_access_rect = pygame.Rect(1380, 190, 318, 392)
    screen.blit(while_access, while_access_rect)

    # COMING SOON
    font = pygame.font.Font(resource_path('font\\White Storm.ttf'), 60)
    text_surface = font.render("Coming soon...", True, (255, 255, 255))
    text_rect = pygame.Rect(1450, 850, 300, 100)
    screen.blit(text_surface, text_rect)

def render_region_selection(screen):

    if region_selection_status == RegionsStatus.MAP:
        render_map(screen)
    elif region_selection_status == RegionsStatus.MAP_COMPLETED:
        render_map_completed(screen)
    elif region_selection_status == RegionsStatus.VARIABLES_COMPLETED:
        render_variables_completed(screen)
    elif region_selection_status == RegionsStatus.IF_COMPLETED:
        render_if_completed(screen)
    elif region_selection_status == RegionsStatus.WHILE_COMPLETED:
        render_while_completed(screen)


