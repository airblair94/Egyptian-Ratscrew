'''
Created on May 13, 2013

@author: brush
'''
from random import shuffle
from queue import *

class Deck:
    def __init__(self):
        suits = ('C', 'S', 'H', 'D')
        ranks = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
        self.Deck = [rank+suit for rank in ranks for suit in suits]
        
    
    def __repr__(self):
        return str(self.Deck)
       
            
    def deal_a_card(self):
        print "\n  deal a card", self.Deck[self.next_card]
        self.next_card += 1
        
    def shuffle_deck(self):
        shuffle(self.Deck)
        print "\nshuffled deck"
    
    def empty(self):
        return self.Deck == []
    
    def put(self, v):
        self.Deck.append(v)
    
    def get(self):
        return self.Deck.pop(0)
        
    def deal_a_hand(self, hand_size):
        hand_size_counter = hand_size
        hand = Queue()
        while hand_size_counter != 0:
            hand.put(self.Deck.pop())
            hand_size_counter= hand_size_counter -1        
        return hand
    
    def  __len__(self):
        counter = 1
        for i in range(len(self.Deck)-1):
            counter = counter + 1
        return counter

"""        
Deck1 = Deck()
Deck1.shuffle_deck()
print Deck1
hand1= Deck1.deal_a_hand(26)
print hand1
"""