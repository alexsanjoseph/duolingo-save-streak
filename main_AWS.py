def main(a, b):
    import duolingo, os
    try:
        lingo = duolingo.Duolingo(os.environ['username'], os.environ['password'])
    except ValueError:
        raise UserWarning("Username Invalid")
        exit()

    print("Trying to Buy Streak Freeze")
    print(lingo.buy_streak_freeze())
