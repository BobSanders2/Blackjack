from time import sleep
from .Interface import generate_readable_list, get_command
from .start_game import start_game
from .Game import create_deck
from .Game.Info import game_help

PLAY = "play"
HELP = "help"
QUIT = "quit"
COMMANDS = [PLAY, HELP, QUIT]

YES = "yes"
NO = "no"
CONTINUE_COMMANDS = [YES, NO]


def main():
    title_seen = False
    final_end = False
    while not final_end:
        if not title_seen:
            print("""
            ===================================================
            ===================================================
            ===================================================
            
                        Let's play some Blackjack!
            
            ===================================================
            ===================================================
            ===================================================
            
            """)

            sleep(1)

            print(f"Please choose either: {generate_readable_list(COMMANDS)}")
            title_seen = True

        else:
            pass

        command = get_command(COMMANDS, list_options=False)

        if command == PLAY:
            end_game = False
            continued_game = False
            deck = None
            wins = 0
            loss = 0
            tie = 0
            result = None

            while not end_game:

                print(f"""
     ===============================================================
     ===============================================================

                              Wins: {wins}
                              Loss: {loss}
                              Ties: {tie}

     ===============================================================
     =============================================================== 
             """)
                if not continued_game:
                    deck = create_deck()
                    result = start_game(deck)
                else:
                    result = start_game(deck)

                if result == "win":
                    wins += 1
                elif result == "loss":
                    loss += 1
                elif result == "tie":
                    tie += 1
                elif result == "end game":
                    end_game = True
                    final_end = True

                if not end_game:

                    print(f"Continue? {generate_readable_list(CONTINUE_COMMANDS)}")
                    command = get_command(CONTINUE_COMMANDS, list_options=False)

                    if command == YES:
                        continued_game = True
                        pass
                    if command == NO:
                        end_game = True
                        final_end = True
                        break

        if command == HELP:
            game_help()
            title_seen = False

        if command == QUIT:
            break
