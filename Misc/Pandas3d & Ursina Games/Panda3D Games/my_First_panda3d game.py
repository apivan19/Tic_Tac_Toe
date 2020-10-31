from direct.showbase.ShowBase import ShowBase

# Begin Defining your Game
class MyGame(ShowBase):
    def __init__(self):
        super().__init__()

# Instantiate the Game / App base
game = MyGame()

# Start the game
game.run()