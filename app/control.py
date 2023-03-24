import pygame as pg
import sys
from states.start import Start

# Store this somewhere else
STATES = {
    "start": Start()
}


class Control():
    def __init__(self):
        self.state_dict = STATES
        self.current_state = None
        self.state_sprites = None

    #####################
    # Functions
    #####################
    def set_state(self, state: str):
        print("SET STATE")
        self.current_state = self.state_dict[state]
        self.state_sprites = self.current_state.get_sprite_group()

    def get_gfx(self):
        """Returns the background and sprite group for current state"""
        background = self.current_state.get_bg()
        sprites = self.current_state.get_sprite_group()
        return background, sprites

    #####################
    # Functions
    #####################
    def event_loop(self):
        mouse_pos = pg.mouse.get_pos()
        self.state_sprites.update(mouse_pos)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit(); sys.exit()  # noqa
            if event.type == pg.MOUSEBUTTONDOWN:
                for sprite in self.state_sprites:
                    sprite.click()

        # Change states if next state is available
        next_state = self.current_state.next_state
        if self.current_state.next_state:
            self.set_state(next_state)
            self.current_state.next_state = None

# TODO:
# Put state dict elsewhere
# Ideally, the bit of code at line 38 can be restructured.
# A button should call state change directly if possible.
