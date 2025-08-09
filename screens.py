import game_context


class BaseGameScreen:
    def __init__(self):
        self.is_active = False
        self.buttons = []
        self.transitions = []
        self.pickups = []
        self.interactables = []
        self._visuals = []

    def load(self, resources):
        self.buttons = resources.get("buttons", [])
        self.transitions = resources.get("transitions", [])
        self.pickups = resources.get("pickups", [])
        self.interactables = resources.get("interactables", [])
        self._visuals = resources.get("visuals", [])

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False

    def update(self, delta_time):
        pass

    def draw(self):
        g = game_context.game
        g.screen.fill((0, 0, 0, 0))
        for visual in self._visuals:
            g.screen.blit(visual.image, visual.rect)
        ...
