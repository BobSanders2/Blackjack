from ..Game import calculate_points


def generate_readable_list(list_to_process):
    processed_list = ["\"{}\"".format(item) for item in list_to_process]
    delimiter = ", "

    if len(processed_list) == 2:
        delimiter = " or "
    return delimiter.join(processed_list)


def generate_readable_cards(entity):
    processed_list = ["{suit}-{number}".format(suit=i.suit, number=i.number) for i in entity.cards]
    delimiter = ", "

    return delimiter.join(processed_list)


def generate_updated_board(deck, player, dealer):
    print(f"""
    ===============================================================
    ===============================================================
                            Dealers Cards:

    {generate_readable_cards(dealer) if dealer.is_turn == True else "Hidden Card"} / {deck.deck[3].suit if not dealer.is_turn else ""} {deck.deck[3].number if not dealer.is_turn else ""} 

    --------------------------------------------------------------
                            Your cards: 

    {generate_readable_cards(player)}

    Points: {calculate_points(player)}
    ===============================================================
    Cards left in deck: {deck.remaining_amount_of_cards}
    ===============================================================
    ===============================================================   
    """)


def generate_updated_board_dealer(deck, player, dealer):
    print(f"""
    ===============================================================
    ===============================================================
                            Dealers Cards:

    {generate_readable_cards(dealer)}

    Points: {calculate_points(dealer)}
    --------------------------------------------------------------
                            Your cards: 

    {generate_readable_cards(player)}

    Points: {calculate_points(player)}
    ===============================================================
    Cards left in deck: {deck.remaining_amount_of_cards}
    ===============================================================
    ===============================================================   
    """)


