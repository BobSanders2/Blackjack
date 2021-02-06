from ..Deck import Deck


def create_deck():
    deck = Deck()
    deck.shuffle_cards()
    return deck


def get_new_card(entity, deck):
    entity.cards.append(deck.deck[deck.get_next_card()])
    pass


def calculate_points(entity):
    suits = ["King", "Queen", "Jack", "Ace"]

    entity_points = 0

    for i in entity.cards:
        try:
            entity_points += int(i.number)
        except ValueError:
            if i.number in suits and i.number != "Ace":
                entity_points += 10
            elif i.number == "Ace":
                if (entity_points + 11) > 21:
                    entity_points += 1
                else:
                    entity_points += 11
    return entity_points


def check_for_winner(player, dealer, end_of_turns=False):
    player_points = calculate_points(player)
    dealer_points = calculate_points(dealer)

    if not end_of_turns:
        if player_points == 21 and dealer_points == 21:
            return "tie"
        elif player_points == 21:
            return "win"
        elif dealer_points == 21:
            return "loss"
        elif player_points > 21:
            return "loss"
        else:
            return None

    if end_of_turns:
        if player_points > dealer_points or dealer_points > 21:
            return "win"
        elif player_points < dealer_points <= 21:
            return "loss"
        else:
            return "tie"


def end_of_game(winner):
    if winner == "tie":
        raise Tie

    if winner == "player":
        raise Victory

    if winner == "dealer":
        raise Defeat
