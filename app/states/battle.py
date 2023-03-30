import pygame as pg
from data import GFX
from states.states import _State
from objects import Button, Grid, Spirit, Unit

# Sprite Group
sprites = pg.sprite.RenderUpdates()
units = pg.sprite.RenderUpdates()  # Use a different sprite group type?


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

test_sprite = Unit(GFX['units']['mage'], (35, 35))
grid.set_sprite(test_sprite, (0, 0))
sprites.add(test_sprite)
units.add(test_sprite)


turtle = Spirit(GFX['spirits']['turtle'], (125, 150))
turtle.set_pos((0, 250))
turtle.set_effect(['move'])
print("TURTLE", turtle.get_effect())
sprites.add(turtle)

bee = Spirit(GFX['spirits']['bee'], (125, 150))
bee.set_pos((150, 250))
sprites.add(bee)


class Battle(_State):
    def __init__(self):
        super().__init__()
        self._bg = GFX['backgrounds']['floor']
        self.grid = grid
        self._sprite_group = sprites
        self._unit_group = units
        start_button.set_function(self.test_function)
        self.released_sprite = None
        self.active_sprite = None

    def test_function(self):
        self.next_state = "start"

    def sprite_released(self, released_sprite):
        """Effect of a released sprite."""
        print(released_sprite == turtle)
        print("SPRITE IS", released_sprite, released_sprite.get_effect())

        if self.active_sprite:
            effects = released_sprite.effect
            for effect in effects:
                if effect == 'move':
                    grid.move_sprite(self.active_sprite, [0, 1])

    def sprite_active(self, active_sprite):
        self.active_sprite = active_sprite

    def get_unit_group(self):
        return self._unit_group


# Sprite creation needs encapsulated so it doesn't run at start
# Can also probably better design grid making functions (18-24)
# This state needs remade multiple times.
# Need a function/inputs page to feed into this for orgainzation
# For example, file includes all sprite GFX and positions
# This would become a single input on this page
# Function would then split this up and call all the needed function to pos

# TODO
# Refactor how objects inherit and function
