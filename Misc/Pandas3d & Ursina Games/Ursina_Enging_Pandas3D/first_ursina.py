# Written in Python 3.7

# My first attempt at using the Ursina Engine

from ursina import *

app = Ursina()

player = Entity(model="cube", color=color.orange, scale_y=2)


def update():  # update gets automatically called.
    player.x += held_keys["d"] * 0.1
    player.x -= held_keys["a"] * 0.1
    player.y += held_keys["w"] * 0.1
    player.y -= held_keys["s"] * 0.1


app.run()
