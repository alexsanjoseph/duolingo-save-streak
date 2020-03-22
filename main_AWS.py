def process_single_user(username, password):
    import duolingo
    try:
        lingo = duolingo.Duolingo(username, password)
    except ValueError:
        raise Exception("Username Invalid")

    stuff_to_purchase = ['streak_freeze', 'rupee_wager']

    for item in stuff_to_purchase:
        try:
            print("Trying to Buy " + item + " for " + username)
            lingo.buy_item(item, 'en')
            print("Bought " + item + " for " + username)
        except duolingo.AlreadyHaveStoreItemException:
            print("Item Already Equipped")
        except Exception:
            raise ValueError("Unable to buy double or nothing")



def main(a, b):
    import duolingo, os

    usernames = os.environ['usernames'].split(',')
    passwords = os.environ['passwords'].split(',')

    list(map(process_single_user, usernames, passwords))

import yaml
learning_config = yaml.safe_load(open("../learning_config/config.yaml"))
process_single_user(learning_config[0]['username'], learning_config[0]['password'])
