# Created by: Hamza Salman
# Created for: Ics3U
# Created on: November 2016
# This is the deck of cards class

import random

class deck_of_cards:
	
    def __init__(self):
        
        cards = ["Diamonds", "Spades", "Clubs", "Hearts"]
        card_sizes = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "J", "K", "Q"]
        deck = []
        for i in cards:
            for v in card_sizes:
                deck.append(i + v)
                
        self.__cards = deck
        
        
    def get_cards(self):
        return self.__cards
