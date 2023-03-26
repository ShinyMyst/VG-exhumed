import pygame as pg
from data import GFX
from states.states import _State
from objects import Button

# Sprite Group
sprites = pg.sprite.RenderUpdates()


class Grid():
    def __init__(self, tile_set, tile_size):
        self.grid = []
        self.tile_set = tile_set
        self.tile_size = tile_size
        self.offset = 10            # Distance between tiles

    def generate_grid(self, grid_size: tuple, top_left_pos: list):
        self.max_width = grid_size[0]
        self.max_height = grid_size[1]
        position = top_left_pos

        # Add a row at a time to the grid until max height reached.
        for row in range(self.max_height):
            print("ROW", position)
            row = self.create_row(position.copy())
            self.grid.append(row)
            print("MID ROW", position)
            position[1] += self.tile_size[1] + self.offset
            print("END ROW", position)

    def create_square(self, image, position):
        """Creates and positions a GridSquare object."""
        square = GridSquare(image, self.tile_size)
        square.set_pos(position)
        return square

    def create_row(self, start_position: list):
        """Returns are list of GridSquare objects positioned horizontally."""
        row = []
        image = self.tile_set[0]  # <------ Currently using single tile.
        position = start_position

        for square in range(self.max_width):
            square = self.create_square(image, position)
            row.append(square)
            position[0] += self.tile_size[0] + self.offset

        return row

    def get_sprites(self):
        """Returns a list of all sprites used to create the grid.
            Does not include sprites positioned on the grid."""
        all_sprites = []
        for row in self.grid:
            for square in row:
                all_sprites.append(square)
        return all_sprites


class GridSquare(Button):
    def __init__(self, image: pg.Surface, size: tuple):
        super().__init__(image, size)


###############
# Create Sprites
##############
start_button = Button(GFX['buttons']['start'], (200, 100))
start_button.set_pos((0, 0))
sprites.add(start_button)


tiles = [GFX['tiles']['tile']]
grid = Grid(tiles, (50, 50))
grid.generate_grid((4, 3), [50, 50])
grid_sprites = grid.get_sprites()
print("THIS IS RUNNING BEFORE USED")
for sprite in grid_sprites:
    sprites.add(sprite)


class Battle(_State):
    def __init__(self):
        super().__init__()
        self._bg = GFX['backgrounds']['floor']
        self._sprite_group = sprites
        start_button.set_function(self.test_function)

    def test_function(self):
        self.next_state = "start"

# Grids can be their own library
# Sprite creation needs encapsulated so it doesn't run at start
# Can also probably better design grid making functions
