import pygame as pg
import sys
from states import STATES


class Control():
    def __init__(self):
        self.state_dict = STATES
        self.current_state = None
        self.state_sprites = None
        self.units = None
        self.change = False

    #####################
    # Functions
    #####################
    def set_state(self, state: str):
        print("SET STATE")
        self.current_state = self.state_dict[state]
        self.state_sprites = self.current_state.get_sprite_group()
        self.unit_sprites = self.current_state.get_unit_group()
        self.change = True

    def get_gfx(self):
        """Returns the background and sprite group for current state"""
        background = self.current_state.get_bg()
        sprites = self.current_state.get_sprite_group()
        self.change = False
        return background, sprites

    def swap_states(self):
        if self.current_state.next_state:
            next_state = self.current_state.next_state
            self.current_state.next_state = None
            self.set_state(next_state)

    #####################
    # Functions
    #####################
    # Use multiple sprite lists based on which need to checked?
    def event_loop(self):
        mouse_pos = pg.mouse.get_pos()
        self.state_sprites.update(mouse_pos)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit(); sys.exit()  # noqa
            if event.type == pg.MOUSEBUTTONDOWN:
                self.current_state.click()

            if event.type == pg.MOUSEBUTTONUP:
                self.current_state.release()

            self.current_state.active()
            self.swap_states()

# TODO:
# Put state dict elsewhere
# Ideally, the bit of code at line 38 can be restructured.
# A button should call state change directly if possible.
# Remove need for states.X for imports; instead use from states import
# Find a less janky way to pass graphics updates.
