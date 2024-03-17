import pygame

def draw_button(x, y, width, height, text, button_color, text_color, screen):
    pygame.draw.rect(screen, button_color, (x, y, width, height))

    text_surface = pygame.font.Font('font/Alkhemikal.ttf', 25).render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))

    screen.blit(text_surface, text_rect)
    return text_rect
def render_light_woods_6(screen):
    screen.fill((255, 255, 255))
    draw_button(800, 500, 350, 50, "LIGHT WOODS 6", (225, 224, 204), 'White', screen)