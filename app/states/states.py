class _State:
    def __init__(self):
        self._bg = None
        self._sprite_group = None
        self._target_state = None

    def get_event(self, event):
        pass

    def get_bg(self):
        return self._bg

    def get_sprite_group(self):
        return self._sprite_group

    def set_target_state(self, state:str):
        self._target_state = state

    def get_target_state(self):
        return self._target_state

# Set up states to only initiate when used and to clear otherwise.