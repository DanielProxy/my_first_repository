import requests
import time

api_url = "https://api.telegram.org/bot"
bot_token = "6612349314:AAG4AyN4twS58s6gq7H7o6aN_BaiYYa3Htg"
api_cat = "https://api.thecatapi.com/v1/images/search"
simple_text = 'Конечно круто, а котики ? '
error_text = 'Хочешь картинку котика ? Напиши мне ещё разок'
max_counter = 100

offset = -2
counter = 0
chat_id: int

while counter < max_counter:
    print('attempt = ', counter) #Для просмотра в консоли (? живой ли код ?)
    updates = requests.get(f'{api_url}{bot_token}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset  = result['update_id']
            chat_id = result['message']['from']['id']
            text = result['message']['text']
            cat_responce = requests.get(api_cat)
            if cat_responce.status_code == 200:
                cat_link = cat_responce.json()[0]['url']
                requests.get(f'{api_url}{bot_token}/sendMessage?chat_id={chat_id}&text{text}{simple_text}/sendPhoto?chat_id={chat_id}&photo{cat_link}')
            else:
                requests.get(f'{api_url}{bot_token}/sendMessage?chat_id{chat_id}&text{error_text}')
            # requests.get(f'{api_url}{bot_token}/sendMessage?chat_id={chat_id}&text={text}')

            time.sleep(1)
            counter += 1