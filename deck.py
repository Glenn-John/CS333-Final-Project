# Implementation of the Deck class
import random
from card import Card

class Deck:
    def __init__(self):
        self.stock: list[Card] = []
        self.discard: list[Card] = []
        self.top_suit: str = ""
        self.build()

    def build(self):
        self.stock.clear()
        self.discard.clear()
        for s in ['Spades', 'Clubs', 'Diamonds', 'Hearts']:
            self.stock.append(Card('Ace', s))
            for v in range(2, 11):
                self.stock.append(Card(v, s))
            self.stock.append(Card('Jack', s))
            self.stock.append(Card('Queen', s))
            self.stock.append(Card('King', s))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.stock)

    def reshuffle(self):
        top_card = self.discard.pop()
        self.stock.extend(self.discard)
        self.discard.clear()
        self.discard.append(top_card)
        random.shuffle(self.stock)

    def deal_card(self) -> Card:
        if len(self.stock) == 0:
            self.reshuffle()
        if len(self.stock) == 0:
            return None
        return self.stock.pop()

    def discard_card(self, card: Card):
        self.discard.append(card)
        self.top_suit = card.suit

    def peek_discard(self) -> Card:
        if len(self.discard) == 0:
            return None
        return Card(self.discard[-1].value, self.top_suit)
    
    def set_top_suit(self, suit: str):
        valid_suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        if suit in valid_suits:
            self.top_suit = suit
    
    def __str__(self):
        return f'Deck containing {len(self.stock)} cards in the stock and {len(self.discard)} cards in the discard pile'
            