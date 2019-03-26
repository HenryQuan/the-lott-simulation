# There are forty-five balls numbered 1 to 45 from which seven winning numbers are randomly selected.
import random
import time

PRICE = 1.3
# It will take some time starting from Div 5
# Div 1 probably takes forever... (Don't blame me if you lost 70 million)
DIVISION = 'Div 1'
GAME_PER_WEEK = 50
GAME = list(range(1, 46))

# return a list of 'num' random numbers from 1 to 45
def getTicket(num):
    return random.sample(GAME, num)

def matching(curr, winning):
    match = 0
    for w in winning:
        for c in curr:
            if c == w:
                match += 1
    return match

def getPrice(curr, winning):
    match = matching(curr, winning[:7])
    sup = matching(curr, winning[-2:])
    if match == 7:
        return 'Div 1'
    elif match == 6 and sup > 0:
        return 'Div 2'
    elif match == 6:
        return 'Div 3'
    elif match == 5 and sup > 0:
        return 'Div 4'
    elif match == 5:
        return 'Div 5'
    elif match == 4:
        return 'Div 6'
    elif match == 3 and sup > 0:
        return 'Div 7'
    else:
        return 'Lose'

# keep playing until you win
def playGame(winning):
    game = 0

    while True:
        curr = getTicket(7)
        game += 1

        print('Game #{} (${}) - {}      '.format(game, int(game * PRICE), curr), end='')
        print('\r', end='')

        reward = getPrice(curr, winning)
        if reward == DIVISION:
            break

    print('\n\nTo get {} price, you need to play {} games and that costs ${}.'.format(reward, game, int(game * PRICE)))
    print('It will take {:.2f} year(s) if you play {} game(s) per week.\n'.format(game / 52 / GAME_PER_WEEK, GAME_PER_WEEK))

# winning ticket
winning = getTicket(9)
print('The winning ticket is {}.'.format(winning))

# It is nearly impossible to get Div 1 price but it is not impossible
playGame(winning)
