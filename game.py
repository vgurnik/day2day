import json
import pygame
import time

from player import Player
from screens import BaseGameScreen
from utils import render


class Game:
    """Основной класс-синглтон, управляет геймплеем и главной отрисовкой, инстанс доступен остальным через game_context.game"""
    def __init__(self, display, config):
        self.display = display
        self.config = config
        self.screen = pygame.Surface(self.config["base_resolution"], pygame.SRCALPHA)
        with open(config['script'], 'r', encoding='utf-8') as cf:
            self.game_script = json.load(cf)
        self.screens = {}
        for screen_name, screen_data in self.game_script['screens'].items():
            self.screens[screen_name] = BaseGameScreen(screen_data)
        self.current_screen = self.screens[self.game_script['first_screen']]
        self.running = True
        self.player = Player(self.config["start_flags"])

    def run(self):
        """Обрабатывает игровой цикл"""
        clock = pygame.time.Clock()
        fps = 60
        dt = 1.0 / fps
        while self.running:
            self.update(dt)
            self.draw()
            dt = clock.tick(fps) / 1000
            # fps = clock.get_fps()

    def update(self, dt):
        """Обновляет события и состояния скринов и игрока"""
        self.current_screen.update(dt)

    def draw(self):
        """Отрисовывает screen на display. На screen рисуется все в FHD, display масштабируется под реальный размер окна"""
        self.current_screen.draw()
        render(self.display, self.screen, self.config["base_resolution"],
               (self.config["screen_width"], self.config["screen_height"]))
        pygame.display.flip()

    def stop(self):
        """Останавливает игровой цикл для выхода 'в меню', меню пока не делалось, если делать то запускать в main"""
        self.running = False
