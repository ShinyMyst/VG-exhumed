from data import GFX, SCREEN
from States.states import _State
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

class StartMenu(_State):
    def __init__(self):
        super().__init__()
        self._bg = GFX['backgrounds']['back_cave']
        self._sprite_group = main_menu_sprites
        start_button.set_function(self.test_function)

    def test_function(self):
        self.set_target_state("start")
