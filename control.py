######################
# Controller
######################
"""
...
"""
from states import STATES
import pygame as pg
import sys

class Control():
    def __init__(self):
        self.state_dict = STATES
        self.current_state = None
        self.state_sprites = None


    def set_state(self, state:str):
        print("SET STATE")
        self.current_state = self.state_dict[state]
        self.state_sprites = self.current_state.get_sprite_group()

    def event_loop(self):
        mouse_pos = pg.mouse.get_pos()
        self.state_sprites.update(mouse_pos)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit(); sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                for sprite in self.state_sprites:
                    sprite.click()
        # Change state if applicable
        if self.current_state.get_target_state():
            self.set_state(self.current_state.get_target_state())
            self.current_state.set_target_state(None)

    def get_gfx(self):
        """Returns the background and sprite group for current state"""
        background = self.current_state.get_bg()
        sprites = self.current_state.get_sprite_group()
        return background, sprites


control = Control()