class _Logic(self):
    def __init__(self):
        # Sprite Groups
        self.buttons = None
        self.grid = None
        self.spirits = None
        self.units = None
        self.all_sprites = None

        self.events = {
            "click": self.click,
            "release": self.release}

    def sync_sprites(self, buttons, spirits, units, all_sprites, grid):
        """Updates all sprite groups."""
        self.buttons = buttons
        self.spirits = spirits
        self.units = units
        self.all_sprites = all_sprites
        self.grid = grid


    #####################
    # Types of Events
    #####################
