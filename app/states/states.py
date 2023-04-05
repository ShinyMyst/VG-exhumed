import pygame as pg
from data import GFX
from objects import Button, Grid, Spirit, Unit


class _State:
    def __init__(self):
        self._bg = None
        self.target_state = None
        self.grid = None
        self.function_dict = dict()

        # Sprite Groups
        self.buttons = pg.sprite.Group()
        self.spirits = pg.sprite.Group()
        self.units = pg.sprite.Group()
        self.all_sprites = pg.sprite.RenderUpdates()

        # Initialization
        # (can't use in template until logic and sprites are parameters)
        # self.initialize_objects
        # self.initialize_logic

    #####################
    # Getters/Setters
    #####################
    def get_bg(self):
        return self._bg

    def get_sprites(self):
        return self.all_sprites

    #####################
    # Initialization
    #####################
    def initialize_objects(self, sprite_input: list, grid_input=None):
        """Resets objects associated with state then sets them to the inputs.
        Used when same state may have different appearences.
        For example: each battle scene needs different inputs."""
        self.buttons = pg.sprite.Group()
        self.spirits = pg.sprite.Group()
        self.units = pg.sprite.Group()
        self.all_sprites = pg.sprite.RenderUpdates()

        if grid_input:
            self._add_grid(**grid_input)
        for sprite in sprite_input:
            if sprite['type'] == 'buttons':
                self._add_button(**sprite)
            if sprite['type'] == 'spirits':
                self._add_spirit(**sprite)
            if sprite['type'] == 'units':
                self._add_unit_grid(**sprite)

    def initialize_logic(self, logic):
        """Call after objects initialized to pass to logic."""
        self.logic = logic
        self.logic.sync_sprites(self.buttons, self.spirits, self.units,
                                self.all_sprites, self.grid)

    #####################
    # Add Sprites/Grids
    #####################
    def _add_grid(self, tile_set, tile_size, grid_dimensions, position):
        self.grid = Grid(tile_set, tile_size)
        self.grid.generate_grid(grid_dimensions, position)
        grid_squares = self.grid.get_squares()
        for square in grid_squares:
            self.all_sprites.add(square)

    def _add_button(self, type, img_name, size, position, function_name):
        button = Button(GFX[type][img_name], size)
        button.set_pos((position))
        button.set_function(self.function_dict[function_name])
        self.buttons.add(button)
        self.all_sprites.add(button)

    def _add_spirit(self, type, img_name, size, position, effect: list):
        spirit = Spirit(GFX[type][img_name], size)
        spirit.set_pos((position))
        spirit.set_effect(effect)
        self.spirits.add(spirit)
        self.all_sprites.add(spirit)

    def _add_unit_grid(self, type, img_name, size, position):
        unit = Unit(GFX[type][img_name], size)
        self.grid.set_sprite(unit, position)
        self.units.add(unit)
        self.all_sprites.add(unit)

    #####################
    # Event Processing
    #####################
    def update(self, event):
        """Updates variables and calls necessary logic when event received"""
        # Find which sprites are moving, which are hovered, and process event.
        # Take position from control and do update here instead of in control.
        held_sprite = None
        hovered_sprite = None
        for sprite in self.all_sprites:
            if sprite.is_held:
                held_sprite = sprite
            if sprite.is_hovered:
                hovered_sprite = sprite

        self.logic.update(event, hovered_sprite, held_sprite)
