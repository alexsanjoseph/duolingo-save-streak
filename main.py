def item_already_equipped(lingo, item):
    if item == 'streak_freeze':
        return lingo.__dict__['user_data'].__dict__['tracking_properties']['num_item_streak_freeze']
    if item == 'rupee_wager':
        return lingo.__dict__['user_data'].__dict__['tracking_properties']['has_item_rupee_wager']

def process_single_user(username, password):
    import duolingo
    print(f"Processing {username}")
    try:
        lingo = duolingo.Duolingo(username, password)
    except ValueError:
        raise Exception("Username Invalid")

    stuff_to_purchase = ['streak_freeze', 'rupee_wager']

    for item in stuff_to_purchase:
        if(item_already_equipped(lingo, item)):
            print(f"Item: {item} Already Equipped")
            continue
        try:
            print("Trying to Buy " + item + " for " + username)
            lingo.buy_item(item, 'en')
            print("Bought " + item + " for " + username)
        except duolingo.AlreadyHaveStoreItemException:
            print("Item Already Equipped")
        except Exception:
            raise ValueError("Unable to buy double or nothing")



def main():
    import os

    usernames = os.environ['usernames'].split(',')
    passwords = os.environ['passwords'].split(',')

    list(map(process_single_user, usernames, passwords))


if __name__ == "__main__":
    main()
