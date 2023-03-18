######################
# Set-Up
######################
"""
Prepares the Pygame Application window and loads all required resources.
"""
import pygame as pg
import os
from loaders import load_graphics

# Default Settings
SIZE = 1000, 500
caption = "Exhumed"

# Initialize Pygame
pg.init()
pg.display.set_caption(caption)
SCREEN = pg.display.set_mode(SIZE)
clock = pg.time.Clock()


# Resource Directories
current_dir = os.path.dirname(os.path.realpath(__file__))
gfx_path = os.path.join(current_dir, "resources", "GFX")

background_dir = os.path.join(gfx_path, "backgrounds")
button_dir = os.path.join(gfx_path, "buttons")
unit_dir = os.path.join(gfx_path, "units")

# Create Resource Dictionaries
GFX = {
    "backgrounds": load_graphics(background_dir),
    "buttons": load_graphics(button_dir),
    "units": load_graphics(unit_dir)
}
