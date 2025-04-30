import unittest
from card import Card
from deck import Deck
from player import Player
from crazyeights import CrazyEights

class Test_Card(unittest.TestCase):
    def test_constructor_number(self):
        mycard = Card(7, "Spades")
        self.assertEqual(mycard.value, 7)
        self.assertEqual(mycard.suit, "Spades")

    def test_constructor_face(self):
        mycard = Card("King", "Diamonds")
        self.assertEqual(mycard.value, "King")
        self.assertEqual(mycard.suit, "Diamonds")

    def test_str(self):
        mycard = Card(7, "Spades")
        self.assertEqual(str(mycard), "7 of Spades")

class Test_Deck(unittest.TestCase):
    pass

class Test_Player(unittest.TestCase):
    pass

class Test_CrazyEights(unittest.TestCase):
    pass