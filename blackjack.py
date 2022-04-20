import random
import logging
import sys
import time

##### Logging
logger = logging.getLogger(__name__)
# udskriver kun til konsollen
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

logger.setLevel(logging.DEBUG)
#######


cards = {'Hearts': ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King'],
        'Diamonds': ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King'],
        'Spades': ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King'],
        'Clubs': ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
        }

# Blackjack combinations
blackjack = {
    1:['Ace', 'Jack'],
    2:['Ace', 'Queen'],
    3:['Ace', 'King'],
    4:['Jack', 'Ace'],
    5:['Queen', 'Ace'],
    6:['King', 'Ace']
}

# logging the cards the player have
card_logger = []

# pick a random card
def randomCard():
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
        if actualPoints <= 7:
            card = 14
        else:
            card = 1
    return card
    



def main():
    humanPlayerStatus = True
    player_point = 0
    dealer_point = 0

    try:
        
        name = "Zeze"
        #name = input("Your name: ")
        print("Here is your first card {}".format(name))
        while True:
            # Human player
            cardNumber, cardType = randomCard()

            # Add card to cardLogger
            card_logger.append(cardNumber)

            if card_logger in blackjack.values():
                print("You have Blackjack...")
                print('Now its dealers turn.')
                player_point = 21
                break

            print("\n {} of {} ".format(str(cardNumber), cardType))
            # Add points to counter
            player_point += card_values(cardNumber, player_point) 

            print("You now have {} points.\n".format(player_point))

            if player_point == 21:
                print("You have blackjack!")
                print('Now its dealers turn.')
                break
 
            if player_point > 21:
                print("You now have more than 21, you loose this game!")
                break

            # Ask if player want one more card
            ask_for_another_card = input('Do you want another card?\n Y or N: ').lower()
            
            if ask_for_another_card == 'y':
                continue
            else:
                print("{} you stopped at {} points.".format(name, player_point))
                print('Now its dealers turn.')
                break

            



    except KeyboardInterrupt:
        logger.log(logging.CRITICAL, "Game interrupted.")
    except logging.exception as err:
        logger.log(logging.CRITICAL, err + 'Fejl opstået')

    finally:
        print("Game Over")

main()
