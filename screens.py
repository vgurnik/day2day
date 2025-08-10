import game_context


class Visual:
    """Базовый класс для визуальных элементов"""
    def __init__(self, sprite_dict, default=None):
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
        pass


class ScreenArea:
    """Базовый класс для определения интерактивной области экрана"""
    def __init__(self, mask, mask_color, visual, active=False):
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
    def __init__(self, mask, mask_color, action):
        super().__init__(mask, mask_color)
        self.action = action  # Действие при нажатии кнопки

    def click(self):
        """Выполняет действие при нажатии на кнопку"""
        pass


class Transition(ScreenArea):
    """Переход на другой экран по клику"""
    def __init__(self, mask, mask_color, new_screen):
        super().__init__(mask, mask_color)
        self.new_screen = new_screen  # Действие при нажатии кнопки

    def click(self):
        """Переход на новый экран"""
        pass


class BaseGameScreen:
    """Базовый класс для экранов игры, содержит основные методы и атрибуты, которые могут быть переопределены в наследниках если надо будет"""
    def __init__(self):
        self.is_active = False
        self.buttons = []
        self.transitions = []
        self.pickups = []
        self.interactables = []
        self._visuals = []

    def load(self, resources):
        """Загружает ресурсы для экрана из словаря
        buttons - кнопки, т.е. можно нажать и что-то произойдет
        transitions - переходы, по нажатию перейти на другой экран
        pickups - предметы, которые можно подобрать
        interactables - места куда можно применить предмет
        visuals - визуальные элементы, которые просто отрисовываются на экране включая фон и аниматоры"""
        self.buttons = resources.get("buttons", [])
        self.transitions = resources.get("transitions", [])
        self.pickups = resources.get("pickups", [])
        self.interactables = resources.get("interactables", [])
        self._visuals = resources.get("visuals", [])

    def activate(self):
        """Запустить экран, активировать все элементы которые нужно"""
        self.is_active = True

    def deactivate(self):
        """Деактивировать экран"""
        self.is_active = False

    def update(self, delta_time):
        """Обновить состояние экрана, активировать и деактивировать элементы, обработать события"""

    def draw(self):
        """Отрисовать экран на Game.screen"""
        g = game_context.game
        g.screen.fill((0, 0, 0, 0))
        for visual in self._visuals:
            g.screen.blit(visual.image, visual.rect)
        ...
