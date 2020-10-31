import random


class Player:

    # List Holding a 1 and 2 for the initiative.
    initiative_possibilities = [1, 2]

    # List Holding the symbols that have not been taken yet
    symbols_available = ["O", "X"]

    # List Holding the two player instances
    player_instances = []

    def __init__(self):
        self.initiative_score = random.choice(Player.initiative_possibilities)
        Player.initiative_possibilities.remove(self.initiative_score)

        self.symbol = random.choice(Player.symbols_available)
        Player.symbols_available.remove(self.symbol)

        Player.player_instances.append(self)

    # Destructor Method for when the player instances are deleted.
    def __del__(self):
        Player.initiative_possibilities.append(self.self.initiative_score)
        Player.symbols_available.append(self.symbol)

    # Function for a human player to make a move
    def make_move(self, 