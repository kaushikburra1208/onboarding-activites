#!/usr/bin/env python
# coding: utf-8




from random import shuffle

suits = ("Hearts", "Clubs", "Diamonds", "Spades")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two" : 2, "Three" : 3, "Four" : 4, "Five" : 5, "Six" : 6, "Seven" :7, "Eight" : 8, "Nine" : 9, "Ten" : 10, "Jack" : 10, "Queen" : 10, "King" : 10, "Ace" : 11}





class Card:
    def __init__(self,rank,suit):
        
        self.rank = rank
        self.suit = suit
        self.value = values[rank]
        
    def __str__(self):
        
     #   Printing a Card
        
        return self.rank + " of " + self.suit





class Deck:
    def __init__(self):
        
        self.cardlist = []
        
        
        #CREATING A DECK {LIST} OF CARDS FOR A GAME.
        
        for suit in suits:
            for rank in ranks:
                
                current_card = Card(rank,suit)
                
                self.cardlist.append(current_card)
                
    def shuffle_deck(self):
        shuffle(self.cardlist)
    
    def deal_one(self):
        return self.cardlist.pop(0)
    





class Player():
    def __init__(self,name,chips):
        self.name = name
        self.chips = chips
        self.bet = 0
   
    def add_chips(self,chips):
        
#        Adding Chips to the Player
        
        
        self.chips += chips
        
    def remove_chips(self,chips):
        
#        Removing Chips from the Player
        
        
        if chips > self.chips:
            print(" Not Sufficient Chips.")
            print("Current balance = {}".format(self.chips))
            
        else:
            self.chips -= chips
            print("Current value = {}".format(self.chips))





class Hand():
    
    def __init__(self):
        
        self.cards = []
        self.value = 0
        self.ace_count = 0
        
    def __str__(self):
        
       # Printing a hand
        
        
        cards_in_hand = 'Card list is : \n'
        for x in range(len(self.cards)):
            cards_in_hand += str(self.cards[x]) + "\n"
        
        return "This hand has a value of {}.\n\n".format(self.value) + cards_in_hand
    
    def add_card(self,card):
        
      #  Adding a Card to a hand.
        
        
        self.cards.append(card)
        self.value += card.value
        
        if card.rank == "Ace":
            self.ace_count += 1
        
        while self.value > 21 and self.ace_count > 0:
            self.value -= 10
            self.ace_count -= 1
                    






def create_player():
    
#    Funtion to create a Player.
    


    global player
    
    while True:
        player_name = input("\n\nEnter Your Name : ")
        
        if player_name != '':
            break
        else:
            print("Enter a valid name.\n")
    
    while True:
        try:
            start_amount = int(input("Enter starting number of Chips : "))
        except:
            print("Please Enter a valid Number.\n")
        else:
            break
            
    player = Player(player_name,start_amount)    





def take_bet(player):
    while True:
        
        try:
            current_bet = int(input("How much bet would you want to place : "))
            
        except:
            print("Enter a Valid Number of Chips.")
            
        else:
            if current_bet > player.chips:
                print("Not Sufficient Amount. Please try again.")
            else:
                player.bet += current_bet
                player.chips -= current_bet
                break





def adjust_winnings(winner):
    
#    Function to adjust chips at the End of the game to determine the winner and ajdust players chips accordingly 
    
    
    if winner == "player":
        player.chips += int(player.bet*2)
        player.bet = 0
    
    elif winner == "tie" :
        player.chips += player.bet
        player.bet = 0
        
    else:
        player.bet = 0  




def hit_or_stand(player_hand,deck_1):
    
#   Function to give Player a choice to HIT or STAND.
    
    
    global player_playing
    
    while True:
        
        temp = input("HIT OR STAND? : ")

        if temp == '':
            print("Please Choose a valid option.\n")

        if temp[0].lower() == 'h':
            player_hand.add_card(deck_1.deal_one())
            break
            
        elif temp[0].lower() == 's':
            
            player_playing = False
            break
            
        else :
            print("Please Choose a valid option.\n")
    
    if temp[0].lower() == 'h':
        return "h"
    else :
        return "s"





