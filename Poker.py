import random


class Card(object):  # Initialization of card with value and suit
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


class Deck(object):
    def shuffle(self):  # Adding shuffle and pop of the first card
        random.shuffle(self.cards)
        print("The deck is shuffled")

    def pop(self):
        return self.cards.pop(0)


class FullDeck(Deck):  # Creating the full deck
    def __init__(self):
        self.cards = []
        suits = {"Hearts": "♡", "Spades": "♠", "Diamonds": "♢", "Clubs": "♣"}
        values = {"Two": 2,
                  "Three": 3,
                  "Four": 4,
                  "Five": 5,
                  "Six": 6,
                  "Seven": 7,
                  "Eight": 8,
                  "Nine": 9,
                  "Ten": 10,
                  "Jack": 11,
                  "Queen": 12,
                  "King": 13,
                  "Ace": 14}