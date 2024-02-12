import telebot
from telebot import types

bot = telebot.TeleBot('6784091371:AAFKg602ndv0ZLs20oPG4gzgrDl7jQicR8g')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Deutschland')
    markup.add(btn1)
    gif = 'gif/lenni-schnitzel.mp4'
    bot.send_message(message.from_user.id, gif, reply_markup=markup)
bot.polling(none_stop=True, interval=0)