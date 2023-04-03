from _spirits import SpiritActions
from _logic import _Logic

class CombatLogic(_Logic):
    def __init__(self):
        super().__init__()
        # SHARED
        self.buttons = None
        self.spirits = None
        self.units = None
        self.all_sprites = None
        self.grid = None

        self.action = SpiritActions(self.grid)

        # SHARED
        self.events = {
            "click": self.click,
            "release": self.release
        }

        self.released_sprite = None
        self.active_sprite = None

        self.actions = {
            "forward": self._foward
        }

    # SHARED
    def sync_sprites(self, buttons, spirits, units, all_sprites, grid):
        self.buttons = buttons
        self.spirits = spirits
        self.units = units
        self.all_sprites = all_sprites
        self.grid = grid

    # SHARED
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



    #####################
    # Actions
    #####################
    def process_turn(self):
        """Performs spirit actions and enemy phase."""
        for unit in self.units:
            try:
                spirit = unit.get_spirit()
                effects = spirit.get_effects()
                for effect in effects:
                    self.action.execute(effect, unit)
            except: # noqa
                pass

    def sprite_released(self, released_sprite):
        # If sprite is hovered when unit released, set spirit
        if self.active_sprite:
            self.active_sprite.set_spirit(released_sprite)