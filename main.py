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

# another way used to run kivy app
from kivy.base import runTouchApp

import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
Config.set('graphics', 'resizable', True)

from poker import Card
import random

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
savedDeck = deck #Refernce

#Player 1
p1Hand = [deck.pop() for __ in range(2)]

#Player 2
p2Hand = [deck.pop() for __ in range(2)]

#Dealing
flop = [deck.pop() for __ in range(3)]
turn = deck.pop()
river = deck.pop()
#add burn cards




class pokerGrd(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 4
        self.rows = 15

        Suits = ["Spades", "Hearts", "Clubs", "Diamond"]
        Ranks = ["A", 2, 3, 4, 5, 6, 7, 8, 9, "T", "j", "Q", "K"]

        #determine buttons state: instance is the object, value is the down
        def callback(instance, value):
            print('My button <%s> state is <%s>' % (instance, value))

        for i in Suits:
            if i in ['Hearts', "Diamond"]:
                btn = Button(text=str(i), background_color=(1,0,0,1))
            else:
                btn = Button(text=str(i), background_color = (0,0,0,1))

            btn.suit = i  # assign suit
            #btn.bind(on_release=lambda i=i: self.clicked(i))
            self.add_widget(btn)

        for i in Ranks:
            for j in range(4):
                btn = Button(text=str(i), on_release=self.clicked)
                btn.rank = i
                btn.suit = Suits[j]  # assign suit
                btn.bind(state=callback)
                #btn.bind(on_release=lambda i=i: self.clicked(i))
                self.add_widget(btn)

    def clicked(self, botn):
        print(f"button suit: {botn.suit}, rank:{botn.rank}, currnt value: {botn.text}")  # print text and suit
        botn.text = "x" #Update action

class CLayout(Widget):
    def press(self, instance):
        name = self.name.text
        self.name.text = ""


class TxPoker(App):
    def build(self):
        return CLayout()






#if __name__  == '__main__':
#    txPoker().run()


myApp = TxPoker()
myApp.run()

# class TxPoker(App):
#
#     def build(self):
        #
        # Rl = FloatLayout()
        #
        # p1card1 = Button(size_hint=(.15, .3),
        #              background_normal = 'PNG-cards-1.3/back_of_card.jpg',
        #              pos_hint = {'center_x':.3, 'center_y':.2},
        #              background_down = 'PNG-cards-1.3/' + txt_to_image(p1Hand[0]) + '.png',
        #              text='Hello world')
        #
        # print(p1card1)
        #
        #
        # p1card2 = Button(size_hint=(.15, .3),
        #                  background_normal='PNG-cards-1.3/back_of_card.jpg',
        #                  pos_hint={'center_x': .7, 'center_y': .2},
        #                  background_down='PNG-cards-1.3/' + txt_to_image(p1Hand[1]) + '.png',
        #                  text='Hello world')
        #
        #
        #
        # # adding widget i.e button
        # Rl.add_widget(p1card1)
        # Rl.add_widget(p1card2)
        # #Rl.add_widget(btn1)
        #
        # # return the layout

        #return RL







# run the app
# if __name__ == "__main__":
#myApp = TxPoker()
#TxPoker().run()
#myApp.run()



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





