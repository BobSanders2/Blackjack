from .Card import Card
from random import shuffle
from copy import deepcopy
from time import sleep


class Deck:
    def __init__(self):
        self.remaining_amount_of_cards = 52
        self.next_card = 0

        suits = ["Hearts", "Diamonds", "Spades", "Clovers"]
        non_number_rank = ["Ace", "King", "Queen", "Jack"]

        self.deck = [Card(suit, number) for number in range(2, 11) for suit in suits]
        additional_cards = [Card(suit, number) for number in non_number_rank for suit in suits]

        for i in additional_cards:
            self.deck.append(i)

    def get_next_card(self, new_game=False):
        if self.remaining_amount_of_cards < 15:
            if not new_game:
                print(f"""
                    =======================================
                    =======================================
                      There are {self.remaining_amount_of_cards} cards left in the deck!
    
                      Deck will be reshuffled on next card!
                    =======================================
                    =======================================
                """)
                self.shuffle_cards()
            else:
                sleep(2)
                print(f"""
            =======================================
            =======================================
                    Please wait.

                    There is less than 15 cards
                    left in the deck.

                    Deck is being reshuffled.
        
            =======================================
            =======================================
                """)
                sleep(3)
                self.shuffle_cards()

        self.remaining_amount_of_cards -= 1

        old_next_card = deepcopy(self.next_card)
        self.next_card = old_next_card + 1

        return old_next_card

    def shuffle_cards(self):
        shuffle(self.deck)
        self.next_card = 0
        self.remaining_amount_of_cards = 52
        return self.deck





