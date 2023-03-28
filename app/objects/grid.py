import pygame as pg
from objects import Button


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
            row = self.create_row(position.copy())
            self.grid.append(row)
            position[1] += self.tile_size[1] + self.offset

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

    def get_square(self, coords: tuple):
        """Returns square object based on its grid coords."""
        column, row = coords
        return self.grid[row][column]


class GridSquare(Button):
    def __init__(self, image: pg.Surface, size: tuple):
        super().__init__(image, size)
