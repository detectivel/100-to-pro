from hand import Hand
from deck import Deck
from art import logo
from blackjack_game_logic import BlackjackGame


# Function to prompt the player to Hit or Stand
def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop

    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's': ")

        if x[0].lower() == 'h':
            hand.add_card(deck.deal())
            hand.adjust_for_ace()

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break


# Function to take hits
def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


# The game logic
if __name__ == "__main__":
    game = BlackjackGame()

    while True:
        print(logo)
        print('Welcome to Blackjack! Get as close to 21 as you can without going over!\n'
              'Dealer hits until she reaches 17. Aces count as 1 or 11.')

        # Create & shuffle the deck, deal two cards to each player
        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        dealer_hand = Hand()

        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        # Show cards (but keep one dealer card hidden)
        game.show_some(player_hand, dealer_hand)

        playing = True
        while playing:
            # Prompt for Player to Hit or Stand
            hit_or_stand(deck, player_hand)

            # Show cards (but keep one dealer card hidden)
            game.show_some(player_hand, dealer_hand)

            if player_hand.value > 21:
                game.player_busts()
                break

        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

            # Show all cards
            game.show_all(player_hand, dealer_hand)

            if dealer_hand.value > 21:
                game.dealer_busts()
            elif dealer_hand.value > player_hand.value:
                game.dealer_wins()
            elif dealer_hand.value < player_hand.value:
                game.player_wins()
            else:
                game.push()

                # Ask to play again
        new_game = input("Would you like to play another hand? Enter 'y' or 'n': ")
        if new_game[0].lower() == 'y':
            continue
        else:
            print("Thanks for playing!")
            break
