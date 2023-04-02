from data import GFX
from states.states import _State

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

    def change_states(self):
        self.target_state = "start"



    #####################
    # Logic Functions
    #####################
    def get_event(self, event: str):
        """Takes an event from control and processes through logic."""
        self.logic.process_event(event)



class BattleLogic:
    def __init__(self):
        self.buttons = None
        self.spirits = None
        self.units = None
        self.all_sprites = None
        self.grid = None

        self.events = {
            "click": self.click,
            "release": self.release
        }

        self.released_sprite = None
        self.active_sprite = None

    def sync_sprites(self, buttons, spirits, units, all_sprites, grid):
        self.buttons = buttons
        self.spirits = spirits
        self.units = units
        self.all_sprites = all_sprites
        self.grid = grid

    def process_event(self, event_type):
        action = self.events[event_type]
        action()
        self.active()

    def click(self):
        """Pass click to all clickable sprites"""
        for button in self.buttons:
            button.click()
        for spirits in self.spirits:
            spirits.click()

    def release(self):
        """Pass release to all sprites with release function"""
        for spirit in self.spirits:
            if spirit.release():
                self.released_sprite = spirit

    def active(self):
        if self.released_sprite:
            for sprite in self.units:
                if sprite._is_hovered:
                    sprite.set_spirit(self.released_sprite)
            self.released_sprite = None

    def process_turn(self):
        """Performs spirit actions and enemy phase."""
        for unit in self.units:
            try:
                actions = unit.execute_turn()
                for action in actions:
                    if action == "move":
                        self.grid.move_sprite(unit, [1, 0])
            except: # noqa
                pass

    def sprite_released(self, released_sprite):
        # If sprite is hovered when unit released, set spirit
        if self.active_sprite:
            self.active_sprite.set_spirit(released_sprite)

# TODO
# STATE should only hold info about what is in current state.
# Sprites should only hold info about what they hold and not execute logic
# Grid should exist only to get grid cells and not logic in finding things

# Spirit functions should be defined elsewhere
# Each type of spirit should have its own class w/spirit as parent.
# This removes need for setting effect

# State still initiated at start.  Need a way to plug inputs via control
# Perhaps add the input parameters in the state change variable?

# BETTER SPRITE GROUP MANAGE
# Object class for click and drag objects?

# Implement logic module
# Logic should handle events.  State holds sprites
# Logic will execute commands on state.
# So control should call logic?  Which in turn changes state?