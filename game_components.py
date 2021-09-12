from random import shuffle
from itertools import product


class Card:
    def __init__(self, suit, card_name):
        if card_name in ["J", "Q", "K"]:
            self.value = 10
        elif card_name in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
            self.value = card_name
        else:
            self.value = [1, 11]
        self.card_name = str(card_name) + " of " + suit

    def __repr__(self):
        return self.card_name


class Hand:
    def __init__(self):
        self.cards_in_hand = []

    def hand_value(self):
        possible_values = []
        possible_aces = []
        for card in self.cards_in_hand:
            if type(card.value) is not list:
                possible_values.append(card.value)
            else:
                possible_aces.append(card.value)

        possible_values = sum(possible_values)
        possible_aces = list(product(*possible_aces))
        possible_final_values = []
        for each in possible_aces:
            possible_final_values.append(sum(each) + possible_values)
        current_answer = 0
        for each in possible_final_values:
            if each > current_answer and each <= 21:
                current_answer = each
        if current_answer == 0:
            output = min(possible_final_values)
        else:
            output = current_answer
        return output


class Player:
    def __init__(self, wallet):
        self.wallet = wallet
        self.hand = Hand()

    def print_hand(self):
        print("Your hand is: ")
        for card in self.hand.cards_in_hand:
            print(card.value)


class Dealer():
    def __init__(self):
        self.deck = []
        for suit in ["Club", "Diamond", "Heart", "Spade"]:
            for val in ["A", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]:
                self.deck.append(Card(suit, val))
        shuffle(self.deck)
        self.hand = Hand()

    def deal(self, target):
        target.hand.cards_in_hand.append(self.deck.pop())

    def print_opening_hand(self):
        print("Dealers hand is")
        print(self.hand.cards_in_hand[0].value)

    def print_hand(self):
        print("Dealer hand is")
        for card in self.hand.cards_in_hand:
            print(card.value)


class Wallet:
    def __init__(self, amount):
        self.amount = amount
