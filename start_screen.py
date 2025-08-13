import time
import pygame
from game import Game
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

    def draw(self, display):
        display.blit(self.cur_img, self.rect)
        display.blit(self.text_surf, self.text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.cur_img = self.img_pressed
                self.pressed = True
                self.text_rect.move_ip(0, 5)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.pressed:
                self.text_rect.move_ip(0, -5)
                if self.rect.collidepoint(event.pos) and self.action:
                    self.action()
            self.pressed = False
            self.cur_img = self.img_normal


class VolumeBar:
    def __init__(self, x, y, bar_width, bar_height, gap, text, font, config, volume_max=10):
        self.x = x
        self.y = y
        self.bar_width = bar_width
        self.bar_height = bar_height
        self.gap = gap
        self.volume_max = volume_max
        self.rect = None
        self.text_surf = font.render(text, True, "Black")
        self.config = config

        pygame.mixer.music.set_volume(self.config["volume_level"] / self.volume_max)

    def draw(self, screen):
        for i in range(self.volume_max):
            self.rect = pygame.Rect(
                self.x + i * (self.bar_width + self.gap),
                self.y,
                self.bar_width,
                self.bar_height
            )
            if i < self.config["volume_level"]:
                pygame.draw.rect(screen, self.config["volume_bar_color"], self.rect)
            else:
                pygame.draw.rect(screen, "Black", self.rect, self.config["volume_bar_border"])
        total_width = self.volume_max * self.bar_width + (self.volume_max - 1) * self.gap
        text_x = self.x + (total_width - self.text_surf.get_width()) // 2
        text_y = self.y + self.bar_height + self.gap
        screen.blit(self.text_surf, (text_x, text_y))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = event.pos
            for i in range(self.volume_max):
                self.rect = pygame.Rect(
                    self.x + i * (self.bar_width + self.gap),
                    self.y,
                    self.bar_width,
                    self.bar_height
                )
                if self.rect.collidepoint(mx, my):
                    self.config["volume_level"] = i + 1
                    pygame.mixer.music.set_volume(self.config["volume_level"] / self.volume_max)
                    break


class StartScreen:
    def __init__(self, display, config):
        self.bg_image = pygame.image.load(config["bg_img"])
        self.buttons = []
        self.display = display
        self.config = config
        self.font = pygame.font.Font(config["font"], config["font_size_start"])

        normal = pygame.image.load(config["btn_img_norm_start"])
        pressed = pygame.image.load(config["btn_img_press_start"])
        btn_width, btn_height = normal.get_size()
        self.btn_img_normal = pygame.transform.scale(normal, (int(btn_width*1.5), int(btn_height*1.5)))
        self.btn_img_pressed = pygame.transform.scale(pressed, (int(btn_width*1.5), int(btn_height*1.5)))

        self.add_button(StartButton(
            x=config["btn_x"],
            y=config["btn_y_1"],
            text=config["btn_text_play"],
            font=self.font,
            img_normal=self.btn_img_normal,
            img_pressed=self.btn_img_pressed,
            action=lambda: btn_play_action(self.display, self.config)
        ))
        self.add_button(StartButton(
            x=config["btn_x"],
            y=config["btn_y_2"],
            text=config["btn_text_settings"],
            font=self.font,
            img_normal=self.btn_img_normal,
            img_pressed=self.btn_img_pressed,
            action=lambda: btn_settings_action(self.display, self.config)
        ))
        self.add_button(StartButton(
            x=config["btn_x"],
            y=config["btn_y_3"],
            text=config["btn_text_exit"],
            font=self.font,
            img_normal=self.btn_img_normal,
            img_pressed=self.btn_img_pressed,
            action=lambda: btn_exit_action(self)
        ))

        self.running = True


    def add_button(self, button):
        self.buttons.append(button)

    def draw(self):
        self.display.blit(self.bg_image, (0,0))
        for btn in self.buttons:
            btn.draw(self.display)
        pygame.display.flip()

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            btn_exit_action(self)
        for btn in self.buttons:
            btn.handle_event(event)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)
            self.draw()
            time.sleep(0.01)


class SettingsScreen:
    def __init__(self, display, config):
        self.display = display
        self.config = config
        self.widgets = []
        self.font = pygame.font.Font(config["font"], config["font_size_start"])
        self.bg_image = pygame.image.load(config["bg_img"])

        normal = pygame.image.load(config["btn_img_norm_start"])
        pressed = pygame.image.load(config["btn_img_press_start"])
        btn_width, btn_height = normal.get_size()
        self.btn_img_normal = pygame.transform.scale(normal, (btn_width * 1.5, btn_height * 1.5))
        self.btn_img_pressed = pygame.transform.scale(pressed, (btn_width * 1.5, btn_height * 1.5))

        self.add_widget(StartButton(
            x=config["btn_x"],
            y=config["btn_y_2"],
            text=config["btn_text_back"],
            font=self.font,
            img_normal=self.btn_img_normal,
            img_pressed=self.btn_img_pressed,
            action=lambda: btn_back_action(self)
        ))

        self.add_widget(VolumeBar(
            x=config["btn_x"],
            y=config["btn_y_1"],
            bar_width=config["volume_bar_width"],
            bar_height=config["volume_bar_height"],
            gap=config["volume_bar_gap"],
            text=config["volume_bar_text"],
            font=self.font,
            config=self.config
        ))

        self.running = True

    def add_widget(self, widget):
        self.widgets.append(widget)

    def draw(self):
        self.display.blit(self.bg_image, (0, 0))
        for wg in self.widgets:
            wg.draw(self.display)
        pygame.display.flip()

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            btn_exit_action(self)
        for wg in self.widgets:
            wg.handle_event(event)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)
            self.draw()
            time.sleep(0.01)

def btn_play_action(display, config):
    import game_context
    game_context.game = Game(display, config)
    game_context.game.run()

def btn_settings_action(display, config):
    settings_screen = SettingsScreen(display, config)
    settings_screen.run()

def btn_back_action(screen_obj):
    screen_obj.running = False

def btn_exit_action(screen_obj):
    screen_obj.running = False
    pygame.quit()
    sys.exit(0)