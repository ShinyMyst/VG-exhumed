######################
# Object
######################
"""
Base class template for all sprite style objects used on screen.
"""
import pygame as pg


class _StaticObject(pg.sprite.Sprite):
    """Template for sprite with no functionality."""
    def __init__(self, image: pg.Surface, size: tuple[int, int]):
        super().__init__()
        self.image = pg.transform.scale(image, size)
        self.mask = pg.mask.from_surface(self.image.convert_alpha())

        self.rect = self.image.get_rect()
        self.size_x, self.size_y = size

    #####################################
    # Getters/Setters
    #####################################
    def set_pos(self, pos):
        self.rect.x, self.rect.y = pos

    def get_coords(self):
        return self.rect

    def get_size(self):
        return self.size_x, self.size_y


    def update(self, mouse_pos:pg.mouse):
        """Overwritten in children classes to perform actions."""
        pass

class Button(_StaticObject):
    """Clickable object."""
    def __init__(self, image: pg.Surface, size: tuple[int, int]):
        super().__init__(image, size)
        self.mask = pg.mask.from_surface(self.image.convert_alpha())

        self.image_base = pg.transform.scale(image, size)
        self.image_active = pg.transform.scale(image, size)
        self.image_active.fill((225, 250, 255, 100), special_flags = pg.BLEND_MULT)


        self.function = None

        self._is_hovered = False

    #####################################
    # Getters/Setters
    #####################################

    def set_function(self, function):
        self.function = function


    def check_collision(self, mouse_pos):
        """Updates variable determining if sprite is being hovered over."""
        if self.rect.collidepoint(mouse_pos):
            pos_in_mask = mouse_pos[0] - self.rect.x, mouse_pos[1] - self.rect.y
            self._is_hovered = True if self.mask.get_at(pos_in_mask) else False
        else:
            self._is_hovered = False

    def update_appearence(self):
        """Change how sprite looks based on its current status."""
        if self._is_hovered:
            self.displayed_image = self.image_active
        else:
            self.displayed_image = self.image_base


    def update(self, mouse_pos:pg.mouse):
        """Updates sprites appearance on screen."""
        self.check_collision(mouse_pos)
        print(self._is_hovered)
        self.update_appearence()

# Needs some refactoring
# self.image is a name used by pg and can't be changed
# Change update to set mouse pos ?