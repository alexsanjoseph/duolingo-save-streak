
import duolingo

try:
    lingo = duolingo.Duolingo('alexjoseph398895',  'xelajoseD')
except ValueError:
    raise UserWarning("Username Invalid")
    exit()

print("Trying to Buy Streak Freeze")
lingo.buy_streak_freeze()
lingo.get_streak_info()
