import pygame as pg
from .object import _StaticObject


class Dragable(_StaticObject):
    """Draggable object"""
    def __init__(self, image: pg.Surface, size: tuple[int, int]):
        super().__init__(image, size)
