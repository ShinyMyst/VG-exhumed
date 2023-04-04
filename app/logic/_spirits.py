# Must be initialized within a logic class.
# Must have a grid to reference.
# Used to translate spirit effects into actions.

class _SpiritActions():
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

    def execute_effect(self, unit, effect):
        """Given a specific unit and effect,
        executes action from that unit on the grid."""
        if effect:  # None is a possible action
            self.actions[effect](unit)

    def follow_spirit(self, unit):
        """Gives unit commands based on its assigned spirit."""
        spirit = unit.get_spirit()
        effects = spirit.get_effects()
        for effect in effects:
            self.execute_effect(unit, effect)
