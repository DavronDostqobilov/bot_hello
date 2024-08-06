import requests
import os
TOKEN = os.environ['TOKEN'] 
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
# Get updates
response = requests.get(URL)
data = response.json()
result=data['result'][-1]
print(get_text_from_update(result))
