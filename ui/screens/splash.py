import pygame

from ui.utils.resource_path_util import resource_path

start_scale = 1
target_scale = 1.4
total_duration = 2
frames_per_second = 60

scale_change_per_frame = (target_scale - start_scale) / (total_duration * frames_per_second)

current_scale = start_scale

blink_interval = 500  # milliseconds
blink_timer = 0
visible = True


def start_game(go_to_map_1):
    go_to_map_1()


def render_splash(screen):
    global current_scale, blink_timer, visible
    background_image = pygame.image.load(resource_path("assets\\splash\\splash_background.png")).convert_alpha()
    background_rect = background_image.get_rect()
    logo_image = pygame.image.load(resource_path("assets\\splash\\UB_logo.jpg")).convert_alpha()
    logo_rect = logo_image.get_rect()

    current_scale += scale_change_per_frame

    current_scale = min(current_scale, target_scale)

    new_width = int(background_rect.width * current_scale)
    new_height = int(background_rect.height * current_scale)
    new_logo_width = int(logo_rect.width * current_scale)
    new_logo_height = int(logo_rect.height * current_scale)

    scaled_background = pygame.transform.scale(background_image, (new_width, new_height))
    scaled_rect = scaled_background.get_rect(center=screen.get_rect().center)

    scaled_logo = pygame.transform.scale(logo_image, (new_logo_width, new_logo_height))
    scaled_logo_rect = scaled_logo.get_rect(center=screen.get_rect().center)

    ############################
    screen.fill((255, 255, 255))
    screen.blit(scaled_background, scaled_rect)
    screen.blit(scaled_logo, scaled_logo_rect)

    if current_scale == target_scale:
        font = pygame.font.Font(resource_path('font\\White Storm.ttf'), 40)
        text_surface = font.render("Press {SPACE-BAR} to continue", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(950, 1000))
        blink_timer += pygame.time.Clock().tick(60)
        if blink_timer >= blink_interval:
            visible = not visible
            blink_timer = 0
        if visible:
            screen.blit(text_surface, text_rect)
