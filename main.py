import telebot
from telebot import types

print('Here we go')

bot = telebot.TeleBot('6784091371:AAFKg602ndv0ZLs20oPG4gzgrDl7jQicR8g')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Deutschland')
    markup.add(btn1)
    gif = 'gif/lenni-schnitzel.mp4'
    with open(gif, 'rb') as gif:
        bot.send_document(message.from_user.id, gif, reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(message.from_user.id, message.from_user.username)
    if message.text == 'Deutschland':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Написати боту')
        btn2 = types.KeyboardButton('Написати нубу')
        btn3 = types.KeyboardButton('Написати шнюку')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, 'Прошу вибрати шо ви хочете', reply_markup=markup)
    elif message.text == 'Написати боту':
        bot.send_message(701101736, "Бот лох")
    elif message.text == 'Написати нубу':
        bot.send_message(701101736, "Нуб лох")
    elif message.text == 'Написати шнюку':
        bot.send_message(701101736, "Шнюк лох")
    else:
        bot.send_message(message.from_user.id, message.from_user.username + ' додік')
bot.polling(none_stop=True, interval=0)