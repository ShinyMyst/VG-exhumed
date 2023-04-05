from data import GFX
from states.states import _State
from logic.combat import CombatLogic
from spirits import turtle

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

        self.function_dict = {
            "start": self.change_states,
            "process_turn": self.next_turn
        }

        self.initialize_objects(sprite_input, grid_input)
        self.logic = CombatLogic(self.grid)
        self.logic.sync_sprites(self.buttons, self.spirits, self.units,
                                self.all_sprites, self.grid)

    #####################
    # Button Functions
    #####################
    def change_states(self):
        print("CHANGE STATE")
        self.target_state = "start"

    def next_turn(self):
        self.logic.process_turn()

# Try to remove sprites from logic

# TODO
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

# Update super state
# Try to remove sprites from logic
# Main issue with this is iterating through all units w/o list
# Perhaps have state iterate through all units for logic somehow
# Consider making grids and sprite groups data varialbes
# Catch out of bounds moves
# State more or less is just the gate keeper for which logic to use
# State also stores the sprite info... for now.
# Logic is more or less an offshoot of state.  It's still
# technically state functionality, just seperated for readability.
# State holds sprites and it holds logic

# Put initialization arguments in class defintion.  So that groups are passed
# when initialized autoamatically.

# Different way to pass objects to logic
# Create a default logic class?