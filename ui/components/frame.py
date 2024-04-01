import pygame
class Frame:
    def __init__(self, screen, x, y, width, height, border_color, img=None):
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.elements = []
        self.border_color = border_color
        self.img = img
        self.width = width
        self.height = height

    def add_element(self, element):
        self.elements.append(element)

    def remove_element(self, element):
        self.elements.remove(element)

    def draw(self):
        if self.img is not None:
            scaled_image = pygame.transform.scale(self.img, (self.width, self.height))
            self.screen.blit(scaled_image, self.rect)
        else:
            pygame.draw.rect(self.screen, self.border_color, self.rect, border_radius=10)
            pygame.draw.rect(self.screen, (255, 255, 255), self.rect.inflate(-6, -6), border_radius=6)
        for element in self.elements:
            element.draw()