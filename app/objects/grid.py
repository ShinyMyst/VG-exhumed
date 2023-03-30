import pygame as pg
from objects import Button


class GridSquare(Button):
    def __init__(self, image: pg.Surface, size: tuple, grid_coords: tuple):
        super().__init__(image, size)
        self.contains = None
        self.grid_coords = grid_coords

    def set_contains(self, object):
        """Determines what is in the square."""
        self.contains = object

    def get_grid_coords(self):
        return self.grid_coords


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
        row_num = 0

        # Add a row at a time to the grid until max height reached.
        for row in range(self.max_height):
            row = self.create_row(position.copy(), row_num)
            self.grid.append(row)
            position[1] += self.tile_size[1] + self.offset
            row_num += 1

    def create_square(self, image, position, grid_coords):
        """Creates and positions a GridSquare object."""
        square = GridSquare(image, self.tile_size, grid_coords)
        square.set_pos(position)
        return square

    def create_row(self, start_position: list, grid_y: int):
        """Returns are list of GridSquare objects positioned horizontally."""
        row = []
        image = self.tile_set[0]  # <------ Currently using single tile.
        position = start_position
        grid_x = 0

        for square in range(self.max_width):
            square = self.create_square(image, position, (grid_x, grid_y))
            row.append(square)
            position[0] += self.tile_size[0] + self.offset
            grid_x += 1

        return row

    def get_sprites(self):
        """Returns a list of all sprites used to create the grid.
            Does not include sprites positioned on the grid."""
        all_sprites = []
        for row in self.grid:
            for square in row:
                all_sprites.append(square)
        return all_sprites

    def get_square(self, grid_coords: tuple) -> GridSquare:
        """Returns square object based on its grid coords."""
        column, row = grid_coords
        return self.grid[row][column]

    def set_sprite(self, sprite, grid_coords: tuple):
        """Finds grid square based on its grid coords.
        Positions sprite and associates it with the square."""
        square = self.get_square(grid_coords)
        square.set_contains(sprite)
        screen_coords = square.get_coords()  # <--- Using top left of square
        sprite.set_pos(screen_coords)
        sprite.set_square(square)

    def move_sprite(self, sprite, move_coords: tuple):
        # Empty original square & get its coords
        square = sprite.get_square()
        square.set_contains(None)
        grid_coords = square.get_grid_coords()

        # Use move values to find new location
        new_coords = (grid_coords[0] + move_coords[0],
                      grid_coords[1] + move_coords[1])
        self.set_sprite(sprite, new_coords)

# Use middle of square
# Validate that new coords are possible move
