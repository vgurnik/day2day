from start_screen import StartScreen
import pygame
import json

if __name__ == "__main__":
    pygame.init()
    with open('configs/config.json', 'r', encoding='utf-8') as cf:
        config = json.load(cf)
    display = pygame.display.set_mode((config["screen_width"], config["screen_height"]),
                                      (pygame.FULLSCREEN if config["fullscreen"] else 0))
    start_menu = StartScreen(display, config)
    start_menu.run()