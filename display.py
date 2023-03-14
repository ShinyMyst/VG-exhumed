################
# Display 
################
"""
Renders sprites and backgrounds to the screen.
"""
import pygame as pg

class Display():
    def __init__(self, screen):
        self.screen = screen
        self.background = None
        self.sprites = None

    def set_bg(self, background: pg.Surface):
        self.background = background
        self.screen.blit(self.background, (0,0))
        pg.display.flip()

    def set_gfx(self, sprite_group: pg.sprite.Group):
        self.sprites = sprite_group

    def set_display(self, background, sprites):
        """Updates the current background and spirte group for display."""
        self.set_bg(background)
        self.set_gfx(sprites)

    def render_screen(self):
        self.screen.blit(self.background, (0,0))
        self.sprites.draw(self.screen)
        pg.display.flip()
