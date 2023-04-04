from data import GFX
from states.states import _State
from spirits import turtle, bee

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
        'img_name': turtle[0],
        'size': (125, 150),
        'position': (0, 250),
        'effect': turtle[1]},

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


##############
# Define State
##############
class Battle(_State):
    def __init__(self):
        super().__init__()
        self._bg = GFX['backgrounds']['floor']

        self.logic = BattleLogic()

        self.function_dict = {
            "start": self.change_states,
            "process_turn": self.logic.process_turn
        }
        self.initialize_objects(sprite_input, grid_input)
        self.logic.sync_sprites(self.buttons, self.spirits, self.units, self.all_sprites, self.grid)

        self.event = None
    #####################
    # Button Functions
    #####################
    def change_states(self):
        self.target_state = "start"


    #####################
    # Getters/Setters
    #####################
    def receive_event(self, event: str):
        """Takes an event from control and processes through logic."""
        self.event = event
        # self.logic.process_event(event)

    def update(self, event):
        """Updates variables and calls necessary logic when event received"""
        # Find which sprites are moving, which are hovered, and process event based on this info
        held_sprite = None
        hovered_sprite = None
        for sprite in self.all_sprites:
            if sprite.is_held:
                held_sprite = sprite
            if sprite.is_hovered:
                hovered_sprite = sprite

        self.logic.update(event, hovered_sprite, held_sprite)

        # Try to remove sprites from logic





# TODO
# Sprites should only hold info about what they hold and not execute logic
# Grid should exist only to get grid cells and not logic in finding things

# Spirit functions should be defined elsewhere
# Each type of spirit should have its own class w/spirit as parent.
# This removes need for setting effect

# State still initiated at start.  Need a way to plug inputs via control
# Perhaps add the input parameters in the state change variable?

# BETTER SPRITE GROUP MANAGE
# Object class for click and drag objects?


# Put logic in its own module with super class
# Create a click and drag class for spirit to inherit
# Squares should inherit basic object class.

# Pass sprite groups to logic better.
# Try class variable over instance variable


# Each state is assigned a logic class to process info.
# Logic class then initialized after state finished initializing
# Update flow chart.


# Use initialize objects for objects standard for all instances of class
 # Use another function to add additional sprites (for example the units)

 # Should DATA hold the sprite groups instead?  Becaue they're everywhere
 # Try that as refactor later.
