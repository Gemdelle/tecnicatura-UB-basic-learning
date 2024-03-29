import pygame

from ui.utils.resource_path_util import resource_path
from ui.utils.throttle import throttle


class Image:

    def __init__(self, screen, x, y, width, height, img, action):
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.img = img
        self.action = action
        self.width = width
        self.height = height
        self.active = False

    def draw(self):
        info_img = pygame.image.load(resource_path(self.img)).convert_alpha()
        info_img = pygame.transform.scale(info_img, (self.width, self.height))

        self.screen.blit(info_img, self.rect)

    def check_click(self):
        mouse_buttons = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND))
            if mouse_buttons[0]:
                self.action()
        else:
            pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))

    def check_mouse_over(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND))
            if not self.active:
                self.action()
                self.active = True
        else:
            self.mark_inactive()

    def mark_inactive(self):
        pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))
        self.active = False