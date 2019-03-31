from lott import Lott

def getPrice(match, sup):
    if match == 8:
        return 'Div 1'
    elif match == 7 and sup > 0:
        return 'Div 2'
    elif match == 7:
        return 'Div 3'
    elif match == 6 and sup > 0:
        return 'Div 4'
    elif match == 6:
        return 'Div 5'
    elif match == 5 and sup > 0:
        return 'Div 6'
    elif match == 5:
        return 'Div 7'
    elif match == 4 and sup > 0:
        return 'Div 8'
    else:
        return 'Lose'

# $8.4 for 2 sets and for 7 days so $0.585 per game, 7 games per week
set_for_life = Lott(8, 2, 0.585, 'Div 2', 50 * 7, 37, getPrice, False)
# set_for_life.playGame()
set_for_life.avg_time(3)
