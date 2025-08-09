import json
import pygame


class Game:
    def __init__(self):
        pygame.init()
        with open('configs/config.json', 'r', encoding='utf-8') as cf:
            self.config = json.load(cf)
        self.display = pygame.display.set_mode((self.config["screen_width"], self.config["screen_height"]),
                                               (pygame.FULLSCREEN if self.config["fullscreen"] else 0))
        self.screen = pygame.Surface(self.config["base_resolution"], pygame.SRCALPHA)
        self.current_screen = None
        self.running = True

    def run(self):
        while self.running:
            self.update()
            self.draw()

    def update(self):
        pass

    def draw(self):
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
        self.running = False
