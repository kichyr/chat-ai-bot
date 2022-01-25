import telebot

bot = telebot.TeleBot("5034819401:AAHzsNRyXh_DJBw-s6je8yP692My4l-dMeI")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, message.chat.id)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(message.chat.id)

bot.infinity_polling()