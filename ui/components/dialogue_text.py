import pygame

from ui.utils.resource_path_util import resource_path


class DialogueText:
    def __init__(self, screen, x, y, width, height, typed_text):
        self.font = pygame.font.Font(resource_path('font\\White Storm.ttf'), 40)
        self.x = x
        self.y = y
        self.text_surface = self.font.render(typed_text, True, (82, 82, 72))
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        self.screen.blit(self.text_surface, self.rect)