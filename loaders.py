######################
# Loaders
#
######################

import os
# import pygame


def load_graphics(directory):
    """Creates a dictionary of all image files in given directory.
    Key == file name - extension.  File == formatted pygame img."""
    gfx_dict = dict()
    for file in os.listdir(directory):
        print(file)
        gfx_dict[file.split(".")[0]] = file

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
# Add a unit test to ensure files can be loaded properly.