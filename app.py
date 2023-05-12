import telebot
import requests
import json

TOKEN = "6042849022:AAEzmCgXh41PfAbc0F62CcEt9lZicVp2y-c"
bot = telebot.TeleBot(TOKEN)

keys = {
    'рубль': 'RUB',
    'евро': 'EUR',
    'доллар': 'USD'
}

class ConvertionException(Exception):
    pass

@bot.message_handler(commands=['start', 'help'])
def repeat(message: telebot.types.Message):
    text = f'Здравствуйте, {message.chat.username}! Я - бот-помощник, помогаю конвертировать указанную вами валюту \
в другую, используя актуальный курс ЦБ РФ на текущую дату.\n' \
           f'Для начала работы введите данные в следующем формате:\n' \
           f' <продаваемая валюта> <покупаемая валюта> <количество продаваемой валюты>.\n' \
           f'Пример ввода: \n' \
           f'доллар рубль 1' \
           f'Нажмите /values чтобы увидеть список доступных валют.'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def repeat(message: telebot.types.Message):
    text = f'Доступные для конвертации валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def get_price(message: telebot.types.Message):
    # доллар рубль 1
    values = message.text.split(' ')
    if len(values) > 3:
        raise ConvertionException('Друг, ты ввел более трех параметров, надо вот так (Пример): доллар рубль 1 ')

    base, quote, amount = values

    r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[base]}&tsyms={keys[quote]}')
    total_quote = json.loads(r.content)[keys[quote]]
    text = f'Цена {amount} {base} в {quote} равна - {total_quote}'
    bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)
