# Must be initialized within a logic class.
# Used to translate spirit effects into actions.

class SpiritActions():
    def __init__(self, grid):
        self.grid = grid
        self.actions = {
            "forward": self._foward
        }

    #####################
    # Actions
    #####################
    def _forward(self, unit):
        self.grid.move_sprite(unit, [1, 0])

    #####################
    # Shared Functions
    #####################
    def get_action(self, action_str):
        return self.actions[action_str]

    def execute(self, action_str, unit):
        """Given a specific unit and action,
        executes action from that unit on the grid."""
        self.actions[action_str](unit)
