# Created by: Hamza Salman
# Created for: Ics3U
# Created on: November 2016
# This is the cards class


from deck_of_cards import *
from numpy import *
import random
deck = deck_of_cards()
shuffled_deck = deck.get_cards()
random.shuffle(shuffled_deck)

deck_values = {}
deck_values['Diamonds2'] = 2
deck_values['Diamonds3'] = 3
deck_values['Diamonds4'] = 4
deck_values['Diamonds5'] = 5
deck_values['Diamonds6'] = 6
deck_values['Diamonds7'] = 7
deck_values['Diamonds8'] = 8
deck_values['Diamonds9'] = 9
deck_values['Diamonds10'] = 10
deck_values['DiamondsA'] = 1
deck_values['DiamondsJ'] = 10
deck_values['DiamondsK'] = 10
deck_values['DiamondsQ'] = 10
deck_values['Spades2'] = 2
deck_values['Spades3'] = 3
deck_values['Spades4'] = 4
deck_values['Spades5'] = 5
deck_values['Spades6'] = 6
deck_values['Spades7'] = 7
deck_values['Spades8'] = 8
deck_values['Spades9'] = 9
deck_values['Spades10'] = 10
deck_values['SpadesA'] = 1
deck_values['SpadesJ'] = 10
deck_values['SpadesK'] = 10
deck_values['SpadesQ'] = 10
deck_values['Clubs2'] = 2
deck_values['Clubs3'] = 3
deck_values['Clubs4'] = 4
deck_values['Clubs5'] = 5
deck_values['Clubs6'] = 6
deck_values['Clubs7'] = 7
deck_values['Clubs8'] = 8
deck_values['Clubs9'] = 9
deck_values['Clubs10'] = 10
deck_values['ClubsA'] = 1
deck_values['ClubsJ'] = 10
deck_values['ClubsK'] = 10
deck_values['ClubsQ'] = 10
deck_values['Hearts2'] = 2
deck_values['Hearts3'] = 3
deck_values['Hearts4'] = 4
deck_values['Hearts5'] = 5
deck_values['Hearts6'] = 6
deck_values['Hearts7'] = 7
deck_values['Hearts8'] = 8
deck_values['Hearts9'] = 9
deck_values['Hearts10'] = 10
deck_values['HeartsA'] = 1
deck_values['HeartsJ'] = 10
deck_values['HeartsK'] = 10
deck_values['HeartsQ'] = 10

class Cards:
    #This is the cards class

    def __init__(self, card_one_image = 'card:BackBlue3', card_one_value = 0, card_two_image = 'card:BackBlue3', card_two_value = 0, card_three_image = 'card:BackBlue3', card_three_value = 0, card_four_image = 'card:BackBlue3', card_four_value = 0, card_five_image = 'card:BackBlue3', card_five_value = 0, card_six_image = 'card:BackBlue3', card_six_value = 0):
        
        self.__card_one_value = 0
        self.__card_one_image = 'card:BackBlue3'
        self.__card_two_value = 0
        self.__card_two_image = 'card:BackBlue3'
        self.__card_three_value = 0
        self.__card_three_image = 'card:BackBlue3'
        self.__card_four_value = 0
        self.__card_four_image = 'card:BackBlue3'
        self.__card_five_value = 0
        self.__card_five_image = 'card:BackBlue3'
        self.__card_six_value = 0
        self.__card_six_image = 'card:BackBlue3'
        
        self.set_card_one_image(card_one_image)
        self.set_card_one_value(card_one_value)
        self.set_card_two_image(card_two_image)
        self.set_card_two_value(card_two_value)
        self.set_card_three_image(card_three_image)
        self.set_card_three_value(card_three_value)
        self.set_card_four_image(card_four_image)
        self.set_card_four_value(card_four_value)
        self.set_card_five_image(card_five_image)
        self.set_card_five_value(card_five_value)
        self.set_card_six_image(card_six_image)
        self.set_card_six_value(card_six_value)
        #print card_one_image
        
    def set_card_one_image(self, card_one_image):
        card_one_image = shuffled_deck[1]
        shuffled_deck.remove(card_one_image)
        #print shuffled_deck
        self.__card_one_image = card_one_image
    def get_card_one_image(self):
        return self.__card_one_image
    def set_card_one_value(self, card_one_value):
        card_one_value = deck_values[self.__card_one_image]
        self.__card_one_value = card_one_value
    def get_card_one_value(self):
        return self.__card_one_value
        
    def set_card_two_image(self, card_two_image):
        card_two_image = shuffled_deck[1]
        shuffled_deck.remove(card_two_image)
        #print shuffled_deck
        self.__card_two_image = card_two_image
    def get_card_two_image(self):
        return self.__card_two_image
    def set_card_two_value(self, card_two_value):
        card_two_value = deck_values[self.__card_two_image]
        self.__card_two_value = card_two_value
    def get_card_two_value(self):
        return self.__card_two_value
        
    def set_card_three_image(self, card_three_image):
        card_three_image = shuffled_deck[1]
        shuffled_deck.remove(card_three_image)
        #print shuffled_deck
        self.__card_three_image = card_three_image
    def get_card_three_image(self):
        return self.__card_three_image
    def set_card_three_value(self, card_three_value):
        card_three_value = deck_values[self.__card_three_image]
        self.__card_three_value = card_three_value
    def get_card_three_value(self):
        return self.__card_three_value
        
    def set_card_four_image(self, card_four_image):
        card_four_image = shuffled_deck[1]
        shuffled_deck.remove(card_four_image)
        #print shuffled_deck
        self.__card_four_image = card_four_image
    def get_card_four_image(self):
        return self.__card_four_image
    def set_card_four_value(self, card_four_value):
        card_four_value = deck_values[self.__card_four_image]
        self.__card_four_value = card_four_value
    def get_card_four_value(self):
        return self.__card_four_value
        
    def set_card_five_image(self, card_five_image):
        card_five_image = shuffled_deck[1]
        shuffled_deck.remove(card_five_image)
        #print shuffled_deck
        self.__card_five_image = card_five_image
    def get_card_five_image(self):
        return self.__card_five_image
    def set_card_five_value(self, card_five_value):
        card_five_value = deck_values[self.__card_five_image]
        self.__card_five_value = card_five_value
    def get_card_five_value(self):
        return self.__card_five_value
        
    def set_card_six_image(self, card_six_image):
        card_six_image = shuffled_deck[1]
        shuffled_deck.remove(card_six_image)
        #print shuffled_deck
        self.__card_six_image = card_six_image
    def get_card_six_image(self):
        return self.__card_six_image
    def set_card_six_value(self, card_six_value):
        card_six_value = deck_values[self.__card_six_image]
        self.__card_six_value = card_six_value
    def get_card_six_value(self):
        return self.__card_six_value
