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
# IDK which inputs are what next day (such as which is tile size)
# Change this up for clarity

test_sprite = Button(GFX['units']['mage'], (35, 35))
grid.set_sprite(test_sprite, (0, 0))
sprites.add(test_sprite)

turtle = Button(GFX['spirits']['turtle'], (125, 150))
turtle.set_pos((0, 250))
sprites.add(turtle)


bee = Button(GFX['spirits']['bee'], (125, 150))
bee.set_pos((150, 250))
sprites.add(bee)


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
# This state needs remade multiple times.
# Need a function/inputs page to feed into this for orgainzation
# For example, file includes all sprite GFX and positions
# This would become a single input on this page
# Function would then split this up and call all the needed function to pos
