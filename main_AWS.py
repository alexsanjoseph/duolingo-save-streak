
def main(a, b):
    import duolingo, os

    usernames = os.environ['usernames'].split(',')
    passwords = os.environ['passwords'].split(',')

    for username,password in zip(usernames,passwords):
        try:
            lingo = duolingo.Duolingo(username, password)
        except ValueError:
            raise Exception("Username Invalid")

        print("Trying to Buy Streak Freeze for " + username)
        print(lingo.buy_streak_freeze())

        try:
            print("Trying to Buy Double or nothing for " + username)
            lingo.buy_item('rupee_wager', 'en')
        except:
            raise UserWarning("Unable to buy double or nothing")
