import telebot
import requests

TOKEN = "6042849022:AAEzmCgXh41PfAbc0F62CcEt9lZicVp2y-c"
bot = telebot.TeleBot(TOKEN)

keys = {
    'рубль': 'RUB',
    'eвро': 'EUR',
    'доллар': 'USD'
}

@bot.message_handler(commands=['start', 'help'])
def repeat(message: telebot.types.Message):
    text = f'Здравствуйте, {message.chat.username}! Я - бот-помощник, помогаю конвертировать указанную вами валюту \
в другую, используя актуальный курс ЦБ РФ на текущую дату.\n' \
           f'Для начала работы введите данные в следующем формате:\n' \
           f' <продаваемая валюта> <покупаемая валюта> <количество продаваемой валюты>.\n' \
           f'Пример ввода:'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def repeat(message: telebot.types.Message):
    text = f'Доступные для конвертации валюты:\n' \
           f'Российский рубль - RUB\n' \
           f'Европейский евро - EUR\n' \
           f'Американский доллар - USD'
    bot.reply_to(message, text)


bot.polling(none_stop=True)
