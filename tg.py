import telebot
from send import token
from main import result_msg

token = token
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, result_msg)


bot.polling(none_stop=True, interval=0)
