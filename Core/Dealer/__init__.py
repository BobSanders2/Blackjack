from ..Game import get_new_card, check_for_winner, calculate_points
from time import sleep
from ..Interface.generate_readable_list import generate_updated_board_dealer


def dealer_turn(deck, dealer, player):
    counter = 0

    while True:
        dealer_points = calculate_points(dealer)
        player_points = calculate_points(player)
        generate_updated_board_dealer(deck, player, dealer)
        result = None

        if dealer_points == 20 or dealer_points == 21:
            sleep(2)
            print("")
            print("Dealer will stay")
            print("")
            sleep(2)
            result = check_for_winner(player, dealer, end_of_turns=True)

        elif dealer_points > 21:
            sleep(2)
            result = check_for_winner(player, dealer, end_of_turns=True)

        elif dealer_points > player_points:
            sleep(2)
            print("")
            print("Dealer will stay")
            print("")
            sleep(2)
            result = check_for_winner(player, dealer, end_of_turns=True)

        elif dealer_points >= 17:
            sleep(2)
            print("")
            print("Dealer will stay")
            print("")
            sleep(2)
            result = check_for_winner(player, dealer, end_of_turns=True)

        elif player_points > dealer_points:
            sleep(2)
            print("The Dealer will hit.")
            sleep(2)
            get_new_card(dealer, deck)
            generate_updated_board_dealer(deck, player, dealer)

        elif dealer_points == player_points and dealer_points >= 17:
            sleep(2)
            print("")
            print("Dealer will stay")
            print("")
            sleep(2)
            result = check_for_winner(player, dealer, end_of_turns=True)

        else:
            sleep(2)
            print("The Dealer will hit.")
            sleep(2)
            get_new_card(dealer, deck)
            generate_updated_board_dealer(deck, player, dealer)

        if result is not None:
            return result


class Dealer:
    def __init__(self, cards):
        self.cards = cards
        self.is_turn = False
