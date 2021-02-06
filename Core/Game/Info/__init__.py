from ...Interface import get_command, generate_readable_list

RULES = "rules"
TIPS = "tips"
MORE_INFO = "more info"
GO_BACK = "go back"
HELP_COMMANDS = [RULES, TIPS, MORE_INFO, GO_BACK]

OBJECT = "object of the game"
SCORING = "scoring"
DEAL = "deal"
PLAY = "play"
RULES_COMMANDS = [OBJECT, SCORING, DEAL, PLAY, GO_BACK]


def game_help():

    print(f"""
    ================================================
    ================================================

              What would you like help with? 

    ================================================
    ================================================
    """)

    while True:
        print(f"Please choose either: {generate_readable_list(HELP_COMMANDS)}")

        command = get_command(HELP_COMMANDS, list_options=False)

        if command == RULES:
            while True:
                print(f"Available Help: {generate_readable_list(RULES_COMMANDS)}")
                command = get_command(RULES_COMMANDS, list_options=False)

                if command == OBJECT:
                    print("""            
                                                             ::OBJECT OF THE GAME:: 
                Each participant attempts to beat the dealer by getting a count as close to 21 as possible, without going over 21.
                    
                    """)
                elif command == SCORING:
                    print("""
                                                                 ::SCORING:: 
                It is up to each individual player if an ace is worth 1 or 11. Face cards are 10 and any other card is its pip value.
                
                    """)

                elif command == DEAL:
                    print("""
                                                                 ::THE DEAL::
                When all the players have placed their bets, the dealer gives one card face up to the player and then one card face 
                down to themselves. Another round of cards is then dealt face up to the player, but the dealer takes the second card 
                face up. Thus, the player except the dealer receives two cards face up, and the dealer receives one card face up and 
                                                               one card face down.                 
                    
                    """)

                elif command == PLAY:
                    print("""
                                                                 ::THE PLAY::
                The player goes first and must decide whether to "stay" (not ask for another card) or "hit" (ask for another card in 
                an attempt to get closer to a count of 21, or even hit 21 exactly). Thus, a player may stand on the two cards 
                originally dealt to them, or they may ask the dealer for additional cards, one at a time, until deciding to stay on 
                                        the total (if it is 21 or under), or if the total is over 21, they lose.             
                
                """)

                elif command == GO_BACK:
                    break

        elif command == TIPS:
            print("""
                                                            ::BASIC STRATEGY::
            Winning tactics in Blackjack require that the player play each hand in the optimum way, and such strategy always 
            takes into account what the dealer's upcard is. When the dealer's upcard is a good one, a 7, 8, 9, 10-card, or 
            ace for example, the player should not stop drawing until a total of 17 or more is reached. When the dealer's 
            upcard is a poor one, 4, 5, or 6, the player should stop drawing as soon as he gets a total of 12 or higher. 
            The strategy here is never to take a card if there is any chance of going bust. The desire with this poor holding 
            is to let the dealer hit and hopefully go over 21. Finally, when the dealer's up card is a fair one, 2 or 3, 
                                         the player should stop with a total of 13 or higher.

            With a soft hand, the general strategy is to keep hitting until a total of at least 18 is reached. Thus, 
                         with an ace and a six (7 or 17), the player would not stop at 17, but would hit.      
            
            """)

        elif command == MORE_INFO:
            print("""
            
                        This game was created by Russell Pacheco.
                        
                              I hope you enjoy playing it!            
            
            """)

        elif command == GO_BACK:
            break


