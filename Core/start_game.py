from .Interface.get_command import get_game_command
from .Interface.generate_readable_list import generate_readable_cards
from time import sleep
from .Dealer import Dealer
from .Player import Player
from .Game import check_for_winner, calculate_points

WIN = "win"
LOSS = "loss"
TIE = "tie"
RESULT_COND = [WIN, LOSS, TIE]


def start_game(deck):
    player = Player(cards=[])
    dealer = Dealer(cards=[])

    print("")
    print("")
    sleep(2)
    print("The Dealer will now deal.")
    sleep(3)
    print("")
    print("")

    card_one = deck.get_next_card(new_game=True)
    card_two = deck.get_next_card(new_game=True)
    card_three = deck.get_next_card(new_game=True)
    card_four = deck.get_next_card(new_game=True)

    dealer.cards = [deck.deck[card_two], deck.deck[card_four]]
    player.cards = [deck.deck[card_one], deck.deck[card_three]]

    print(f"""
    ===============================================================
    ===============================================================
                            Dealers Cards:

    Hidden Card / {deck.deck[card_four].suit}-{deck.deck[card_four].number}
    
    --------------------------------------------------------------
                            Your cards: 
   
    {generate_readable_cards(player)}
    
    Points: {calculate_points(player)}
    ===============================================================
    Cards left in deck: {deck.remaining_amount_of_cards}
    ===============================================================
    ===============================================================   
    
    """)

    result = check_for_winner(player, dealer)

    if result is not None:
        return result

    command = get_game_command(deck=deck, dealer=dealer, player=player)

    if command == "end game":
        return "end game"

    if command in RESULT_COND:
        if command == LOSS:
            print("""
    ===================================================
    ===================================================
    ===================================================
    
                        YOU LOST!
    
    ===================================================
    ===================================================
    ===================================================
            """)
            return "loss"

        if command == WIN:
            print("""
    ===================================================
    ===================================================
    ===================================================
    
                        YOU WON!
                        
                        Congrats! 
                                
    ===================================================
    ===================================================
    ===================================================
            """)
            return "win"

        if command == TIE:
            print("""
    ===================================================
    ===================================================
    ===================================================
    
                        It's a tie!
    
    ===================================================
    ===================================================
    ===================================================
            """)
            return "tie"
