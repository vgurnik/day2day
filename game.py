import json
import pygame

from player import Player


class Game:
    """Основной класс-синглтон, управляет геймплеем и главной отрисовкой, инстанс доступен остальным через game_context.game"""
    def __init__(self):
        pygame.init()
        with open('configs/config.json', 'r', encoding='utf-8') as cf:
            self.config = json.load(cf)
        self.display = pygame.display.set_mode((self.config["screen_width"], self.config["screen_height"]),
                                               (pygame.FULLSCREEN if self.config["fullscreen"] else 0))
        self.screen = pygame.Surface(self.config["base_resolution"], pygame.SRCALPHA)
        self.current_screen = None
        self.running = True
        self.player = Player(self.config["start_flags"])

    def run(self):
        """Обрабатывает игровой цикл"""
        while self.running:
            self.update()
            self.draw()

    def update(self):
        """Обновляет события и состояния скринов и игрока"""

    def draw(self):
        """Отрисовывает screen на display. На screen рисуется все в FHD, display масштабируется под реальный размер окна"""
        screen_size = (self.config["screen_width"], self.config["screen_height"])
        aspect = self.config["base_resolution"][1] / self.config["base_resolution"][0]
        if screen_size[1] / screen_size[0] == aspect:
            self.display.blit(pygame.transform.scale(self.screen, screen_size), (0, 0))
        elif screen_size[1] / screen_size[0] > aspect:
            diff = round(screen_size[1] - screen_size[0] * aspect)
            self.display.blit(pygame.transform.scale(self.screen, (screen_size[0], screen_size[1] - diff)),
                              (0, diff // 2))
        else:
            diff = round(screen_size[0] - screen_size[1] / aspect)
            self.display.blit(pygame.transform.scale(self.screen, (screen_size[0] - diff, screen_size[1])),
                              (diff // 2, 0))
        pygame.display.flip()

    def stop(self):
        """Останавливает игровой цикл для выхода 'в меню', меню пока не делалось, если делать то запускать в main"""
        self.running = False
