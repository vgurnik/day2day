from game import Game

if __name__ == "__main__":
    import game_context
    game_context.game = Game()
    game_context.game.run()
