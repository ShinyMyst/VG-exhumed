import unittest
import pygame
import os
from loaders import load_graphics


class TestLoaders(unittest.TestCase):
    def setUp(self):
        pygame.init()
        current_dir = os.path.dirname(os.path.realpath(__file__))
        gfx_path = os.path.join(current_dir, "resources", "GFX")
        
        # Backgrounds
        self.background_dir = os.path.join(gfx_path, "backgrounds")
        self.background_list = os.listdir(self.background_dir)
        
        
    def tearDown(self):
        pygame.quit()
        
    def test_bg_length(self):
        """Background dctionary length == length of background directory."""
        background_dict = load_graphics(self.background_dir)
        self.assertEqual(len(self.background_list), len(background_dict)
                         
    def test_bg_file_type(self):
        """Background files correctly formatted"""
        return
        #for image in image_dict.values()
         #   self.assertIsInstance(image, pygame.Surface)
         
if __name__ == '__main__':
    unittest.main()