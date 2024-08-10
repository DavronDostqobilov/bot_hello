import requests
import os
from pprint import pprint
TOKEN = os.environ['TOKEN'] 

def get_user_profile_photos(user_id: int):
    """
    Get user profile photos

    Args:
        user_id (int): user id

    Returns:
        dict: user profile photos
    """
    URL = f'https://api.telegram.org/bot{TOKEN}/getUserProfilePhotos'
    response = requests.get(URL, params={'user_id': user_id})
    return response.json()


user_id = 1383186462
pprint(get_user_profile_photos(user_id))