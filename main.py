import requests
import os
TOKEN = os.environ['TOKEN'] 
URL = f'https://api.telegram.org/bot{TOKEN}/getMe'

# Get bot information
response = requests.get(URL)
print(response.json())
from get_file import speech_to_text,download_file
