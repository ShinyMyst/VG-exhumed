# Must be initialized within a logic class.
# Must have a grid to reference.
# Used to translate spirit effects into actions.

class _SpiritActions():
    def __init__(self, grid):
        self.grid = grid
        self.actions = {
            "forward": self._forward
        }

    #####################
    # Actions
    #####################
    def _forward(self, unit):
        self.grid.move_sprite(unit, [1, 0])

    #####################
    # Shared Functions
    #####################

    def execute_effect(self, unit, effect):
        """Given a specific unit and effect,
        executes action from that unit on the grid."""
        if effect:  # None is a possible action
            action = self.actions[effect]
            action(unit)

    def follow_spirit(self, unit):
        """Gives unit commands based on its assigned spirit."""
        spirit = unit.get_spirit()
        if spirit:
            effect = spirit.get_effect()
            for action in effect:
                self.execute_effect(unit, action)
