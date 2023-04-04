class _Logic():
    def __init__(self):
        # Sprite Groups
        self.buttons = None
        self.grid = None
        self.spirits = None
        self.units = None
        self.all_sprites = None

        self.hovered_sprite = None
        self.held_sprite = None

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

    def update(self, event_type, hovered_sprite, held_sprite):
        """Performs specified action"""
        self.hovered_sprite = hovered_sprite
        self.held_sprite = held_sprite

        event = self.events[event_type]
        event()
        self.execute_logic()

    #####################
    # Types of Events
    #####################
    def click(self):
        """Pass click command to the sprite being hovered."""
        if self.hovered_sprite:
            self.hovered_sprite.click()

    def release(self):
        """Pass release command to the sprite being held."""
        if self.held_sprite:
            self.held_sprite.release()

    #####################
    # Overwritten Functions
    #####################
    def execute_logic(self):
        """Overwritten in subclasses."""
        pass
