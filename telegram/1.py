from telethon import TelegramClient, events, sync, connection

api_id = 25160302 # Тут укажите полученый ранее api
api_hash = '1859dd79b785079f62d03d191dea2ded' # Тут укажите полученый ранее hash

client = TelegramClient('session_name2', api_id, api_hash)
client.start()
print(client.get_me())
client.disconnect()
