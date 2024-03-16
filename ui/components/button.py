import pygame


class Button:
    def __init__(self, screen, x, y, width, height, text, text_color, color, action):
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.text_color = text_color
        self.color = color
        self.action = action

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect, 2)

        text_surface = pygame.font.Font('font/Alkhemikal.ttf', 25).render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)

        self.screen.blit(text_surface, text_rect)

    def check_click(self):
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                self.action()