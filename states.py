
class _State:
    def __init__(self):
        self._bg = None
        self._sprite_group = None
        self._target_state = None

    def get_event(self, event):
        pass

    def get_bg(self):
        return self._bg

    def get_sprite_group(self):
        return self._sprite_group

    def set_target_state(self, state:str):
        self._target_state = state

    def get_target_state(self):
        return self._target_state

from data import GFX, SCREEN
from SpriteKit.object import Button
import pygame as pg


### Beyond this point is a seperate main menu state file in future ###
def test_function(self):
    #print("Hello world!")
    self.set_state("start")



start_button = Button(GFX['buttons']['start'], (200, 100))
start_button.set_pos((50, 50))

main_menu_group = [
    start_button
]



main_menu_sprites = pg.sprite.RenderUpdates()
main_menu_sprites.add(start_button)

class MainMenu(_State):
    def __init__(self):
        super().__init__()
        self._bg = GFX['backgrounds']['back_cave']
        self._sprite_group = main_menu_sprites
        start_button.set_function(self.test_function)

    def test_function(self):
        self.set_target_state("start")



STATES = {
    "start": MainMenu()
}


# Set up states to only initiate when used and to clear otherwise.