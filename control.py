######################
# Controller
######################
"""
...
"""
from states import STATES

class Control():
    def __init__(self):
        self.state_dict = STATES
        self.current_state = self.state_dict['start']

    def init_states(self, state_dict: dict, start_state: str):
        """Saves the completed state dict and saves the current state"""
        self.state_dict = state_dict
        self.current_state = self.state_dict[start_state]

    def event_loop(self):
        while True:
            pass

    def get_gfx(self):
        """Returns the background and sprite group for current state"""
        background = self.current_state.get_bg()
        sprites = self.current_state.get_sprite_group()
        return background, sprites
