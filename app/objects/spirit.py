import pygame as pg
from objects.object import _FluidObject


class Spirit(_FluidObject):
    """Clickable object."""
    def __init__(self, image: pg.Surface, size: tuple[int, int]):
        super().__init__(image, size)
        self.anchor_x = None
        self.anchor_y = None
        self.effect = None  # List of string commands.
        # Refactor how effects saved/stored.

    #####################
    # Getters/Setters
    #####################
    def set_pos(self, pos):
        """Set the anchor position in addition to rect position."""
        self.rect.x, self.rect.y = pos
        self.anchor_x, self.anchor_y = pos

    def set_effect(self, effect):
        self.effect = effect

    def get_effect(self):
        return self.effect

    #####################
    # Visual Functions
    #####################
    def _update_appearence(self, mouse_pos):
        """Change appearnce if mouse is over sprite."""
        if self.is_held:
            self.rect.x, self.rect.y = mouse_pos
        elif self.is_hovered:
            self.image = self.image_active
        else:
            self.image = self.image_base

    #####################
    # Control Functions
    #####################
    def update(self, mouse_pos: pg.mouse):
        """Checks if hovered and updates appearence."""
        self._check_collision(mouse_pos)
        self._update_appearence(mouse_pos)

    def click(self):
        """Lock sprite into moving mode if clicked."""
        if self.is_hovered:
            self.is_held = True
            self.image = self.image_active

    def release(self):
        """Return object to its starting position when released."""
        if self.is_held:
            self.is_held = False
            self.rect.x = self.anchor_x
            self.rect.y = self.anchor_y
