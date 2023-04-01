######################
# Set-Up
######################
"""
Prepares the Pygame Application window and loads all required resources.
"""
import pygame as pg
import os
from setup.loaders import load_graphics
from setup.config import start_size, caption, resource_folder, graphics_folder

# Initialize Pygame
pg.init()
pg.display.set_caption(caption)
SCREEN = pg.display.set_mode(start_size)
CLOCK = pg.time.Clock()

# Resource Directories
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
gfx_path = os.path.join(parent_dir, resource_folder, graphics_folder)

# Create dict of all graphics in directory
GFX = dict()
for folder in os.listdir(gfx_path):
    directory = os.path.join(gfx_path, folder)
    GFX[folder] = load_graphics(directory)
