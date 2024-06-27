import requests
import time
import random


# def slovarnik():
#     slovarik = ['Ещё нада ?', "Что ещё одну ?", "Всё ещё интересно смотреть ?", "Что дальше как думаешь собачка или кошечка ?", "Ну что, может хватит ?", "Снова и снова.... и снова ?", "Картинок там ещё дохуя, показать ?"]
#     return print(slovarik[random.randint(0,6)])

api_url = "https://api.telegram.org/bot"
bot_token = "6612349314:AAG4AyN4twS58s6gq7H7o6aN_BaiYYa3Htg"
api_cat = "https://api.thecatapi.com/v1/images/search"
api_dog = "https://random.dog/woof.json"
simple_text = 'конечно круто, а котики ? '
error_text = 'Хочешь картинку котика ? Напиши мне ещё разок'
max_counter = 100

offset = -2
counter = 0
chat_id: int
dog_responce: requests.Response
cat_responce: requests.Response
cat_link:str

while counter < max_counter:
    print('attempt = ', counter) #Для просмотра в консоли (? живой ли код ?)
    updates = requests.get(f'{api_url}{bot_token}/getUpdates?offset={offset + 1}').json()
    slovarik = ['Ещё нада ?', "Что ещё одну ?", "Всё ещё интересно смотреть ?", "Что дальше как думаешь собачка или кошечка ?", "Ну что, может хватит ?", "Снова и снова.... и снова ?", "Картинок там ещё дохуя, показать ?"]
    if updates['result']:
        for result in updates['result']:
            offset  = result['update_id']
            chat_id = result['message']['from']['id']
            text = result['message']['text']
            cat_responce = requests.get(api_cat)
            dog_responce = requests.get(api_dog)
            rand_num = random.randint(-10,10)
            if rand_num > 0:
                if dog_responce.status_code == 200:
                    dog_link = dog_responce.json()['url']
                    # requests.get(f'{api_url}{bot_token}/sendMessage?chat_id={chat_id}&text={slovarnik}')
                    requests.get(f'{api_url}{bot_token}/sendPhoto?chat_id={chat_id}&photo={dog_link}')
                    requests.get(f'{api_url}{bot_token}/sendMessage?chat_id={chat_id}&text={slovarik[random.randint(0,6)]}')
            elif rand_num<=0:
                if cat_responce.status_code == 200:
                    cat_link = cat_responce.json()[0]['url']
                    # requests.get(f'{api_url}{bot_token}/sendMessage?chat_id={chat_id}&text="{text} "{simple_text}')
                    requests.get(f'{api_url}{bot_token}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
                    requests.get(f'{api_url}{bot_token}/sendMessage?chat_id={chat_id}&text={slovarik[random.randint(0,6)]}')
            else:
                requests.get(f'{api_url}{bot_token}/sendMessage?chat_id{chat_id}&text{error_text}')
            # requests.get(f'{api_url}{bot_token}/sendMessage?chat_id={chat_id}&text={text}')

            time.sleep(1)
            counter += 1

