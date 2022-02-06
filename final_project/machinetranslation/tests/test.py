import unittest
from translator import english_to_french,french_to_english
class TestenglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertEqual(english_to_french('Goodbye'),'Au revoir')
        self.assertNotEqual(english_to_french('Welcome'),'Au revoir')
        self.assertEqual(english_to_french('Welcome'),'Bienvenue')
class TestfrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertEqual(french_to_english('Au revoir'),'Goodbye')
        self.assertNotEqual(french_to_english('Au revoir'),'Welcome')
        self.assertEqual(french_to_english('Bienvenue'),'Welcome')

unittest.main()