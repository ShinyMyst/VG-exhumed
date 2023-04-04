from _spirits import _SpiritActions
from _logic import _Logic


class CombatLogic(_Logic):
    def __init__(self):
        super().__init__()
        self.spirit_action = _SpiritActions(self.grid)
        self.released_sprite = None
        self.active_sprite = None

        self.hovered_sprite = None
        self.held_sprite = None


    # SHARED
    def update(self, event_type, hovered_sprite, held_sprite):
        """Performs specified action"""
        self.hovered_sprite = hovered_sprite
        self.held_sprite = held_sprite

        event = self.events[event_type]
        event()
        execute_logic()
        # Execute turn should be an entirely seperate function

    def click(self, sprite):
        """Pass click command to the sprite being hovered."""
        self.hovered_sprite.click()

    def release(self, sprite):
        """Pass release command to the sprite being held."""
        self.held_sprite.release()


    def execute_logic(self):
        self.assign_spirit()
        self.execute_player_turn()


    def assign_sprit(self):
        """Assigns a spirit to a unit."""
        if self.hovered_sprite and self.released_sprite:
            if (self.hovered_sprite in self.units and
                self.released_sprite in self.spirits):
                self.hovered_sprite.set_spirit(self.released_sprite)
    # This needs refactored.  Ideally use type instead of spritegroup also.

    def execute_player_turn(self):
        for unit in self.units:
            self.spirit_action.follow_spirit(unit)
