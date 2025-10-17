import json
import pygame
import time
from game import Game
from utils import render, get_mouse
from start_screen import StartScreen
from start_screen import SettingsScreen

class App:
    """Основной класс-синглтон, управляет состояниями приложения, инстанс доступен остальным через game_context.app"""
    def __init__(self):
        pygame.init()
        with open('configs/config.json', 'r', encoding='utf-8') as cf:
            self.config = json.load(cf)
        self.display = pygame.display.set_mode((self.config["screen_width"], self.config["screen_height"]),
                                               (pygame.FULLSCREEN if self.config["fullscreen"] else 0))
        self.state = 'start_menu'  # Возможные состояния: start_menu, settings, game
        self.running = True
        self.game = None  # Будет инициализирован при входе в состояние 'game'
        self.start_menu = None  # Будет инициализирован при входе в состояние 'start_menu'
        self.settings_menu = None  # Будет инициализирован при входе в состояние 'settings'

    def run(self):
        """Главный цикл приложения, переключается между состояниями"""
        while self.running:
            if self.state == 'start_menu':
                if not self.start_menu:
                    self.start_menu = StartScreen(self.display, self.config)
                self.start_menu.run()
            elif self.state == 'settings':
                if not self.settings_menu:
                    self.settings_menu = SettingsScreen(self.display, self.config)
                self.settings_menu.run()
            elif self.state == 'game':
                if not self.game:
                    self.game = Game(self.display, self.config)
                self.game.run()

    def change_state(self, new_state):
        """Меняет текущее состояние приложения"""
        if new_state in ['start_menu', 'settings', 'game', 'exit']:
            # Очистка предыдущего состояния
            if new_state != 'start_menu':
                self.start_menu = None
            if new_state != 'settings':
                self.settings_menu = None
            if new_state != 'game':
                self.game = None
            self.state = new_state