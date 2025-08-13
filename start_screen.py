import pygame
import sys

class StartButton:
    def __init__(self, x, y, text, font, img_normal, img_pressed, action=None):
        self.x = x
        self.y = y
        self.text = text
        self.font = font
        self.img_normal = img_normal
        self.img_pressed = img_pressed
        self.cur_img = self.img_normal
        self.rect = self.cur_img.get_rect(topleft=(x,y))
        self.action = action
        self.pressed = False
        self.text_surf = font.render(text, True, "Black")
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def draw(self, screen):
        screen.blit(self.cur_img, self.rect)
        screen.blit(self.text_surf, self.text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.cur_img = self.img_pressed
            self.pressed = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.pressed and self.rect.collidepoint(event.pos):
                self.action()
            self.pressed = False
            self.cur_img = self.img_normal


class StartScreen:
    def __init__(self, display, config):
        self.bg_image = pygame.image.load(config["bg_img_start"])
        self.buttons = []
        self.display = display
        self.config = config
        self.font = pygame.font.Font(config["font"], config["font_size_start"])
        self.but_img_normal = pygame.image.load(config["but_img_norm_start"])
        self.but_img_pressed = pygame.image.load(config["but_img_norm_start"])

    def add_button(self, button):
        self.buttons.append(button)

    def draw(self, screen):
        screen.blit(self.bg_image, (0,0))
        for btn in self.buttons:
            btn.draw(screen)

    def handle_event(self, event):
        for btn in self.buttons:
            btn.handle_event(event)