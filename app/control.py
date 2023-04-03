import pygame as pg
import sys
from states import STATES
# Imports for Type Hinting
from states.states import _State


class Control():
    state: _State

    def __init__(self):
        self.state_dict = STATES
        self.state = None
        self.all_sprites = None

        self.update_gfx = False  # Tells Display when to update sprite list

    #####################
    # Functions
    #####################
    def swap_states(self):
        """If a new target state is available, swap the current state."""
        if self.state.target_state:
            next_state = self.state.target_state
            self.state.target_state = None
            self.set_state(next_state)
            self.update_gfx = True

    def event_loop(self):
        self.update_gfx = False
        mouse_pos = pg.mouse.get_pos()
        self.all_sprites.update(mouse_pos)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit(); sys.exit()  # noqa
            if event.type == pg.MOUSEBUTTONDOWN:
                self.state.get_event("click")
            if event.type == pg.MOUSEBUTTONUP:
                self.state.get_event("release")

            self.swap_states()

    #####################
    # Getters/Setters
    #####################
    def set_state(self, state_name: str):
        self.state = self.state_dict[state_name]
        self.all_sprites = self.state.get_sprites()

    def get_gfx(self):
        """Returns the background and all sprites for current state."""
        background = self.state.get_bg()
        sprites = self.state.get_sprites()
        return background, sprites
