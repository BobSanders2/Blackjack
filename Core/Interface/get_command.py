from .generate_readable_list import generate_readable_list, generate_updated_board
from ..Game import get_new_card, check_for_winner
from time import sleep
from ..Dealer import dealer_turn

HIT = "hit"
STAY = "stay"
END_GAME = "end game"

BASE_COMMANDS = [HIT, STAY, END_GAME]


def get_command(commands, list_options=True):
    while True:
        if list_options:
            print(f"Available Commands: {generate_readable_list(commands)}")

        received_input = input(">>>").lower()

        if received_input in commands:
            return received_input

        print(f"""I didn't understand that command. 
Available commands are: {generate_readable_list(commands)}""")


def get_game_command(deck, dealer, player):

    while True:
        print()
        command = get_command(BASE_COMMANDS)

        if command == "hit":
            get_new_card(player, deck)
            generate_updated_board(deck, player, dealer)
            sleep(2)
            result = check_for_winner(player, dealer)

            if result is not None:
                return result

        if command == "stay":
            return dealer_turn(deck, dealer, player)

        if command == "end game":
            return "end game"

