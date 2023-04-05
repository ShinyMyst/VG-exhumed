import pygame as pg
from .object import _FluidObject


class Button(_FluidObject):
    """Clickable object."""
    def __init__(self, image: pg.Surface, size: tuple[int, int]):
        super().__init__(image, size)

    #####################
    # Getters/Setters
    #####################
    def set_function(self, function):
        self.function = function

    #####################
    # Control Functions
    #####################
    def click(self):
        """Perform function when clicked."""
        if self.is_hovered and self.function:
            self.function()
