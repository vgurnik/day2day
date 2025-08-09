import game_context


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
        """Загружает ресурсы для экрана из словаря. Ресурсы наверное будут определены классами
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
