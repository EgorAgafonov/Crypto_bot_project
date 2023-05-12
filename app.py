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
# base_ticker, quote_ticker = keys[base], keys[quote]

class ConvertionException(Exception):
    pass

class CryptoConvertor:
    @staticmethod
    def convert(base: str, quote: str, amount: str):
        if base == quote:
            raise ConvertionException(
                f'Друг, ты конвертируешь одинаковые валюты {quote}. Надо вот так (Пример): доллар рубль 1')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}.')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество валюты {amount}.')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        total_quote = json.loads(r.content)[keys[quote]]

        return total_quote


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = f'Здравствуйте, {message.chat.username}! Я - бот-помощник, помогаю конвертировать указанную вами валюту \
в другую, используя актуальный курс на текущую дату.\n' \
f'Для начала работы введите данные в следующем формате: \n <имя валюты> <в какую валюту перевести> \
<количество продаваемой валюты>. \n Нажмите /values чтобы увидеть список доступных валют.'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = f'Доступные для конвертации валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    values = message.text.split(' ')

    if len(values) != 3:
        raise ConvertionException('Друг, ты ввел более трех параметров, надо вот так (Пример): доллар рубль 1')

    base, quote, amount = values
    total_quote = CryptoConvertor.convert(base, quote, amount)

    text = f'Цена {amount} {base} в {quote} равна - {total_quote}'
    bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)
