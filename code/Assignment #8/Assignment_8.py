# Created by: Hamza Salman
# Created for: Ics3U
#Created on: November 2016
#This is a black jack game similar to our last assignment but this time it is using an actual deck lf cards rather than numbers and uses classes.

import ui
import console
from cards import *

def play_button_touch_up_inside(sender):
	# this function sets up the game to be played

    global dealer_total
    global player_total
    global player_card_one_image
    global player_card_one_value
    global player_card_two_image
    global player_card_two_value
    global player_card_three_image
    global player_card_three_value
    global computer_card_one_image
    global computer_card_one_value
    global computer_card_two_image
    global computer_card_two_value
    global computer_card_three_image
    global computer_card_three_value


    view['result_label'].text = ''

    player1 = Cards()
    player_card_one_image = player1.get_card_one_image()
    player_card_one_value = player1.get_card_one_value()

    player2 = Cards()
    player_card_two_image = player2.get_card_two_image()
    player_card_two_value = player2.get_card_two_value()

    player3 = Cards()
    player_card_three_image = player3.get_card_two_image()
    player_card_three_value = player3.get_card_two_value()

    computer1 = Cards()
    computer_card_one_image = computer1.get_card_four_image()
    computer_card_one_value = computer1.get_card_four_value()

    computer2 = Cards()
    computer_card_two_image = computer2.get_card_five_image()
    computer_card_two_value = computer2.get_card_five_value()

    computer3 = Cards()
    computer_card_three_image = computer3.get_card_six_image()
    computer_card_three_value = computer3.get_card_six_value()
    
    dealer_total = computer_card_one_value + computer_card_two_value + computer_card_three_value

    
    #dealer_total = 0
    player_total = 0

def check_button_touch_up_inside(sender):
	# this functionchecks and compares the final values. it also reveals the dealers cards.
	
    global dealer_total
    #global computer_card_one_value
    #global computer_card_two_value
    #global computer_card_three_value
    
    #dealer_total = computer_card_one_value + computer_card_two_value + computer_card_three_value
	
    view['computer_card_one_imageview'].image = ui.Image('card:' + str(computer_card_one_image))
    view['computer_card_two_imageview'].image = ui.Image('card:' + str(computer_card_two_image))
    view['computer_card_three_imageview'].image = ui.Image('card:' + str(computer_card_three_image))
    view['computer_total_label'].text = 'Dealer Total: ' + str(dealer_total)
    
    if player_total <= 21:
        if dealer_total > 21:
            view['result_label'].text = 'You Win!'
        elif dealer_total <= 21:
            if dealer_total < player_total:
                view['result_label'].text = 'You Win!'
            elif dealer_total > player_total:
                view['result_label'].text = 'You Lose!'
            elif dealer_total == player_total:
                view['result_label'].text = 'It is a Tie! Dealer Wins!'
    if player_total > 21:
        view['result_label'].text = 'You Lose!'
        if dealer_total > 21:
            view['result_label'].text = 'You both Lose!'
    

def player_card_one_touch_up_inside(sender):
	# this function flips over the first card when it is touched.
	
    global player_card_one_value
    #global player_card_one_image
    global player_total
    
    
    view['player_card_one_imageview'].image = ui.Image('card:' + str(player_card_one_image))
    if player_card_one_value == 1:
        ace = console.alert('info','would you like 1 or 11', '1', '11', hide_cancel_button=True)
        if ace == 1:
            player_total = player_total + player_card_one_value
            view['player_total_label'].text = 'Player Total: ' + str(player_total)
        else:
            player_total = int(player_total) + 11
            view['player_total_label'].text = 'Player Total: ' + str(player_total)
    else:
        player_total = player_total + player_card_one_value
        view['player_total_label'].text = 'Player Total: ' + str(player_total)
    
def player_card_two_touch_up_inside(sender):
	# this function flips over the second card when it is touched.
	
    global player_total
    global player_card_two_value
    #global player_card_two_image
    
	
    view['player_card_two_imageview'].image = ui.Image('card:' + str(player_card_two_image))
    if player_card_two_value == 1:
        ace = console.alert('info','would you like 1 or 11', '1', '11', hide_cancel_button=True)
        if ace == 1:
            player_total = player_total + player_card_two_value
            view['player_total_label'].text = 'Player Total: ' + str(player_total)
        else:
            player_total = int(player_total) + 11
            view['player_total_label'].text = 'Player Total: ' + str(player_total)
    else:
        player_total = player_total + player_card_two_value
        view['player_total_label'].text = 'Player Total: ' + str(player_total)
    
def player_card_three_touch_up_inside(sender):
	# this function flips over the third card when it is touched.
	
    global player_total
    global player_card_three_value
    #global player_card_three_image
    
	
    third_card = console.alert('Third Card', 'Would you like a third card?', 'Yes', 'No', hide_cancel_button=True)
    
    if third_card == 1:
        view['player_card_three_imageview'].image = ui.Image('card:' + str(player_card_three_image))
        if player_card_three_value == 1:
            ace = console.alert('info','would you like 1 or 11', '1', '11', hide_cancel_button=True)
            if ace == 1:
                player_total = player_total + player_card_three_value
                view['player_total_label'].text = 'Player Total: ' + str(player_total)
            else:
                player_total = int(player_total) + 11
                view['player_total_label'].text = 'Player Total: ' + str(player_total)
        else:
            player_total = player_total + player_card_three_value
            view['player_total_label'].text = 'Player Total: ' + str(player_total)
     
    else:
        pass
    
    
view = ui.load_view()
view.present('full_screen')

view['computer_card_one_imageview'].image = ui.Image('card:BackBlue4')
view['computer_card_two_imageview'].image = ui.Image('card:BackBlue4')
view['computer_card_three_imageview'].image = ui.Image('card:BackBlue4')
view['player_card_one_imageview'].image = ui.Image('card:BackBlue4')
view['player_card_two_imageview'].image = ui.Image('card:BackBlue4')
view['player_card_three_imageview'].image = ui.Image('card:BackGreen2')
