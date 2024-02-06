import unittest
from src.settings import *


class test_settings(unittest.TestCase):
    
    def test_check_first_name(self):
        item = Settings()
        
        item.first_name = "  Yaroslav  "
        
        assert item.first_name == "Yaroslav"

    def test_check_second_name(self):
        item = Settings()
        
        item.first_name = "Stepanov"
        
        assert item.first_name == "Stepanov"