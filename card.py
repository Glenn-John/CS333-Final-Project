# Implementation of the Card class
class Card:
    def __init__(self, v, s):
        self.value = v
        self.suit = s

    def __str__(self):
        return f'{self.value} of {self.suit}'
    
    def __eq__(self, other):
        return (self.value == other.value) and (self.suit == other.suit)