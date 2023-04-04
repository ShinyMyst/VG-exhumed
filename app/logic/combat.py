from logic._spirits import _SpiritActions
from logic._logic import _Logic


class CombatLogic(_Logic):
    def __init__(self, grid):
        super().__init__()
        self.spirit_action = _SpiritActions(grid)  # Find dif way to pass grid

    #####################
    # Subclass Logic
    #####################
    def execute_logic(self):
        self.assign_spirit()

    def assign_spirit(self):
        """Assigns a spirit to a unit."""
        if self.hovered_sprite and self.held_sprite:
            if (self.hovered_sprite in self.units and
                    self.held_sprite in self.spirits):
                self.hovered_sprite.set_spirit(self.held_sprite)
    # This needs refactored.  Ideally use type instead of spritegroup also.

    #####################
    # Turn Logic
    #####################
    def execute_player_turn(self):
        for unit in self.units:
            self.spirit_action.follow_spirit(unit)

    def process_turn(self):
        self.execute_player_turn()
