######################
# Set-Up
######################
"""
Prepares the Pygame Application window and loads all required resources.
"""
import pygame as pg
import os
from setup.loaders import load_graphics

# Default Settings
SIZE = 960, 540
caption = "Exhumed"

# Initialize Pygame
pg.init()
pg.display.set_caption(caption)
SCREEN = pg.display.set_mode(SIZE)
CLOCK = pg.time.Clock()


# Resource Directories
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
gfx_path = os.path.join(parent_dir, "resources", "GFX")

background_dir = os.path.join(gfx_path, "backgrounds")
button_dir = os.path.join(gfx_path, "buttons")
unit_dir = os.path.join(gfx_path, "units")
tile_dir = os.path.join(gfx_path, "tiles")

# Create Resource Dictionaries
GFX = {
    "backgrounds": load_graphics(background_dir),
    "buttons": load_graphics(button_dir),
    "units": load_graphics(unit_dir),
    "tiles": load_graphics(tile_dir)
}

# Window sizes 640×360, 960×540, and 1920×1080. 1280×720
