import requests
import os
from pprint import pprint
TOKEN = os.environ['TOKEN'] 

def send_contact(chat_id: int, phone_number: str, first_name: str, last_name: str):
    """
    Send contact

    Args:
        chat_id (int): chat id
        phone_number (str): phone number
        first_name (str): first name
    """
    URL = f'https://api.telegram.org/bot{TOKEN}/sendContact'
    response = requests.get(URL, params={'chat_id': chat_id, 'phone_number': phone_number, 'first_name': first_name, 'last_name': last_name})
    return response.json()


chat_id = 86775091
phone_number = '+123456789'
first_name = 'Zarif'
last_name = 'Naxalov'


pprint(send_contact(chat_id, phone_number, first_name, last_name))