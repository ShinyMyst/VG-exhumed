import pygame as pg


class _StaticObject(pg.sprite.Sprite):
    """Template for sprite with no functionality."""
    def __init__(self, image: pg.Surface, size: tuple[int, int]):
        super().__init__()
        self.image = pg.transform.scale(image, size)
        self.mask = pg.mask.from_surface(self.image.convert_alpha())

        self.rect = self.image.get_rect()
        self.size_x, self.size_y = size

    #####################
    # Getters/Setters
    #####################
    def set_pos(self, pos):
        self.rect.x, self.rect.y = pos

    def get_coords(self):
        return self.rect

    def get_size(self):
        return self.size_x, self.size_y

    #####################
    # Control Functions
    #####################
    def update(self, mouse_pos: pg.mouse):
        """Overwritten in children classes to track mouse position."""
        pass

    def click(self):
        """Overwritten in children classes to perform action when clicked."""
        pass


class Button(_StaticObject):
    """Clickable object."""
    def __init__(self, image: pg.Surface, size: tuple[int, int]):
        super().__init__(image, size)
        # Info
        self.active_color = (225, 250, 255, 100)
        self._is_hovered = False
        self.function = None

        # Apperances
        self.mask = pg.mask.from_surface(self.image.convert_alpha())
        self.image_base = pg.transform.scale(image, size)
        self.image_active = pg.transform.scale(image, size)
        self.image_active.fill(self.active_color, special_flags=pg.BLEND_MULT)

    #####################
    # Getters/Setters
    #####################
    def set_function(self, function):
        self.function = function

    def set_color(self, color: tuple):
        """Changes the default hover color."""
        self.active_color = color

    #####################
    # Button Functions
    #####################
    def _check_collision(self, mouse_pos):
        """Determines is mouse is over sprite."""
        if self.rect.collidepoint(mouse_pos):
            pos_in_mask = mouse_pos[0] - self.rect.x, mouse_pos[1] - self.rect.y # noqa
            self._is_hovered = True if self.mask.get_at(pos_in_mask) else False
        else:
            self._is_hovered = False

    def _update_appearence(self):
        """Change appearnce if mouse is over sprite."""
        if self._is_hovered:
            self.image = self.image_active
        else:
            self.image = self.image_base

    #####################
    # Control Functions
    #####################
    def update(self, mouse_pos: pg.mouse):
        """Checks if hovered and updates appearence."""
        self._check_collision(mouse_pos)
        self._update_appearence()

    def click(self):
        """Perform function when clicked."""
        if self._is_hovered and self.function:
            self.function()

# TODO
# Needs some refactoring
# self.image is a name used by pg and can't be changed
# Change update to set mouse pos ?  (Why?)
# Some of button's functions need shared with other objects
