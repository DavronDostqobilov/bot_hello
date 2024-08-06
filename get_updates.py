import requests
import os
TOKEN = os.environ['TOKEN'] 
import time
URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'


def get_text_from_update(update):
    """
    Get text from update

    Args:
        update (dict): update

    Returns:
        str: text from update
    """
    return update['message']['text']
# # Get updates
# response = requests.get(URL)
# data = response.json()
# result=data['result'][-1]
# get_text_from_update(result)

next_update_id=0
while True:
    response = requests.get(URL)
    data = response.json()
    result=data['result'][-1]
    first_update_id=result['update_id']
    if first_update_id!=next_update_id:
        print(get_text_from_update(result))
    next_update_id=result['update_id']
    time.sleep(0.5)
