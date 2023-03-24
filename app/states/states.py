class _State:
    def __init__(self):
        self._bg = None
        self._sprite_group = None
        self.next_state = None

    def get_event(self, event):
        pass

    def get_bg(self):
        return self._bg

    def get_sprite_group(self):
        return self._sprite_group
