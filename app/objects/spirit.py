import pygame as pg
from objects import Button


class Spirit(Button):
    """Clickable object."""
    def __init__(self, image: pg.Surface, size: tuple[int, int]):
        super().__init__(image, size)
        self.anchor_x = None
        self.anchor_y = None
        self.effect = None  # List of string commands.
        # Refactor how effects saved/stored.

    def set_pos(self, pos):
        """Set the anchor position in addition to rect position."""
        self.rect.x, self.rect.y = pos
        self.anchor_x, self.anchor_y = pos

    def click(self):
        """Lock sprite into moving mode if clicked."""
        if self.is_hovered:
            self.is_held = True
            self.image = self.image_active

    def _update_appearence(self, mouse_pos):
        """Change appearnce if mouse is over sprite."""
        if self.is_held:
            self.rect.x, self.rect.y = mouse_pos
        if self.is_hovered:
            self.image = self.image_active
        else:
            self.image = self.image_base

    def release(self):
        """Return object to its starting position when released."""
        if self.is_held is True:
            self.is_held = False
            self.rect.x = self.anchor_x
            self.rect.y = self.anchor_y
            return True
        return False

    def is_clicked(self):
        pass
        # Use a function like this to determine when sprite clicked
        # Instead of checking is hovered manually

    def set_effect(self, effect):
        self.effect = effect

    def get_effect(self):
        return self.effect

    #####################
    # Control Functions
    #####################
    def update(self, mouse_pos: pg.mouse):
        """Checks if hovered and updates appearence."""
        self._check_collision(mouse_pos)
        self._update_appearence(mouse_pos)
