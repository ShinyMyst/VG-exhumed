######################
# Tests
######################
"""
Verifies everything is working
"""

# Standard Library Imports
import os
import unittest
# Third-pary Imports
import pygame as pg
# Local Imports
from app.setup.loaders import load_graphics


class TestLoaders(unittest.TestCase):
    def setUp(self):
        # Create Dummy Environment
        os.environ["SDL_VIDEODRIVER"] = "dummy"
        pg.init()
        pg.display.set_mode((1, 1))  # pg display w/o a display

        # Common GFX Directories
        current_dir = os.path.dirname(os.path.realpath(__file__))
        gfx_path = os.path.join(current_dir, "resources", "GFX")

        # Backgrounds
        self.background_dir = os.path.join(gfx_path, "backgrounds")
        self.background_list = os.listdir(self.background_dir)
        self.background_dict = load_graphics(self.background_dir)

        # Buttons
        self.button_dir = os.path.join(gfx_path, "buttons")
        self.button_list = os.listdir(self.background_dir)
        self.button_dict = load_graphics(self.background_dir)

        # Units
        self.unit_dir = os.path.join(gfx_path, "units")
        self.unit_list = os.listdir(self.background_dir)
        self.unit_dict = load_graphics(self.background_dir)

    def tearDown(self):
        pg.quit()

    def test_bg_dict_length(self):
        """Background dctionary length == length of background directory."""
        self.assertEqual(len(self.background_list), len(self.background_dict))

    def test_bg_file_type(self):
        """Background files correctly formatted"""
        for image in self.background_dict.values():
            self.assertIsInstance(image, pg.Surface)

    def test_button_dict_length(self):
        """Button dctionary length == length of button directory."""
        self.assertEqual(len(self.button_list), len(self.button_dict))

    def test_button_file_type(self):
        """Button files correctly formatted"""
        for image in self.button_dict.values():
            self.assertIsInstance(image, pg.Surface)

    def test_unit_dict_length(self):
        """Unit dctionary length == length of unit directory."""
        self.assertEqual(len(self.unit_list), len(self.unit_dict))

    def test_unit_file_type(self):
        """Unit files correctly formatted"""
        for image in self.unit_dict.values():
            self.assertIsInstance(image, pg.Surface)


if __name__ == '__main__':
    unittest.main()
