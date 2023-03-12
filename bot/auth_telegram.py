from telethon import TelegramClient
from telethon import functions

#function to login in tg account
def  __auth():
    api_id = 123456789 # Replace this with your own api_id
    api_hash = '' # Replace this with your own api_hash
    phone = '' # Your phone number goes here with the area code and +
    client = TelegramClient(phone, api_id, api_hash)
    #connection with your telegram user
    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phone)
        client.sign_in(phone, input('Enter the code: ')) 
    return client

#function to send message from bot
def __core_to_send_message(client, receiver, msg):
    client((functions.messages.SendMessageRequest(
        peer=receiver,
        message=msg,
        silent=False,
    )))
    

