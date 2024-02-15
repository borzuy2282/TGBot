import telebot
from telebot import types

print('Here we go')

bot = telebot.TeleBot('6784091371:AAFKg602ndv0ZLs20oPG4gzgrDl7jQicR8g')


def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Україна🇺🇦')
    btn2 = types.KeyboardButton('Polska🇵🇱')
    btn3 = types.KeyboardButton('Deutschland🇩🇪')
    btn4 = types.KeyboardButton('France🇫🇷')
    markup.add(btn1, btn2, btn3, btn4)
    gif = 'gif/dancing-monkeys.mp4'
    with open(gif, 'rb') as gif:
        bot.send_document(message.from_user.id, gif, reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
    menu(message)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Україна🇺🇦':
        markupUA = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Написати боту')
        btn2 = types.KeyboardButton('Написати нубу')
        btn3 = types.KeyboardButton('Написати шнюку')
        btn4 = types.KeyboardButton('Написати блюю')
        btn5 = types.KeyboardButton('Написати вацкі')
        markupUA.add(btn1, btn2, btn3, btn4, btn5)
        gif = 'gif/ukraine-fun.mp4'
        with open(gif, 'rb') as gif:
            bot.send_document(message.from_user.id, gif)
        bot.send_message(message.from_user.id, 'Прошу вибрати шо ви хочете', reply_markup=markupUA)
    elif message.text == 'Polska🇵🇱':
        markupPL = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('napisać botu')
        btn2 = types.KeyboardButton('napisać nubu')
        btn3 = types.KeyboardButton('napisać szniuku')
        btn4 = types.KeyboardButton('napisać bluju')
        btn5 = types.KeyboardButton('napisać wacky')
        markupPL.add(btn1, btn2, btn3, btn4, btn5)
        gif = 'gif/polska.mp4'
        with open(gif, 'rb') as gif:
            bot.send_document(message.from_user.id, gif)
        bot.send_message(message.from_user.id, 'Proszę wybrać co pan chce', reply_markup=markupPL)
    elif message.text == 'Deutschland🇩🇪':
        markupDE = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('schreibe dem Bot')
        btn2 = types.KeyboardButton('schreibe an Noob')
        btn3 = types.KeyboardButton('schreib dem Schnatz')
        btn4 = types.KeyboardButton('schreibe an Blau')
        btn5 = types.KeyboardButton('Schreiben Sie an Vatsky')
        markupDE.add(btn1, btn2, btn3, btn4, btn5)
        gif = 'gif/lenni-schnitzel.mp4'
        with open(gif, 'rb') as gif:
            bot.send_document(message.from_user.id, gif)
        bot.send_message(message.from_user.id, 'Bitte wählen Sie aus, was Sie möchten', reply_markup=markupDE)
    elif message.text == 'France🇫🇷':
        markupFR = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('écrire un bot')
        btn2 = types.KeyboardButton('écrire à noob')
        btn3 = types.KeyboardButton('écrire au vif d\'or')
        btn4 = types.KeyboardButton('écrire pour vomir')
        btn5 = types.KeyboardButton('écrire à Vatsky')
        markupFR.add(btn1, btn2, btn3, btn4, btn5)
        gif = 'gif/france-eiffel-tower.mp4'
        with open(gif, 'rb') as gif:
            bot.send_document(message.from_user.id, gif)
        bot.send_message(message.from_user.id, 's\'il te plaît, choisis ce que tu veux', reply_markup=markupFR)
    # else:
    #     print('refutado 1')
    #     refutado = 'gif/tony-stark-court.mp4'
    #     with open(refutado, 'rb') as refutado:
    #         bot.send_document(message.from_user.id, refutado)
    #     bot.send_message(message.from_user.id, message.from_user.username + ' додік')
    elif message.text == 'Написати боту' or message.text == 'napisać botu' or message.text == 'schreibe dem Bot' or message.text == 'écrire un bot':
        # id bota
        bot.send_message(701101736, "Бот лох\nВід " + message.from_user.username)
        gif = 'gif/bot_govoryt.mp4'
        with open(gif, 'rb') as gif:
            bot.send_document(message.from_user.id, gif)
        bot.send_message(message.from_user.id, 'Delivered')
        menu(message)
    elif message.text == 'Написати нубу' or message.text == 'napisać nubu' or message.text == 'schreibe an Noob' or message.text == 'écrire à noob':
        # id bota(have to be noob)
        bot.send_message(701101736, "Нуб лох\nВід " + message.from_user.username)
        gif = 'gif/nub_vahui.MP4'
        with open(gif, 'rb') as gif:
            bot.send_document(message.from_user.id, gif)
        bot.send_message(message.from_user.id, 'Delivered')
        menu(message)
    elif message.text == 'Написати шнюку' or message.text == 'napisać szniuku' or message.text == 'schreib dem Schnatz' or message.text == 'écrire au vif d\'or':
        # id shnuka
        bot.send_message(542008688, "Шнюк лох\nВід " + message.from_user.username)
        gif = 'gif/shnyuk_loh.mp4'
        with open(gif, 'rb') as gif:
            bot.send_document(message.from_user.id, gif)
        bot.send_message(message.from_user.id, 'Delivered')
        menu(message)
    elif message.text == 'Написати блюю' or message.text == 'napisać bluju' or message.text == 'schreibe an Blau' or message.text == 'écrire pour vomir':
        # id shnuka(have to be bluy)
        bot.send_message(542008688, "Блюй лох\nВід " + message.from_user.username)
        gif = 'gif/bluy_i_bot.MP4'
        with open(gif, 'rb') as gif:
            bot.send_document(message.from_user.id, gif)
        bot.send_message(message.from_user.id, 'Delivered')
        menu(message)
    elif message.text == 'Написати вацкі' or message.text == 'napisać wacky' or message.text == 'Schreiben Sie an Vatsky' or message.text == 'écrire à Vatsky':
        # id shnuka(have to be bluy)
        bot.send_message(542008688, "Вацкі лох\nВід " + message.from_user.username)
        gif = 'gif/vlad_sose.mp4'
        with open(gif, 'rb') as gif:
            bot.send_document(message.from_user.id, gif)
        bot.send_message(message.from_user.id, 'Delivered')
        menu(message)
    else:
        print("refutado 2")
        refutado = 'gif/tony-stark-court.mp4'
        with open(refutado, 'rb') as refutado:
            bot.send_document(message.from_user.id, refutado)
        bot.send_message(message.from_user.id, message.from_user.username + ' додік')
        menu(message)



bot.polling(none_stop=True, interval=0)