def player_busted():
    
#    Final Winner : Dealer
    
    
    global winner
    
    print("\nPlayer Busted.")
    print("Dealer Wins!\n")
    winner = "dealer"

def dealer_busted():
#    Final Winner : Player
    
    
    global winner
    
    print("\nDealer Busted.")
    print("Player Wins!\n")
    winner = "player"
    
  






def player_wins():

#   Final Winner : Player


global winner

print("Player Wins!\n")
winner = "player"

def dealer_wins():

#    Final Winner : Dealer


global winner

print("Dealer Wins!")
winner = "dealer"  


# In[ ]:


#   Method to  show both hands while Hiding one of dealers Cards.
def show_some_cards(player_hand, dealer_hand):


    print("\nPlayer Cards are : ")
    for card in player_hand.cards:
        print("  " + str(card))
        
    print("\nDealer Cards are : ")
    print("  " + str(dealer_hand.cards[0]))
    print("**Card is Hidden.**\n")
    print("\n")




def show_all_cards(player_hand, dealer_hand):
    
#    Method to show both hands
    
    
    print("\nPlayer Cards are : ")
    for card in player_hand.cards:
        print("  " + str(card))
        
    print("\nDealer Cards are : ")
    for card in dealer_hand.cards:
        print("  " + str(card))
    print("\n")





###Starting the game
def main(player):    
        
    #INITIALIZE A DECK OF CARDS AND SHUFFLE THEM.
    deck_1=Deck()
    deck_1.shuffle_deck()
    
    #CREATE PLAYER AND DEALER HANDS.
    player_hand = Hand()
    dealer_hand = Hand()

    print("\n")
    
    print(player)
    
    
    #TAKE A BET FROM THE PLAYER.
    
    take_bet(player)
    
    #DEAL TWO CARDS TO PLAYER AND DEALER EACH.
    player_hand.add_card(deck_1.deal_one())
    player_hand.add_card(deck_1.deal_one())
    
    dealer_hand.add_card(deck_1.deal_one())
    dealer_hand.add_card(deck_1.deal_one())
    
    
    #SHOW PLAYERS CARDS AND HIDE DEALERS ONE CARD.
    show_some_cards(player_hand, dealer_hand)
    
    #ASK THE PLAYER TO HIT OR STAND.
    
    player_playing = True
    
    while player_playing == True:

        if player_hand.value == 21:
            break
        
        if player_hand.value > 21:
            player_busted()
            break
        
        req = hit_or_stand(player_hand, deck_1)
        
        if req == 's':
            break
        
        show_some_cards(player_hand, dealer_hand)
                 
    show_all_cards(player_hand, dealer_hand)
    
    
    #DEALERS TURN
    
    dealer_playing = True
    
    while dealer_playing:
    
        if player_hand.value <= 21:
            
            while dealer_hand.value <17 :
                print("\nDealer Hits......")
                dealer_hand.add_card(deck_1.deal_one())
                show_all_cards(player_hand, dealer_hand)
                
            dealer_playing = False
                
            if dealer_hand.value > 21:
                dealer_busted()
                break
                        
            elif player_hand.value == dealer_hand.value:
                player_dealer_tie()
                break
                
            elif player_hand.value > dealer_hand.value:
                player_wins()
                break
                
            else:
                dealer_wins()
                break
                
        else:
            break
    adjust_winnings(winner)
    
    print("\n" + str(player))





### Asking the player to play again 
def play_again():
    
    while True:
        
        print("\n")
        temp = input("\n Do you want to play again? : ")
        
        if temp[0].lower() == 'y':
            return True
            break
         elif temp[0].lower() == 'n':
            print("\n")
            print("\nThank You for playing...\n")
            print("\n")
            return False
            break
            
        else :
            print("Please Choose a valid option.\n")



if __name__ == '__main__':
    playing = True
    create_player()
    while playing:
        main(player)
        playing=play_again()













