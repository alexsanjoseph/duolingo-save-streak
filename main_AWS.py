def process_single_user(username, password):
    try:
        lingo = duolingo.Duolingo(username, password)
    except ValueError:
        raise Exception("Username Invalid")

    print("Trying to Buy Streak Freeze for " + username)
    if(lingo.buy_streak_freeze()):
        print("Bought streak freeze for " + username)
    else:
        print("Unable to buy streak freeze")

    try:
        print("Trying to Buy Double or nothing for " + username)
        lingo.buy_item('rupee_wager', 'en')
        print("Bought Double or nothing for " + username)
    except:
        print("Unable to buy double or nothing")



def main(a, b):
    import duolingo, os

    usernames = os.environ['usernames'].split(',')
    passwords = os.environ['passwords'].split(',')

    list(map(process_single_user, usernames, passwords))
