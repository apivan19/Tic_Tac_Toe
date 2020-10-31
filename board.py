class Board:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        self.board_layout = [None for i in range(9)]


b1 = Board()
b1.board_layout