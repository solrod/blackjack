import random
import logging
import sys

##### Logging
logger = logging.getLogger(__name__)
# udskriver kun til konsollen
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

logger.setLevel(logging.DEBUG)
#######


cards = {'Hearts': ['Ace',2,3,4,5,6,7,8,9,10,'J','Q','K'],
        'Diamonds': ['Ace',2,3,4,5,6,7,8,9,10,'J','Q','K'],
        'Spades': ['Ace',2,3,4,5,6,7,8,9,10,'J','Q','K'],
        'Clubs': ['Ace',2,3,4,5,6,7,8,9,10,'J','Q','K']}

# pick a random card
def randomCard():
    logger.log(logging.DEBUG, 'giving random card')
    # random key from cards
    cardType = random.choice(list(cards))
    # random nr card
    cardNumber = random.choice(cards[cardType])
    return cardNumber, cardType
    
    
def main():
    try:
        name = input("Your name: ")
        
        randomCard()

    except logging.exception as err:
        logger.log(logging.CRITICAL, err + 'Fejl opstået')


