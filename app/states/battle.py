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

turn_button = Button(GFX['buttons']['start'], (200, 100))
turn_button.set_pos((300, 300))
sprites.add(turn_button)

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
        turn_button.set_function(self.process_turn)
        self.released_sprite = None
        self.active_sprite = None

        sprite_types = {
            "Spirit": None,
            "Button": None,
            "Unit": None
        }

    def test_function(self):
        self.next_state = "start"

    def sprite_released(self, released_sprite):
        """Effect of a released sprite."""
        """
        if self.active_sprite:
            effects = released_sprite.effect
            for effect in effects:
                if effect == 'move':
                    grid.move_sprite(self.active_sprite, [1, 0])"""

        # If sprite is hovered when unit released, set spirit
        if self.active_sprite:
            self.active_sprite.set_spirit(released_sprite)

    def sprite_active(self, active_sprite): # Delete
        self.active_sprite = active_sprite

    def get_unit_group(self):
        return self._unit_group

    def process_turn(self):
        """Performs spirit actions and enemy phase."""
        for unit in self._unit_group:
            try:
                actions = unit.execute_turn()
                for action in actions:
                    if action == "move":
                        grid.move_sprite(unit, [1, 0])
            except: # noqa
                pass

    def add_sprite(sprite_type, position: tuple):
        pass

    def click(self):
        for sprite in self._sprite_group:
            sprite.click()

    def release(self):
        for sprite in self._sprite_group:
            if sprite.release():
                self.released_sprite = sprite

    def active(self):
        if self.released_sprite:
            for sprite in self._unit_group:
                if sprite._is_hovered:
                    sprite.set_spirit(self.released_sprite)
                    print("SET SPIRIT")
            self.released_sprite = None


# Where will the functions be added to buttons?
# Where will the actions be added to spirits??

# Sprite creation needs encapsulated so it doesn't run at start
# Can also probably better design grid making functions (18-24)
# This state needs remade multiple times.
# Need a function/inputs page to feed into this for orgainzation
# For example, file includes all sprite GFX and positions
# This would become a single input on this page
# Function would then split this up and call all the needed function to pos

# TODO
# Refactor how objects inherit and function

# STATE should only hold info about what is in current state.
# Sprites should only hold info about what they hold and not execute logic
# Grid should exist only to get grid cells and not logic in finding things

# Seperate some of these state functions into the base class
