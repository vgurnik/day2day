import pygame
import game_context


class Visual:
    """Базовый класс для визуальных элементов"""
    def __init__(self, position, sprite_dict, default=None):
        self.active = True
        self.position = position
        if isinstance(sprite_dict, dict):
            self.sprites = sprite_dict
            self.sprite = sprite_dict[default]
        else:
            self.sprite = sprite_dict

    def set_state(self, state):
        """Обновляет состояние визуального элемента"""
        self.sprite = self.sprites.get(state, None)

    def draw(self, surface):
        """Отрисовывает визуальный элемент на заданном surface"""
        surface.blit(self.sprite, self.position)


class ScreenArea:
    """Базовый класс для определения интерактивной области экрана"""
    def __init__(self, mask, mask_color, visual, active=True):
        # Наверное маску взаимодействия можно сделать для каждого экрана цветной картинкой с зонами
        self.mask = mask == mask_color
        self.active = active
        self.visual = visual

    def activate(self):
        """Активирует область, делает её интерактивной"""
        self.active = True

    def deactivate(self):
        """Деактивирует область"""
        self.active = False

    def is_point_inside(self, point):
        """Проверяет, находится ли точка внутри области"""
        pass


class Button(ScreenArea):
    """Кнопка, которая может быть нажата"""
    def __init__(self, mask, mask_color, visual, action):
        super().__init__(mask, mask_color, visual)
        self.action = action  # Действие при нажатии кнопки

    def click(self):
        """Выполняет действие при нажатии на кнопку"""
        pass


def load_elements(resources):
    """Загружает элемент из словаря ресурсов, возвращает объект соответствующего класса"""
    elements = {}
    for element in resources:
        if element['type'] == 'visual':
            image = pygame.image.load(element['image'])
            elements[element['name']] = Visual(element['position'], image)
        elif element['type'] == 'button':
            button_visual = Visual(element['position'], element['image'])
            elements[element['name']] = Button(element['mask'], element['mask_color'], button_visual, element['action'])
    return elements


class BaseGameScreen:
    """Базовый класс для экранов игры, содержит основные методы и атрибуты, которые могут быть переопределены в наследниках если надо будет"""
    def __init__(self, resources):
        self.is_active = False
        self.elements = load_elements(resources["elements"])

    def activate(self):
        """Запустить экран, активировать все элементы которые нужно"""
        self.is_active = True

    def deactivate(self):
        """Деактивировать экран"""
        self.is_active = False

    def update(self, dt):
        """Обновить состояние экрана, активировать и деактивировать элементы, обработать события"""

    def draw(self):
        """Отрисовать экран на Game.screen"""
        g = game_context.game
        g.screen.fill((0, 0, 0, 0))
        for element in self.elements.values():
            if element.active:
                element.draw(g.screen)
        ...
