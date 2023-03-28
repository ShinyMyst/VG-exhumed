import pygame as pg
from data import GFX
from states.states import _State
from objects import Button, Grid

# Sprite Group
sprites = pg.sprite.RenderUpdates()


###############
# Create Sprites
##############
start_button = Button(GFX['buttons']['start'], (200, 100))
start_button.set_pos((0, 0))
sprites.add(start_button)


tiles = [GFX['tiles']['tile']]
grid = Grid(tiles, (50, 50))
grid.generate_grid((4, 3), [50, 50])
grid_sprites = grid.get_sprites()
print("THIS IS RUNNING BEFORE USED")
for sprite in grid_sprites:
    sprites.add(sprite)


class Battle(_State):
    def __init__(self):
        super().__init__()
        self._bg = GFX['backgrounds']['floor']
        self._sprite_group = sprites
        start_button.set_function(self.test_function)

    def test_function(self):
        self.next_state = "start"


# Sprite creation needs encapsulated so it doesn't run at start
# Can also probably better design grid making functions (18-24)
