from data import GFX, SCREEN
from SpriteKit.object import Button
import pygame as pg




class _State:
    def __init__(self):
        self._bg = None
        self._sprite_group = None

    def get_event(self, event):
        pass

    def get_bg(self):
        return self._bg

    def get_sprite_group(self):
        return self._sprite_group

### Beyond this point is a seperate main menu state file in future ###

start_button = Button(GFX['buttons']['start'], (200, 100))
start_button.set_pos((50, 50))
start_button.set_function(None)
main_menu_group = [
    start_button
]



main_menu_sprites = pg.sprite.RenderUpdates()
main_menu_sprites.add(start_button)

class MainMenu(_State):
    def __init__(self):
        self._bg = GFX['backgrounds']['back_cave']
        self._sprite_group = main_menu_sprites



STATES = {
    "start": MainMenu()
}