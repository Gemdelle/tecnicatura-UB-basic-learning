import pygame

def draw_button(x, y, width, height, text, button_color, text_color, screen):
    pygame.draw.rect(screen, button_color, (x, y, width, height))

    text_surface = pygame.font.Font('font/Alkhemikal.ttf', 25).render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))

    screen.blit(text_surface, text_rect)
    return text_rect
def render_map_1(screen,go_to_map_2, go_to_map_3, go_to_map_4, go_to_map_5):
    screen.fill((255, 255, 255))
    draw_button(800, 500, 350, 50, "MAP 1", (225, 224, 204), 'White', screen)