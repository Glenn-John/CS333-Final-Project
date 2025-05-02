# Implementation of the Deck class
import random
from card import Card

class Deck:
    def __init__(self):
        self.stock: list[Card] = []
        self.discard: list[Card] = []

    def build(self):
        self.stock.clear()
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

    def peek_discard(self) -> Card:
        if len(self.discard) == 0:
            return None
        return self.discard[-1]
    
    def __str__(self):
        return f'Deck containing {len(self.stock)} cards in the stock and {len(self.discard)} cards in the discard pile'
            