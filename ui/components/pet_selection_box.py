import pygame
from enum import Enum

class PetSelectionBox:
    def __init__(self, screen, x, y, width, height, pet_img, pet_selection_id):
        self.x = x
        self.y = y
        self.character_selection_id = pet_selection_id
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.personaje = pygame.transform.scale(pet_img.convert_alpha(), (width, height))

    def draw(self):
        self.screen.blit(self.personaje, self.rect)

class PetSelectionID(Enum):
    ORKY = 1
    HUNNY = 2
    TOBI = 3
