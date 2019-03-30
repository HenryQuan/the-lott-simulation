import random
import time

class Lott:
    def __init__(self, num, sup, price, div, game_per_week, game_range, price_condition_func):
        self.price = price
        self.div = div
        self.game_per_week = game_per_week
        self.game = list(range(1, game_range + 1))
        self.price_func = price_condition_func

        # get winning ticket
        self.winning = self.getTicket(num + sup)
        print('The winning ticket is {}.'.format(self.winning))

        # get number and supplementary
        self.numberList = self.winning[:num]
        self.supList = self.winning[-sup:]

    # return a list of 'num' random numbers from 1 to range
    def getTicket(self, num):
        return random.sample(self.game, num)

    def matching(self, curr, numlist):
        match = 0
        for w in numlist:
            for c in curr:
                if c == w:
                    match += 1
        return match

    def getPrice(self, curr):
        match = self.matching(curr, self.numberList)
        sup = self.matching(curr, self.supList)
        return self.price_func(match, sup)

    # keep playing until you win
    def playGame(self):
        game = 0

        while True:
            curr = self.getTicket(7)
            game += 1

            print('Game #{} (${}) - {}      '.format(game, int(game * self.price), curr), end='')
            print('\r', end='')

            reward = self.getPrice(curr)
            if reward == self.div:
                break

        print('\n\nTo get {} price, you need to play {} games and that costs ${}.'.format(reward, game, int(game * self.price)))
        print('It will take {:.2f} year(s) if you play {} game(s) per week.\n'.format(game / 52 / self.game_per_week, self.game_per_week))
