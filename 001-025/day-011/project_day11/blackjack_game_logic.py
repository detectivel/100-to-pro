# Blackjack game class for displaying cards and handling game scenarios
class BlackjackGame:
    def show_some(self, player, dealer):
        print("\nDealer's Hand:")
        print(" <card hidden>")
        print('', dealer.cards[1])
        print("\nPlayer's Hand:", *player.cards, sep='\n ')

    def show_all(self, player, dealer):
        print("\nDealer's Hand:", *dealer.cards, sep='\n ')
        print("Dealer's Hand =", dealer.value)
        print("\nPlayer's Hand:", *player.cards, sep='\n ')
        print("Player's Hand =", player.value)

    def player_busts(self):
        print("Player busts!")

    def player_wins(self):
        print("Player wins!")

    def dealer_busts(self):
        print("Dealer busts!")

    def dealer_wins(self):
        print("Dealer wins!")

    def push(self):
        print("Dealer and Player tie! It's a push.")
