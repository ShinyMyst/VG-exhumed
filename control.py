######################
# Controller
######################
"""
...
"""


class Control():
    def __init__(self):
        self.state_dict = dict()
        self.current_state = None

    def init_states(self, state_dict: dict, start_state: str):
        """Saves the completed state dict and saves the current state"""
        self.state_dict = state_dict
        self.current_state = self.state_dict[start_state]

    def event_loop(self):
        while True:
            pass
