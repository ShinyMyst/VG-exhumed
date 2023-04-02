import pygame as pg
from data import SIZE


class Display():
    def __init__(self, screen):
        self.screen = screen
        self.background = None
        self.sprites = None

    #####################
    # Getters/Setters
    #####################
    def set_bg(self, background: pg.Surface):
        """Resizes and assigns background."""
        self.background = pg.transform.scale(background, SIZE)
        self.screen.blit(self.background, (0, 0))
        pg.display.flip()

    def set_gfx(self, sprite_group: pg.sprite.Group):
        self.sprites = sprite_group

    def set_display(self, background, sprites):
        """Sets the current background and spirte group."""
        self.set_bg(background)
        self.set_gfx(sprites)

    #####################
    # Functions
    #####################
    def render_screen(self):
        """Updates what is displayed on screen."""
        self.screen.blit(self.background, (0, 0))
        self.sprites.draw(self.screen)
        pg.display.flip()

# TODO:
# Should display do sizing?
# Sizing within states eliminates the need to import
# Alternatively, set size as a BG arg OR a set size func
