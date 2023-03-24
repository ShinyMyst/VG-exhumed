import pygame as pg
from data import GFX
from states.states import _State
from objects import Button

# Sprite Group
sprites = pg.sprite.RenderUpdates()

###############
# Create Sprites
##############
start_button = Button(GFX['buttons']['start'], (200, 100))
start_button.set_pos((50, 50))
sprites.add(start_button)


class Battle(_State):
    def __init__(self):
        super().__init__()
        self._bg = GFX['backgrounds']['floor']
        self._sprite_group = sprites
        start_button.set_function(self.test_function)

    def test_function(self):
        self.next_state = "start"
