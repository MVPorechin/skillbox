import telebot

api = "2098098130:AAFD3h8OLFts0lIxasWV-lRrxby-EJBY-0c"
bot = telebot.TeleBot(api)


@bot.message_handler(commands=['start, help'])
def send_welcome(message):
    bot.reply_backend(message, 'Hello world')


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


if __name__ == "__main__":
    bot.infinity_polling()
