from game import Game
import pygame
import json

if __name__ == "__main__":
    pygame.init()
    with open('configs/config.json', 'r', encoding='utf-8') as cf:
        config = json.load(cf)
    display = pygame.display.set_mode((config["screen_width"], config["screen_height"]),
                                      (pygame.FULLSCREEN if config["fullscreen"] else 0))
    import game_context
    game_context.game = Game(display, config)
    game_context.game.run()