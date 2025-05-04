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
    
    def select_suit(self, i):
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        if i < 1 or i > 4:
            return None
        return suits[i-1]
    
    def handle_win(self):
        player1 = self.players[0]
        player2 = self.players[1]
        winner = ""
        # Both players have cards left, so the game ended by running out of cards
        # Winner is the player with the lowest point hand
        # That player gains points equal to the difference between their two hands' scores
        if len(player1.hand) > 0 and len(player2.hand) > 0:
            points = player1.get_hand_value() - player2.get_hand_value()
            # if points is positive, then player2 won
            if points > 0: 
                player2.points += points
                winner = "Player 2"
            # if negative, then player1 won
            else: 
                player1.points -= points
                winner = "Player 1"
        # else, if player1 has cards left then player2 won
        elif len(player1.hand) > 0:
            player2.points += player1.get_hand_value()
            winner = "Player 2"
        # else, player1 won
        else:
            player1.points += player2.get_hand_value()
            winner = "Player 1"
        return winner
    
    def list_points(self):
        return f"Player 1: {self.players[0].points}\nPlayer 2: {self.players[1].points}\n"

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
                    card = player.draw(self.deck)
                    if card is None:
                        round = False  # if no cards are left in the deck/discard then the game is over
                        break
                    print(f"No valid cards. Drew {str(card)}")
                if not round:
                    break
                print("Your Hand:\n" + player.list_hand())
                print(f"Top Card: {self.deck.peek_discard()}")
                num_cards = len(player.hand)
                valid_choice = False
                while not valid_choice:
                    choice = int(input("Enter the number of the card you wish to play: "))
                    if choice < 1 or choice > num_cards:
                        print("Invalid Number")
                    else:
                        played_card = player.hand[choice-1]
                        if not self.is_card_valid(played_card):
                            print("Invalid Card")
                        else:
                            valid_choice = True
                            played_card = player.hand.pop(choice-1)
                self.deck.discard_card(played_card)
                if played_card.value == 8:
                    choice = int(input(f"1. Clubs\n2. Diamonds\n3. Hearts\n4. Spades\nYou played an Eight! Choose a suit for the next play (default is {played_card.suit})"))
                    suit = self.select_suit(choice)
                    if suit is None:
                        suit = played_card.suit
                    self.deck.set_top_suit(suit)
                if len(player.hand) == 0:
                    round = False
                else:
                    self.change_player()
            winner = self.handle_win()
            choice = input("Would you like to play again? (Y/n): ")
            playing = choice.lower() == 'y'