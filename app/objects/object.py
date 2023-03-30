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
        return self.rect.x, self.rect.y

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

    def release(self):
        """Overwritten in children classes to perform action when released."""
        pass

# TODO
# Needs some refactoring
# self.image is a name used by pg and can't be changed
# Change update to set mouse pos ?  (Why?)
# Some of button's functions need shared with other objects
