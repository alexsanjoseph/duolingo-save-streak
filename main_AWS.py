def main(a, b):
    import duolingo, os

    usernames = os.environ['usernames'].split(',')
    passwords = os.environ['passwords'].split(',')

    for username,password in zip(usernames,passwords):
        try:
            lingo = duolingo.Duolingo(username, password)
        except ValueError:
            raise UserWarning("Username Invalid")
            exit()

        print("Trying to Buy Streak Freeze for " + username)
        print(lingo.buy_streak_freeze())
