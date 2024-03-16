import pygame
from enum import Enum

class CharacterSelectionBox:
    def __init__(self, screen, x, y, width, height, character_img, character_selection_id):
        self.x = x
        self.y = y
        self.character_selection_id = character_selection_id
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.personaje = pygame.transform.scale(character_img.convert_alpha(), (width, height))

    def draw(self):
        self.screen.blit(self.personaje, self.rect)

class CharacterSelectionID(Enum):
    PEPE = 1
    NORBERT = 2
    DORY = 3


class CharacterSelectionInput:
    def __init__(self, screen, x, y, width, height, text_input):
        self.x = x
        self.y = y
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.text_input = text_input

    def draw(self):
        font = pygame.font.Font('font/Alkhemikal.ttf', 25)
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect, 2)
        text_surface = font.render(self.text_input, True, (0, 0, 0))
        self.screen.blit(text_surface, self.rect)

