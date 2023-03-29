import pygame as pg
from objects import Button


class Spirit(Button):
    """Clickable object."""
    def __init__(self, image: pg.Surface, size: tuple[int, int]):
        super().__init__(image, size)
        self.anchor_x = None
        self.anchor_y = None
        self.moving = True

    def set_pos(self, pos):
        """Set the anchor position in addition to rect position."""
        self.rect.x, self.rect.y = pos
        self.anchor_x, self.anchor_y = pos

    def click(self):
        """Lock sprite into moving mode if clicked."""
        if self._is_hovered:
            self.moving = True
            self.image = self.image_active

    def _update_appearence(self, mouse_pos):
        """Change appearnce if mouse is over sprite."""
        if self._is_hovered:
            self.image = self.image_active
        elif self.moving:
            self.rect.x, self.rect.y = mouse_pos
        else:
            self.image = self.image_base

    def release(self):
        """Return object to its starting position when released."""
        self.moving = False
        self.rect.x = self.anchor_x
        self.rect.y = self.anchor_y

    def is_clicked(self):
        pass
        # Use a function like this to determine when sprite clicked
        # Instead of checking is hovered manually

    #####################
    # Control Functions
    #####################
    def update(self, mouse_pos: pg.mouse):
        """Checks if hovered and updates appearence."""
        self._check_collision(mouse_pos)
        self._update_appearence(mouse_pos)
