import unittest
from settings import settings
from settings_maneger import settings_maneger


class test_settings(unittest.TestCase):
    
    def test_check_first_name(self):
        item = settings()
        
        item.first_name = "  Yaroslav  "
        
        assert item.first_name == "Yaroslav"

    def test_check_open_settings(self):
        maneger = settings_maneger()
        
        result=maneger.open("settings.json")

        assert result==True

    def test_check_create_maneger(self):
        maneger1 = settings_maneger()
        maneger2 = settings_maneger()
        
        print(maneger1.unique_number)
        print(maneger2.unique_number)
        assert maneger1.unique_number==maneger2.unique_number


    def test_check_meneger_convert(self):
        maneger=settings_maneger()
        result=maneger.open("settings.json")
        maneger.convert()
