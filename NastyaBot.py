import requests
import time

api_url = "https://api.telegram.org/bot"
bot_token = "6612349314:AAG4AyN4twS58s6gq7H7o6aN_BaiYYa3Htg"
text = 'Настя котичек '
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
            requests.get(f'{api_url}{bot_token}/sendMessage?chat_id={chat_id}&text={text}')

            time.sleep(1)
            counter += 1

# print(response.text)

# https://api.telegram.org/bot6612349314:AAG4AyN4twS58s6gq7H7o6aN_BaiYYa3Htg/sendMessage?chat_id=889757921&text=%D0%9F%D1%80%D0%B8%D0%B2%D0%B5%D1%82,%20Daniel
# https://api.telegram.org/bot6612349314:AAG4AyN4twS58s6gq7H7o6aN_BaiYYa3Htg/sendMessage?chat_id=655061046&text=%D0%9F%D1%80%D0%B8%D0%B2%D0%B5%D1%82


# https://api.telegram.org/bot<token>sendMessage?chat_id<chat_id>&text=AMAZING