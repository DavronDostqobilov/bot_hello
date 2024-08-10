import requests
from sendmessage import send_message
from get_file import speech_to_text
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
    # return update['message']['text']

    next_update_id=0
    chat_id=1432402481
    while True:
        response = requests.get(URL)
        data = response.json()
        result=data['result'][-1]
        first_update_id=result['update_id']
        if first_update_id!=next_update_id:
            text=get_text_from_update(result)
            send_message(chat_id,text)
        next_update_id=result['update_id']
        time.sleep(0.2)

        return update['message']['text'] 

def get_chat_id_from_update(update):
    """
    Get chat id from update

    Args:
        update (dict): update

    Returns:
        int: chat id from update
    """
    return update['message']['chat']['id']




# Get updates
response = requests.get(URL)
print(response.json())
# Get text from update
print(get_text_from_update(response.json()['result'][0]))
# Get chat id from update
print(get_chat_id_from_update(response.json()['result'][0]))

