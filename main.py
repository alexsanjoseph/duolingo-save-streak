
def main():
    import duolingo

    try:
        lingo = duolingo.Duolingo('get')
    except ValueError:
        raise UserWarning("Username Invalid")
        exit()

    print("Trying to Buy Streak Freeze")
    lingo.get_streak_info()
