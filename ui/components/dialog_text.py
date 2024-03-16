import pygame


class DialogText:
    def __init__(self, screen, x, y, width, height, typed_text):
        self.font = pygame.font.Font('font/Alkhemikal.ttf', 40)
        self.x = x
        self.y = y
        self.text_surface = self.font.render(typed_text, True, (0, 0, 0))
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        self.screen.blit(self.text_surface, self.rect)