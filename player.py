class Player:
    def __init__(self, flagset):
        self.flags = flagset
        self.inventory = []

    def flip_flag(self, flag):
        """Переключает флаг"""
        if flag in self.flags:
            self.flags[flag] = not self.flags[flag]
        else:
            self.flags[flag] = True

    def increase_flag(self, flag, val=1):
        """Увеличивает флаг"""
        if flag in self.flags:
            self.flags[flag] += val
        else:
            self.flags[flag] = 1
