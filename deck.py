# Implementation of the Deck class
import random
from card import Card

class Deck:
    def __init__(self):
        self.stock: list[Card] = []
        self.discard: list[Card] = []

    def build(self):
        pass

    def shuffle(self):
        pass

    def reshuffle(self):
        pass

    def deal_card(self) -> Card:
        pass

    def discard_card(self, card: Card):
        pass

    def peek_discard(self) -> Card:
        pass
    
    def __str__(self):
        pass
            