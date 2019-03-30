from lott import Lott

def getPrice(match, sup):
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

oz_lotto = Lott(7, 2, 1.3, 'Div 7', 50, 45, getPrice)
oz_lotto.playGame()
# oz_lotto.avg_time(100)
