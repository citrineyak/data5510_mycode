from DeckOfCards import *
import sys

deck = DeckOfCards()

# Logic for calling a replay

def play_again():
    play = input("Play again? y/n:")
    if play == "y":
        play_game()
    else:
        print("Have a good day!")
        sys.exit()

# Contains the game

def play_game():
    deck.print_deck()
    deck.shuffle_deck()
    print("\n")
    deck.print_deck()

#Drawing user cards and checking for aces

    users_aces = 0
    user_card1 = deck.get_card()
    if user_card1.face == "Ace":
        users_aces += 1
    user_card2 = deck.get_card()
    if user_card2.face == "Ace":
        users_aces += 1
    

    user_score = user_card1.val + user_card2.val
    print("Your cards are the", user_card1.face, "of", user_card1.suit, "and the", user_card2.face, "of", user_card2.suit,"\nUser score:", user_score)

# Getting dealer's cards and checking for aces

    dealer_card1 = deck.get_card()
    dealer_aces = 0
    if dealer_card1.face == "Ace":
        dealer_aces += 1
    dealer_card2 = deck.get_card()
    if dealer_card2.face == "Ace":
        dealer_aces += 1

    dealer_score = dealer_card1.val + dealer_card2.val
    

    bust = 0
    while bust == 0:

# Hit loop. Checks for if there are aces when user's score exceeds 21

        hit = input("Do you want to hit? y/n:")

        if hit == "y":
            user_card3 = deck.get_card()
            if user_card3.face == "Ace":
                users_aces += 1
            user_score += user_card3.val
            print("You drew a",user_card3.face, "of", user_card3.suit)
            
            if user_score > 21:
                if users_aces > 0:
                    users_aces -= 1
                    user_score -= 10
                else:
                    bust = 1
            print("Your new score is", user_score)

# Logic for when the dealer needs to go. Very similar to user logic

        else:
            print("The dealer has a", dealer_card1.face, "of", dealer_card1.suit, "and a", dealer_card2.face, "of", dealer_card2.suit,"\nThe dealer's score is", dealer_score)
            dealer_bust = 0
            while dealer_bust == 0:
                if dealer_score < 17:
                    dealer_new_card = deck.get_card()
                    if dealer_new_card.face == "Ace":
                        dealer_aces += 1
                    print("The dealer drew a ", dealer_new_card.face, "of", dealer_new_card.suit)
                    dealer_score += dealer_new_card.val
                    
                    if dealer_score > 21:
                        if dealer_aces > 0:
                            dealer_aces -= 1
                            dealer_score -= 10
                            print("The dealers new score is", dealer_score)
                            
                        else:
                            print("The dealers new score is", dealer_score)
                            print("The dealer busted!")
                            dealer_bust = 1

# Logic for who wins (excludes dealer busting)     
              
                else:
    
                    if user_score > dealer_score:
                        print("You beat the dealer's score of", dealer_score, "so you win!")
                        play_again()

                    else:
                        print("Sorry, the dealer got", dealer_score, "so you lose :(")
                        play_again()
            print("You win!")
            play_again()
    print("Sorry, you busted! You lose.")
    play_again()

# Code starts running here. Welcome message and play game function call

print("\nWelcome to Blackjack! I am your dealer, and will be dealing 2 cards to you. If your cards exceed 21, you bust! Try to beat my score!\n")
play_game()