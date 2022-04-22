import random
import logging
import sys
import time
import copy


##### Logging
logger = logging.getLogger(__name__)
# udskriver kun til konsollen
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

logger.setLevel(logging.CRITICAL)
#######

# New stack of cards when cards is used
new_cards = {'Hearts': ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King'],
        'Diamonds': ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King'],
        'Spades': ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King'],
        'Clubs': ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
        }

cards = copy.deepcopy(new_cards)


# Blackjack combinations
blackjack = {
    1:['Ace', 'Jack'],
    2:['Ace', 'Queen'],
    3:['Ace', 'King'],
    4:['Jack', 'Ace'],
    5:['Queen', 'Ace'],
    6:['King', 'Ace']
}

# logging the cards the player have to control for blackjack
card_logger = []

# pick a random card
def randomCard():
    # If no cards in stack fill it up
    if len(cards) < 1:
        for key, value in new_cards.items():
            cards[key] = value
        logger.log(logging.DEBUG, '\nShuffle new stack of cards.')
        
    logger.log(logging.INFO, 'giving random card')
    # random key from cards
    cardType = random.choice(list(cards))
    # random nr card
    cardNumber = random.choice(cards[cardType])
    # remove card from stack
    cards[cardType].remove(cardNumber)
    if len(cards[cardType]) == 0:
        cards.pop(cardType)
        logger.log(logging.DEBUG, "{} fjernet fra dict".format(cardType))
    return cardNumber, cardType
    
# translate the text card into numeric values
def card_values(card, actualPoints):
    if card == 'Jack' or card == 'Queen' or card == 'King':
        card = 10
    elif card == 'Ace':
        if actualPoints <= 10:
            card = 11
        else:
            card = 1
    return card
    

def main():
    sleepTimer = 6
    humanPlayerStatus = True
    game_on = True
    player_point = 0
    dealer_point = 0

    try:
        while game_on == True:

            # Human player code
            if humanPlayerStatus:
                logger.log(logging.DEBUG, card_logger)
                player_point = 0
                name = "Player 1"
                print("\nWelcome to the Blackjacktable {}!".format(name))
                print("\nIf you wanna Quit press: CTRL + C")
                print("\nLets get started.\nHere is your first card.")
                while game_on == True:

                    # Get card
                    cardNumber, cardType = randomCard()

                    # Add card to cardLogger
                    card_logger.append(cardNumber)

                    # Show card
                    print("\n {} of {} ".format(str(cardNumber), cardType))

                    # Check for blackjack ex. ace & king or jack & ace
                    if card_logger in blackjack.values():
                        print("You have Blackjack...")
                        print('Now its dealers turn.')
                        player_point = 21
                        humanPlayerStatus = False
                        break


                    # Add points to counter
                    player_point += card_values(cardNumber, player_point) 

                    print("You now have {} points.\n".format(player_point))

                    if player_point == 21:
                        print("You have blackjack!")
                        print('Now its dealers turn.')
                        humanPlayerStatus = False
                        logger.log(logging.DEBUG, card_logger)
                        card_logger.clear()
                        break
        
                    if player_point > 21:
                        print("You now have more than 21.")
                        print("You loose this game!")
                        start_again = input("\nDo you want to try again? Y or N ").lower()
                        if start_again == 'n':
                            game_on = False
                        card_logger.clear()
                        break

                    # Ask if player want one more card
                    ask_for_another_card = input('Do you want another card?\n Y or N: ').lower()
                    
                    if ask_for_another_card == 'y':
                        continue
                    else:
                        print("{} you stopped at {} points.\n\n".format(name, player_point))
                        print('Dealers turn.')
                        logger.log(logging.DEBUG, card_logger)
                        humanPlayerStatus = False
                        card_logger.clear()
                        break

            # Dealer code
            elif not humanPlayerStatus:
                logger.log(logging.DEBUG, card_logger)
                dealer_point = 0
                dealerName = 'Dealer'
                print("Here is the dealers first card.")
                humanPlayerStatus = False
                time.sleep(sleepTimer)
                while game_on == True:
                    # Dealer
                    cardNumber, cardType = randomCard()

                    # Add card to cardLogger
                    card_logger.append(cardNumber)

                    # Show card
                    print("\n {} of {} ".format(str(cardNumber), cardType))

                    if card_logger in blackjack.values():
                        print("Dealer have Blackjack...")
                        print('Now its players turn.')
                        dealer_point = 21
                        humanPlayerStatus = True
                        card_logger.clear()
                        break

                    # Add points to counter
                    dealer_point += card_values(cardNumber, dealer_point) 

                    print("Dealer now have {} points.\n".format(dealer_point))
                    time.sleep(2)

                    if dealer_point == 21:
                        print("Dealer have blackjack!")
                        print("Dealer wins the game.")
                        start_again = input("\nDo you want to try again? Y or N: ").lower()
                        if start_again == 'n':
                            game_on = False
                        else:
                            time.sleep(sleepTimer)
                            humanPlayerStatus = True
                            card_logger.clear()
                            break
        
                    if dealer_point > 21:
                        print("\n Dealer now have more than 21")
                        print("{} win this game.\n".format(name))
                        start_again = input("Do you want to try again? Y or N: ").lower()
                        if start_again == 'n':
                            game_on = False
                        else:
                            humanPlayerStatus = True
                            card_logger.clear()
                        break

                    # Another card for dealer if dealer points is less playerpoints
                    if dealer_point < player_point:
                        continue
                    else:
                        print("{} stopped at {} points.".format(dealerName, dealer_point))
                        time.sleep(sleepTimer)
                        print("{name}: {points} Points.".format(name=name, points=player_point))
                        print("Dealer: {} Points.".format(dealer_point))
                        time.sleep(3)

                        # Draw game / Player win game / Dealer win game
                        if player_point == dealer_point:
                            print("\nIts a draw.")
                        elif player_point > dealer_point:
                            print("{} Wins the game.".format(name))
                        else:
                            print("Dealer wins the game")

                        # Start a new game or quit
                        start_again = input("\nDo you want to try again? Y or N: ").lower()
                        if start_again == 'n':
                            game_on = False
                            break
                        else:
                            print('Now its players turn.')
                            humanPlayerStatus = True
                            card_logger.clear()
                            break

                
    except KeyboardInterrupt:
        logger.log(logging.CRITICAL, "Game interrupted by player.")

    finally:
        print("Thank You for playing Blackjack.")
        print("Game Over")

main()
