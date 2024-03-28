import os
import sys

import pygame

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
class DialogText:
    def __init__(self, screen, x, y, width, height, typed_text):
        self.font = pygame.font.Font(resource_path('font\\Alkhemikal.ttf'), 40)
        self.x = x
        self.y = y
        self.text_surface = self.font.render(typed_text, True, (0, 0, 0))
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        self.screen.blit(self.text_surface, self.rect)