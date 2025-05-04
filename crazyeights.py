# Implementation of the CrazyEights class
from card import Card
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

    def get_current_player(self):
        return self.players[self.current_player]
    
    def is_card_valid(self, card: Card):
        top_card = self.deck.peek_discard()
        if card.value == 8:
            return True
        if card.suit == top_card.suit:
            return True
        if card.value == top_card.value:
            return True
        return False
    
    def has_valid_play(self):
        for card in self.get_current_player().hand:
            if self.is_card_valid(card):
                return True
        return False

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
            round = True
            while round:
                player = self.get_current_player()
                while not self.has_valid_play():
                    print("No valid cards. Drawing Card")
                    player.draw(self.deck)
                print("Your Hand:\n" + player.list_hand())
                num_cards = len(player.hand)




            choice = input("Would you like to play again? (Y/n): ")
            playing = choice.lower() == 'y'