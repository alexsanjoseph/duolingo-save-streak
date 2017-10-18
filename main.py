
def main():
    import duolingo

    try:
        lingo = duolingo.Duolingo('get')
    except ValueError:
        raise UserWarning("Username Invalid")
        exit()

    lingo = duolingo.Duolingo('akivalam', "@kivalam@duo")
    lingo.get_streak_info()
    lingo.get_vocabulary()

    lingo.buy_streak_freeze()
    print("Trying to Buy Streak Freeze")
    lingo.get_user_info()
