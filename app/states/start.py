import pygame as pg
from data import GFX
from states.states import _State
from objects import Button

# Sprite Group
start_sprites = pg.sprite.RenderUpdates()

###############
# Create Sprites
##############
start_button = Button(GFX['buttons']['start'], (200, 100))
start_button.set_pos((0, 0))
start_sprites.add(start_button)


class Start(_State):
    def __init__(self):
        super().__init__()
        self._bg = GFX['backgrounds']['back_cave']
        self._sprite_group = start_sprites
        start_button.set_function(self.test_function)

    def test_function(self):
        self.next_state = "battle"

# TODO:
# There may be a cleaner way to add sprites to a group in future
# Wait until there are more complex examples
# Remove need for states.states
