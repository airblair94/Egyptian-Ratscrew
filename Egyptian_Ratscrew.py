'''
Created on Apr 26, 2013

@author: brush
'''

from stack import *
from queue import *
from Deck import *
import time

DK1 = Deck()
def game(Deck):
    original_deck = Deck
    print "Hello"
    Deck.shuffle_deck()
    player1 = Deck.deal_a_hand(26)
    player2 = Deck
    print "cards have been dealt, time to play"
    print "player 1 use 'a' to play a card and 's' to slap"
    print "player 2 use 'k' to play a card and 'l' to slap"
    print "game will show number of cards in each players hand after stack is won"
    game_pile = Stack()
    #print player1
    #print player2
    just_played = "nothing the game just started silly"
    while not(player1.empty() or player2.empty()):
        print game_pile.rep[-5:]
        #rules for jack
        if len(game_pile)>= 2 and (game_pile.rep[-2])[0]== 'J' and (game_pile.rep[-1])[0] !='J' and (game_pile.rep[-1])[0] !='Q' and (game_pile.rep[-1])[0] != 'K' and (game_pile.rep[-1])[0] != 'A':
            time.sleep(1)
            if just_played == 'a':
                print "player 2 wins this stack"
                cards_to_be_got = len(game_pile)
                while cards_to_be_got != 0:
                    player2.put(game_pile.pop())
                    cards_to_be_got = cards_to_be_got - 1
                print "player 1 hand", len(player1)
                print "player 2 hand", len(player2)
            elif just_played == 'k':
                print "player 1 wins this stack"
                cards_to_be_got = len(game_pile)
                while cards_to_be_got != 0:
                    player1.put(game_pile.pop())
                    cards_to_be_got = cards_to_be_got - 1
                print "player 1 hand", len(player1)
                print "player 2 hand", len(player2)
        #rules for Queen
        elif len(game_pile)>= 3 and (game_pile.rep[-3])[0]== 'Q' and (game_pile.rep[-2])[0] !='J' and (game_pile.rep[-2])[0] !='Q' and (game_pile.rep[-2])[0] != 'K' and (game_pile.rep[-2])[0] != 'A' and (game_pile.rep[-1])[0] !='J' and (game_pile.rep[-1])[0] !='Q' and (game_pile.rep[-1])[0] != 'K' and (game_pile.rep[-1])[0] != 'A':
            time.sleep(1)
            if just_played == 'a':
                print "player 2 wins this stack"
                cards_to_be_got = len(game_pile)
                while cards_to_be_got != 0:
                    player2.put(game_pile.pop())
                    cards_to_be_got = cards_to_be_got - 1
                print "player 1 hand", len(player1)
                print "player 2 hand", len(player2)
            elif just_played == 'k':
                print "player 1 wins this stack"
                cards_to_be_got = len(game_pile)
                while cards_to_be_got != 0:
                    player1.put(game_pile.pop())
                    cards_to_be_got = cards_to_be_got - 1
                print "player 1 hand", len(player1)
                print "player 2 hand", len(player2)
        # rules for King
        elif len(game_pile)>= 4 and (game_pile.rep[-4])[0]== 'K' and (game_pile.rep[-3])[0] !='J' and (game_pile.rep[-3])[0] !='Q' and (game_pile.rep[-3])[0] != 'K' and (game_pile.rep[-3])[0] != 'A' and (game_pile.rep[-2])[0] !='J' and (game_pile.rep[-2])[0] !='Q' and (game_pile.rep[-2])[0] != 'K' and (game_pile.rep[-2])[0] != 'A'and (game_pile.rep[-1])[0] !='J' and (game_pile.rep[-1])[0] !='Q' and (game_pile.rep[-1])[0] != 'K' and (game_pile.rep[-1])[0] != 'A':
            time.sleep(1)
            if just_played == 'a':
                print "player 2 wins this stack"
                cards_to_be_got = len(game_pile)
                while cards_to_be_got != 0:
                    player2.put(game_pile.pop())
                    cards_to_be_got = cards_to_be_got - 1
                print len(player1)
                print len(player2)
            elif just_played == 'k':
                print "player 1 wins this stack"
                cards_to_be_got = len(game_pile)
                while cards_to_be_got != 0:
                    player1.put(game_pile.pop())
                    cards_to_be_got = cards_to_be_got - 1
                print "player 1 hand", len(player1)
                print "player 2 hand", len(player2)
        #rules for Ace
        elif len(game_pile)>= 5 and (game_pile.rep[-5])[0]== 'A' and (game_pile.rep[-4])[0] !='J' and (game_pile.rep[-4])[0] !='Q' and (game_pile.rep[-4])[0] != 'K' and (game_pile.rep[-4])[0] != 'A' and (game_pile.rep[-3])[0] !='J' and (game_pile.rep[-3])[0] !='Q' and (game_pile.rep[-3])[0] != 'K' and (game_pile.rep[-3])[0] != 'A'and (game_pile.rep[-2])[0] !='J' and (game_pile.rep[-2])[0] !='Q' and (game_pile.rep[-2])[0] != 'K' and (game_pile.rep[-2])[0] != 'A' and (game_pile.rep[-1])[0] !='J' and (game_pile.rep[-1])[0] !='Q' and (game_pile.rep[-1])[0] != 'K' and (game_pile.rep[-1])[0] != 'A':
            time.sleep(1)
            if just_played == 'a':
                print "player 2 wins this stack"
                cards_to_be_got = len(game_pile)
                while cards_to_be_got != 0:
                    player2.put(game_pile.pop())
                    cards_to_be_got = cards_to_be_got - 1
                print "player 1 hand", len(player1)
                print "player 2 hand", len(player2)
            elif just_played == 'k':
                print "player 1 wins this stack"
                cards_to_be_got = len(game_pile)
                while cards_to_be_got != 0:
                    player1.put(game_pile.pop())
                    cards_to_be_got = cards_to_be_got - 1
                print "player 1 hand", len(player1)
                print "player 2 hand", len(player2)
        just_played = raw_input() #creates raw input option
        #cancels out invalid responses to raw input
        if just_played != "a" and just_played !="k" and just_played != "s" and just_played !="l":
            print "not a valid input"
        #play card options
        if just_played == "a":
            game_pile.push(player1.get())
        elif just_played == "k":
            game_pile.push(player2.get())
        #if there is a good slap
        elif just_played == "s" and (len(game_pile)>=2 and ((game_pile.rep[-1])[0] == (game_pile.rep[-2])[0]) or (len(game_pile) >= 3 and((game_pile.rep[-1])[0]) == ((game_pile.rep[-3])[0]))):
            cards_to_be_got = len(game_pile)
            while cards_to_be_got != 0:
                player1.put(game_pile.pop())
                cards_to_be_got = cards_to_be_got - 1
            assert(game_pile.empty)
            game_pile = Stack()
            print "player 1 won the stack by slap"
            print "player 1 hand", len(player1)
            print "player 2 hand", len(player2)
        elif just_played == "l" and (len(game_pile) >= 2 and((game_pile.rep[-1])[0] == (game_pile.rep[-2])[0]) or (len(game_pile) >= 3 and((game_pile.rep[-1])[0]) == ((game_pile.rep[-3])[0]))):
            cards_to_be_got = len(game_pile)
            while cards_to_be_got != 0:
                player2.put(game_pile.pop())
                cards_to_be_got = cards_to_be_got - 1
            assert(game_pile.empty)
            game_pile = Stack()
            print "player 2 won the stack by slap"
            print "player 1 hand", len(player1)
            print "player 2 hand", len(player2)
        #if there is a bad slap
        elif just_played == "s" and len(game_pile) < 2 or (not ((game_pile.rep[-1])[0] == (game_pile.rep[-2])[0]) or (len(game_pile) < 3 and((game_pile.rep[-1])[0]) == ((game_pile.rep[-3])[0]))):
            print"not a valid slap"
        elif just_played == "l" and len(game_pile) < 2 or (not ((game_pile.rep[-1])[0] == (game_pile.rep[-2])[0]) or (len(game_pile) < 3 and((game_pile.rep[-1])[0]) == ((game_pile.rep[-3])[0]))):
            print"not a valid slap"
        

            
    #game is over here    
    if player1.empty():
        print "player 2 is far too powerful for player 1 - player 2 wins (yes or no)"
        if raw_input("would you like to play again?") == "yes":
            return game(original_deck)
        else:
            return "thanks for playing"
    if player2.empty():
        print "player 1 has shown that he is the best in the land - player 1 wins (yes or no)"
        if raw_input("would you like to play again?") == "yes":
            return game(original_deck)
        else:
            return "thanks for playing"
game(DK1)

   #http://www.daniweb.com/software-development/python/threads/441615/python-classes-and-methods-example 

    


        

