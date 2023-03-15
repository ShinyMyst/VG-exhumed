######################
# Object
######################
"""
Base class template for all sprite style objects used on screen.
"""
import pygame as pg


class _Object(pg.sprite.Sprite):
    """Template for all sprites on screen."""
    def __init__(self, image: pg.Surface, size: tuple[int, int]):
        self.image = pg.transform.scale(image, size)
        self.mask = pg.mask.from_surface(self.image.convert_alpha())

        self.rect = self.image.get_rect()
        self.size_x, self.size_y = size
        self.rect.x, self.rect.y = None

    #####################################
    # Getters/Setters
    #####################################
    def set_pos(self, pos):
        self.rect[0], self.rect[1] = pos

    def get_coords(self):
        return self.rect

    def get_size(self):
        return self.size_x, self.size_y