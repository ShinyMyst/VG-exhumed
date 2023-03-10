######################
# Loaders
######################
"""
Creates and formats images and other assets used by pygame.
"""

import os
import pygame as pg


def load_graphics(directory):
    """Creates a dictionary of all image files in given directory.
    Key == file name - extension.  File == formatted pygame img."""
    gfx_dict = dict()
    for file in os.listdir(directory):
        file_name, ext = os.path.split(file)
        image = pg.image.load(os.path.join(directory, file))
        image = format_image(image)
        gfx_dict[file_name] = image

    return gfx_dict


def format_image(image):
    """Formats a given image to work within PyGame."""
    if image.get_alpha():
        image = image.convert_alpha()
    else:
        image = image.convert()
        image.set_colorkey()
    return image


# Add color to color key
# Encapsulate so Pygame does not need imported/initialized in this folder
# Verify image extension type
