import os
import requests

def process_single_user(id: str, jwt: str):

    userAgent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

    with requests.Session() as session:
        print(f"Processing id {id}.")

        # Get User Data
        url = f"https://www.duolingo.com/2017-06-30/users/{id}?fields=learningLanguage,trackingProperties,username"
        headers = {'Authorization': f"Bearer {jwt}", 'User-Agent': userAgent}
        response = session.get(url, headers=headers)
        response.raise_for_status()

        user_data = response.json()
        username = user_data['username']
        learning_language = user_data['learningLanguage']
        has_item_rupee_wager = user_data['trackingProperties']['has_item_rupee_wager']
        num_item_streak_freeze = user_data['trackingProperties']['num_item_streak_freeze']

        print(f"User: {username}")

        if learning_language is None:
            print('No learning language assigned.')
        else:
            # Go shopping
            url = f"https://www.duolingo.com/2017-06-30/users/{id}/shop-items"

            for item in ['streak_freeze', 'rupee_wager']:
                if item == 'rupee_wager':
                    if has_item_rupee_wager:
                        num_item = 1
                    else:
                        num_item = 0
                    max_item = 1
                elif item == 'streak_freeze':
                    num_item = num_item_streak_freeze
                    max_item = 2
                else:
                    continue

                if num_item >= max_item:
                    print(f"Item {item} is fully equipped.")
                else:
                    print(f"Item {item} has {num_item} of {max_item} equipped.")

                while num_item < max_item:
                    jsonData={'itemName': item, 'learningLanguage': learning_language}
                    response = session.post(url,headers=headers,json=jsonData)
                    response.raise_for_status()

                    shop_data = response.json()
                    print(f"Purchased {item} for {shop_data['purchasePrice']} lingots.")
                    num_item += 1

def lambda_handler(event, context):
    ids = os.environ['ids'].split(',')
    jwts = os.environ['jwts'].split(',')
    list(map(process_single_user, ids, jwts))
