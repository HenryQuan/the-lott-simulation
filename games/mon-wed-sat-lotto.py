from lott import Lott

def getPrice(match, sup):
    if match == 6:
        return 'Div 1'
    elif match == 5 and sup > 0:
        return 'Div 2'
    elif match == 5:
        return 'Div 3'
    elif match == 4:
        return 'Div 4'
    elif match == 3 and sup > 0:
        return 'Div 5'
    elif (match == 2 or match == 1) and sup > 1:
        return 'Div 6'
    else:
        return 'Lose'

mon_wed_sat_lotto = Lott(6, 2, 0.715, 'Div 2', 50, 45, getPrice)
mon_wed_sat_lotto.playGame()
# mon_wed_sat_lotto.avg_time(100)
