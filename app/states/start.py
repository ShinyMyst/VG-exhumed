import pygame as pg
from data import GFX
from states.states import _State
from objects import Button
from logic._logic import _Logic

# Sprite Group
start_sprites = pg.sprite.RenderUpdates()

###############
# Create Sprites
##############
start_button = Button(GFX['buttons']['start'], (200, 100))
start_button.set_pos((0, 0))
start_sprites.add(start_button)
sprite_input = [
    {
        'type': 'buttons',
        'img_name': 'start',
        'size': (200, 100),
        'position': (0, 0),
        'function_name': 'start'},
]


class Start(_State):
    def __init__(self):
        super().__init__()
        self._bg = GFX['backgrounds']['back_cave']

        self.function_dict = {
            "start": self.test_function
        }

        self.initialize_objects(sprite_input)
        self.logic = _Logic()
        self.logic.sync_sprites(self.buttons, self.spirits, self.units,
                                self.all_sprites, self.grid)

    #####################
    # Button Functions
    #####################
    def test_function(self):
        self.target_state = "battle"

# TODO:
# There may be a cleaner way to add sprites to a group in future
# Wait until there are more complex examples
# Remove need for states.states
