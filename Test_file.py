import telebot

TOKEN = "6042849022:AAEzmCgXh41PfAbc0F62CcEt9lZicVp2y-c"
bot = telebot.TeleBot(TOKEN)

bot.polling(none_stop=True)

@bot.message_handler(content_types=['voice', ])
def repeat (message: telebot.types.Message):
    bot.send_message(message.chat.id, 'У тебя приятный голос!')

bot.polling(none_stop=True)