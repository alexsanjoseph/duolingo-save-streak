
def main():
    import duolingo, os
    try:
        # lingo = duolingo.Duolingo(os.environ['username'], os.environ['password'])
        lingo = duolingo.Duolingo('akivalam', '@kivalam@duo')
    except ValueError:
        raise UserWarning("Username Invalid")
        exit()

    print("Trying to Buy Streak Freeze")
    lingo.buy_streak_freeze()

main()
