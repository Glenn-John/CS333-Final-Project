# Implementation of the CrazyEights class
from deck import Deck
from player import Player

class CrazyEights:
    def __init__(self):
        self.players = [Player(), Player()]
        self.deck = Deck()
        self.current_player = 0

    def deal_new_round(self):
        for player in self.players:
            player.discard_hand()
        self.deck.build()
        for i in range(5):
            for player in self.players:
                player.draw(self.deck)
        self.deck.discard_card(self.deck.deal_card())

    def change_player(self):
        self.current_player = (self.current_player + 1) % 2 

    def play(self):
        # while playing:
        #   deal a new round
        #   print player hand
        #   if no valid card, draw until there is
        #   get player input for card to play
        #   check if winner (empty hand)
        #   no win: go to next player
        playing = True
        while playing:
            self.deal_new_round()


            choice = input("Would you like to play again? (Y/n): ")
            playing = choice.lower() == 'y'