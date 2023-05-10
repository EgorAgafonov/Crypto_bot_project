import telebot

# TOKEN = "6042849022:AAEzmCgXh41PfAbc0F62CcEt9lZicVp2y-c"
# bot = telebot.TeleBot(TOKEN)
#
#
# @bot.message_handler(content_types=['voice', ])
# def repeat(message: telebot.types.Message):
#     bot.send_message(message.chat.id, 'У тебя приятный голос!')
#
# @bot.message_handler(content_types=['text', ])
# def repeat(message: telebot.types.Message):
#     bot.send_message(message.chat.id, 'Рад тебя слышать, дружище!')
#
# bot.polling(none_stop=True)


TOKEN = "6042849022:AAEzmCgXh41PfAbc0F62CcEt9lZicVp2y-c"
bot = telebot.TeleBot(TOKEN)

# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def repeat(message: telebot.types.Message):
    print(message.text)
    bot.reply_to(message, f"Привет, дорогой {message.chat.username}")

# Обрабатываются все документы и аудиозаписи
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    bot.send_message(message.chat.id, f"Отличный трек, {message.chat.username}, мне нравится!")

@bot.message_handler(content_types=['photo'])
def reply_to_photo(message: telebot.types.Message):
    bot.reply_to(message, f"Отличная картинка, {message.chat.username}, мне нравится!")

bot.polling(none_stop=True)
