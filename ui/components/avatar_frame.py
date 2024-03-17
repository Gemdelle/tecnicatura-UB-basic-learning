import pygame

class AvatarFrame:
    def __init__(self, screen, x, y, width, height, color):
        self.x = x
        self.y = y
        self.screen = screen
        self.color = color
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.height // 2), 150, self.width)
