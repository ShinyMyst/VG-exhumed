import pygame as pg
from objects import Button


class Unit(Button):
    """Clickable object."""
    def __init__(self, image: pg.Surface, size: tuple[int, int]):
        super().__init__(image, size)
        self.square = None

    def get_square(self):
        return self.square

    def set_square(self, square):
        self.square = square

    def set_pos(self, pos):
        self.rect.x, self.rect.y = pos
        print(pos)
