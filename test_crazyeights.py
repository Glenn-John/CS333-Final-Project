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
    def setUp(self):
        self.mydeck = Deck()
        self.valid_values = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
        self.valid_suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']

    def test_constructor(self):
        self.assertEqual(len(self.mydeck.stock), 52)
        self.assertEqual(len(self.mydeck.discard), 0)

    def test_build(self):
        self.mydeck.build()
        self.assertEqual(len(self.mydeck.stock), 52)

    def test_draw_from_full_deck(self):
        drawn_card = self.mydeck.deal_card()
        self.assertEqual(len(self.mydeck.stock), 51)
        self.assertIn(drawn_card.value, self.valid_values)
        self.assertIn(drawn_card.suit, self.valid_suits)

    def test_discard_card(self):
        drawn_card = self.mydeck.deal_card()
        self.mydeck.discard_card(drawn_card)
        self.assertEqual(self.mydeck.discard[0].value, drawn_card.value)
        self.assertEqual(self.mydeck.discard[0].suit, drawn_card.suit)

    def test_peek_discard(self):
        self.mydeck.discard_card(self.mydeck.deal_card())
        second_card = self.mydeck.deal_card()
        self.mydeck.discard_card(second_card)
        peek_card = self.mydeck.peek_discard()
        self.assertEqual(second_card.value, peek_card.value)
        self.assertEqual(second_card.suit, peek_card.suit)

    def test_reshuffle(self):
        for _ in range(52):
            self.mydeck.discard_card(self.mydeck.deal_card())
        top_card = self.mydeck.peek_discard()
        self.mydeck.reshuffle()
        self.assertEqual(top_card, self.mydeck.peek_discard())

    def test_draw_from_one_card_deck(self):
        self.mydeck.stock.clear()
        self.mydeck.stock.append(Card(7, "Clubs"))
        drawn_card = self.mydeck.deal_card()
        self.assertEqual(len(self.mydeck.stock), 0)
        self.assertIn(drawn_card.value, self.valid_values)
        self.assertIn(drawn_card.suit, self.valid_suits)

    def test_draw_from_empty_stock(self):
        for _ in range(52):
            self.mydeck.discard_card(self.mydeck.deal_card())
        drawn_card = self.mydeck.deal_card()
        self.assertEqual(len(self.mydeck.stock), 50) # full 52 minus drawn card and the card left in the discard pile
        self.assertEqual(len(self.mydeck.discard), 1)
        self.assertIn(drawn_card.value, self.valid_values)
        self.assertIn(drawn_card.suit, self.valid_suits)

    def test_draw_from_empty_deck(self):
        self.mydeck.discard_card(self.mydeck.deal_card())
        self.mydeck.stock.clear()
        drawn_card = self.mydeck.deal_card()
        self.assertEqual(len(self.mydeck.stock), 0)
        self.assertEqual(len(self.mydeck.discard), 1)
        self.assertIsNone(drawn_card)

    def test_str(self):
        self.mydeck.discard_card(self.mydeck.deal_card())
        self.assertEqual(str(self.mydeck), 'Deck containing 51 cards in the stock and 1 cards in the discard pile')

class Test_Player(unittest.TestCase):
    def setUp(self):
        self.myplayer = Player()
        self.mydeck = Deck()

    def test_constructor(self):
        self.assertEqual(self.myplayer.hand, [])
        self.assertEqual(self.myplayer.points, 0)
    
    def test_draw(self):
        self.myplayer.draw(self.mydeck)
        card = self.myplayer.hand[0]
        self.assertEqual(len(self.mydeck.cards), 51)
        self.assertEqual(len(self.myplayer.hand), 1)
        self.assertNotIn(card, self.mydeck.cards)

    def test_discard_hand(self):
        self.myplayer.draw(self.mydeck)
        self.myplayer.discard_hand()
        self.assertEqual(len(self.myplayer.hand), 0)

    def test_get_hand_value(self):
        self.myplayer.hand = [Card("Ace", "Diamonds"), Card(5, "Hearts"), Card(8, "Spades"), Card("Jack", "Clubs"), Card("Queen", "Clubs"), Card("King", "Clubs")]
        self.assertEqual(self.myplayer.get_hand_value(), 86)

    def test_sort_hand(self):
        self.myplayer.hand = [Card(7, "Spades"), Card("Ace", "Diamonds"), Card("King", "Clubs"), Card("Jack", "Hearts")]
        self.myplayer.sort_hand()
        self.assertEqual(self.myplayer.hand[0].suit, "Clubs")
        self.assertEqual(self.myplayer.hand[1].suit, "Diamonds")
        self.assertEqual(self.myplayer.hand[2].suit, "Hearts")
        self.assertEqual(self.myplayer.hand[3].suit, "Spades")

    def test_list_hand(self):
        self.myplayer.hand = [Card(7, "Spades"), Card("Ace", "Diamonds")]
        mystr = "1. Ace of Diamonds\n2. 7 of Spades\n"
        self.assertEqual(self.myplayer.list_hand(), mystr)

    def test_str(self):
        self.myplayer.points = 42
        mystr = 'Player with 42 points'
        self.assertEqual(str(self.myplayer), mystr)

class Test_CrazyEights(unittest.TestCase):
    pass