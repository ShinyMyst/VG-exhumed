import os
import pygame

current_dir = os.path.dirname(os.path.realpath(__file__))


def load_gfx(gfx_dir: str, folder: str):
    """Targets all files in the gfx_dir in given folder.
    Saves the files in folder to a dict with file name as key."""
    gfx_dictionary = dict()
    gfx_path = gfx_dir + "/" + folder
    target_folder = os.path.join(current_dir, gfx_path)
    for file in os.listdir(target_folder):
        
        gfx_dictionary[file.split(".")[0]] = file
        
    return gfx_dictionary

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