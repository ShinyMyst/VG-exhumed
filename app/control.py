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

    #####################
    # Functions
    #####################
    # Use multiple sprite lists based on which need to checked?
    def event_loop(self):
        mouse_pos = pg.mouse.get_pos()
        self.state_sprites.update(mouse_pos)
        released_sprite = None
        active_sprite = None
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit(); sys.exit()  # noqa
            if event.type == pg.MOUSEBUTTONDOWN:
                for sprite in self.state_sprites:
                    sprite.click()
            if event.type == pg.MOUSEBUTTONUP:
                for spirit in self.state_sprites:
                    if spirit.release():
                        released_sprite = spirit
            for sprite in self.unit_sprites:
                if sprite._is_hovered:
                    active_sprite = sprite
                    break
                else:
                    active_sprite = None
            if active_sprite:
                print("ACTIVE")
                self.current_state.sprite_active(active_sprite)
            if released_sprite:
                self.current_state.sprite_released(released_sprite)

        # Change states if next state is available
        next_state = self.current_state.next_state
        if self.current_state.next_state:
            self.set_state(next_state)
            self.current_state.next_state = None

# TODO:
# Put state dict elsewhere
# Ideally, the bit of code at line 38 can be restructured.
# A button should call state change directly if possible.
# Remove need for states.X for imports; instead use from states import
# Find a less janky way to pass graphics updates.
