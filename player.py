# Implementation of the Player class
from card import Card
from deck import Deck

class Player:
    def __init__(self):
        self.hand: list[Card] = []
        self.points = 0

    def draw(self, deck: Deck):
        drawn_card = deck.deal_card()
        if drawn_card is not None:
            self.hand.append(drawn_card)
        return drawn_card

    def discard_hand(self):
        self.hand.clear()

    def get_hand_value(self) -> int:
        total = 0
        for card in self.hand:
            if card.value == 'Ace':
                total += 1
            elif card.value == 8:
                total += 50
            elif card.value in ['Jack', 'Queen', 'King']:
                total += 10
            else:
                total += card.value
        return total
    
    def sort_hand(self):
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        values = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
        self.hand.sort(key=lambda card: (suits.index(card.suit), values.index(card.value)))

    def list_hand(self) -> str:
        self.sort_hand()
        mystr = ''
        for i in range(len(self.hand)):
            mystr += f'{i+1}. {self.hand[i].value} of {self.hand[i].suit}\n'
        return mystr

    def __str__(self):
        return f'Player with {self.points} points'
