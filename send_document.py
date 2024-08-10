import requests
import os
TOKEN = os.environ['TOKEN'] 
chat_id=1432402481
def send_document(chat_id:int,document:str):


    URL=f'https://api.telegram.org/bot{TOKEN}/sendDocument'
    response=requests.get(URL,params={'chat_id':chat_id},files={'document':document})
    return response.json()

file_path='rasm1.jpg'
document=open(file_path, 'rb').read()
print(send_document(chat_id,document))
