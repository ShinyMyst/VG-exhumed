import pygame as pg
from data import GFX
from states.states import _State
from objects import Button, Grid, Spirit, Unit


###############
# Define Sprites
##############
sprite_input = [
    # Buttons
    {
        'type': 'buttons',
        'img_name': 'start',
        'size': (200, 100),
        'position': (0, 0),
        'function_name': 'start'},

    {
        'type': 'buttons',
        'img_name': 'start',
        'size': (200, 100),
        'position': (300, 300),
        'function_name': 'process_turn'},

    # Spirits
    {
        'type': 'spirits',
        'img_name': 'turtle',
        'size': (125, 150),
        'position': (0, 250),
        'effect': "move"},

    {
        'type': 'spirits',
        'img_name': 'bee',
        'size': (125, 150),
        'position': (300, 300),
        'effect': None},

    # Sprites on Grid
    {
        'type': 'units',
        'img_name': 'mage',
        'size': (35, 35),
        'position': (0, 0)}
]

##############
# Define Grid
##############
grid_input = {
    "tile_set": [GFX['tiles']['tile']],
    "tile_size": (50, 50),
    "grid_dimensions": (4, 3),
    "position": [50, 50]}


class Battle(_State):
    def __init__(self):
        super().__init__()
        self._bg = GFX['backgrounds']['floor']
        self.released_sprite = None
        self.active_sprite = None
        self.function_dict = {
            "start": self.test_function,
            "process_turn": self.process_turn
        }
        print("CALL")
        self.initialize_objects(sprite_input, grid_input)
        print("END CALL")

    def test_function(self):
        self.target_state = "start"

    def sprite_released(self, released_sprite):
        # If sprite is hovered when unit released, set spirit
        if self.active_sprite:
            self.active_sprite.set_spirit(released_sprite)

    def sprite_active(self, active_sprite):  # Delete
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
                        self.grid.move_sprite(unit, [1, 0])
            except: # noqa
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

# Spirit functions should be defined elsewhere
# Each type of spirit should have its own class w/spirit as parent.
# This removes need for setting effect
