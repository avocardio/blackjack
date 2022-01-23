
from re import S
from xmlrpc.client import Boolean
import numpy as np
import time


cards = np.array(['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'])

hand = []
dealer = []

def deal_card():
    return np.random.choice(cards, 1)[0]

def deal_hand():
    return np.random.choice(cards, 2)

def count(hand):
    total = 0
    for card in hand:
        if card == 'A':
            if total > 10:
                total += 1
            elif total < 10:
                total += 11
        elif card in ['J', 'Q', 'K']:
            total += 10
        else:
            total += int(card)    
    return total

def action():
    action = input('Hit (h) or stand (s)?    ')
    if action == 'h':
        return True
    elif action == 's':
        return False
    else:
        print('Invalid input, try again.')
        return action()


print('\n')
print('Welcome to Blackjack!')
print('Press CRTL+C to exit the game')
print('\n')
print('--------------------------')

# While true 

print('\n')
print('Dealer\'s hand:')
dealer_hand = deal_card()
dealer.append(dealer_hand)
print(dealer)
print(count(dealer))
print('\n')
print('Your hand:')
player_hand = deal_hand()
hand.append(player_hand[0])
hand.append(player_hand[1])
print(hand)
print(count(hand))

act = True

print('\n')
if count(hand) == 21:
    print('Blackjack!')
    act == False
else:
    act = action()

time.sleep(1)

while act == True:

    print('\n')
    print('-------')

    if count(hand) > 21:
        print('Bust!')
        break

    if count(hand) < 21:

        print('\n')
        print('Dealer\'s hand:')
        print(dealer)
        print(count(dealer))
        print('\n')
        print('Your hand:')
        hand.append(deal_card())
        print(hand)
        print(count(hand))

        if count(hand) == 21:
            print('Blackjack!')
            time.sleep(1)
            act = False
            break

        if count(hand) > 21:
            time.sleep(1)
            print('Bust!')
            break

        print('\n')
        act = action()
        time.sleep(1)

while act == False:

    print('\n')
    print('-------')

    if count(dealer) < 17:

        print('\n')
        print('Dealer\'s hand:')
        dealer.append(deal_card())
        print(dealer)
        print(count(dealer))
        print('\n')
        print('Your hand:')
        print(hand)
        print(count(hand))
        time.sleep(1)
    
    elif count(dealer) >= 17:
        break

print('\n')
if count(dealer) == count(hand):
    print('Push!')
    print('\n')

if count(dealer) > count(hand) and count(dealer) <= 21:
    print('Dealer wins, sucka!')
    print('\n')
elif count(dealer) > count(hand) and count(dealer) > 21: 
    print('You win!')
    print('\n')

if count(dealer) < count(hand) and count(hand) <= 21:
    if count(hand) == 21:
        print('Win & Blackjack!')
        print('\n')
    else:
        print('You win!')
        print('\n')
elif count(dealer) < count(hand) and count(hand) > 21:
    print('Dealer wins, sucka!')
    print('\n')

