#import kivy module

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


import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config

Config.set('graphics', 'resizable', True)





from poker import Card
import random
import poker


def txt_to_image(card):
    suits = {'♣': 'spades', '♦': 'diamonds', '♥': 'hearts', '♠': 'clubs' }
    special_ranks = {'T': '10', 'J': 'jack', 'Q': 'queen', 'K': 'king', 'A': 'ace'}
    print(card)

    rank = str(card)[0]
    suit = str(card)[1]

    if rank in special_ranks:
        image = f'{special_ranks[rank]}_of_{suits[suit]}'
    else:
        image = f'{rank}_of_{suits[suit]}'
    return image





deck = list(Card)
random.shuffle(deck)

#Player 1
p1Hand = [deck.pop() for __ in range(2)]


flop = [deck.pop() for __ in range(3)]
turn = deck.pop()
river = deck.pop()


print(txt_to_image(p1Hand[0]))





class TxPoker(App):

    def build(self):

        Rl = FloatLayout()

        p1card1 = Button(size_hint=(.15, .3),
                     background_normal = 'PNG-cards-1.3/back_of_card.jpg',
                     pos_hint = {'center_x':.3, 'center_y':.2},
                     background_down = 'PNG-cards-1.3/' + txt_to_image(p1Hand[0]) + '.png',
                     text='Hello world')

        print(p1card1)


        p1card2 = Button(size_hint=(.15, .3),
                         background_normal='PNG-cards-1.3/back_of_card.jpg',
                         pos_hint={'center_x': .7, 'center_y': .2},
                         background_down='PNG-cards-1.3/' + txt_to_image(p1Hand[1]) + '.png',
                         text='Hello world')



        # adding widget i.e button
        Rl.add_widget(p1card1)
        Rl.add_widget(p1card2)
        #Rl.add_widget(btn1)

        # return the layout
        return Rl






# run the app
if __name__ == "__main__":
    TxPoker().run()




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





