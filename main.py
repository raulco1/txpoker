#import kivy module
import random

import kivy

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require('1.9.0')

# Importing Drop-down from the module to use in the program
from kivy.uix.dropdown import DropDown

# The Button is a Label with associated actions
# that are triggered when the button is pressed
# (or released after a click / touch)
from kivy.uix.button import Button

# another way used to run kivy app
from kivy.base import runTouchApp

from kivy.config import Config
Config.set('graphics', 'resizable', True)





from poker import Card
import random
import poker



deck = list(Card)
random.shuffle(deck)

#Player 1
p1Hand = [deck.pop() for __ in range(2)]

def txt_to_image(card):
    print("hrer" , card[1])
    suits = {'♣': 'spades', '♦': 'diamonds', '♥': 'hearts', '♠': 'clubs' }
    special_ranks = {'T': '10', 'J': 'jack', 'Q': 'queen', 'K': 'king', 'A': 'ace'}

    #image = f'{special_ranks[card[0]]}_of_{suits[card[1]]}'
    return suits[str(card[1])]





print(p1Hand)
print(p1Hand[0])
print(txt_to_image(p1Hand[0]))


flop = [deck.pop() for __ in range(3)]
turn = deck.pop()
river = deck.pop()

#
# print(flop.Suit)
# print(turn)
# print(turn.__str__())
#
#
# def shuffle():
#     suits = ["spades", "hearts", "diamonds", "clubs"]
#     rankings = range(2, 11) #Faces cards how to add
#     # 11-Jack, 12-Queen, 13-King, 14-Ace
#
#     global deck
#     deck = []
#     for suit in suits:
#         for rank in rankings:
#             deck.append(f'{rank}_of_{suit}')
# shuffle()





