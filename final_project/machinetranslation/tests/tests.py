import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        english_greeting = "Hello"
        translated_french_greeting = english_to_french(english_greeting)
        self.assertEqual(translated_french_greeting, "Bonjour")

    def test2(self):
        english_ending = "Bye"
        translated_french_ending = english_to_french(english_ending)
        self.assertNotEqual(translated_french_ending, "Bonjour")


class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        french_greeting = "Bonjour"
        translated_english_greeting = french_to_english(french_greeting)
        self.assertEqual(translated_english_greeting, "Hello")

    def test2(self):
        french_ending = "Au revoir"
        translated_english_ending = french_to_english(french_ending)
        self.assertNotEqual(translated_english_ending, "Hello")


unittest.main()