import telebot
from telebot import types
from dotenv import load_dotenv
from os import environ

load_dotenv()

bot = telebot.TeleBot(environ.get('BOT_ID'))

# Constants
USER_STATES = {
    int(environ.get('ID_OF_DIMA')): "0",
    int(environ.get('ID_OF_DAVID')): "0",
    int(environ.get('ID_OF_VLAD')): "0",
    int(environ.get('ID_OF_TYMOFII')): "0",
    int(environ.get('ID_OF_MAX')): "0"
}

GUYS = {
    environ.get('ID_OF_DIMA'): {
        'gif': 'gif/nub_vahui.MP4',
        'message': 'Нуб лох',
        'options': ['написати нубу', 'napisać nubu', 'schreibe an Noob', 'écrire à noob']
    }, environ.get('ID_OF_DAVID'): {
        'gif': 'gif/bluy_i_bot.MP4',
        'message': 'Блюй лох',
        'options': ['написати блюю', 'napisać bluju', 'schreibe an Blau', 'écrire pour vomir']
    }, environ.get('ID_OF_VLAD'): {
        'gif': 'gif/vlad_sose.mp4',
        'message': 'Вацкі лох',
        'options': ['написати вацкі', 'napisać wacky', 'Schreiben Sie an Vatsky', 'écrire à Vatsky']
    }, environ.get('ID_OF_TYMOFII'): {
        'gif': 'gif/bot_govoryt.mp4',
        'message': 'Бот лох',
        'options': ['написати боту', 'napisać botu', 'schreibe dem Bot', 'écrire un bot']
    }, environ.get('ID_OF_MAX'): {
        'gif': 'gif/Shnyuk_loh.mp4',
        'message': 'Шнюк лох',
        'options': ['написати шнюку', 'napisać szniuku', 'schreib dem Schnatz', 'écrire au vif d\'or']
    },
}

LANGUAGES = {
    'Україна🇺🇦': {
        'keyboard': ['написати боту', 'написати нубу', 'написати шнюку', 'написати блюю', 'написати вацкі'],
        'gif': 'gif/ukraine-fun.mp4',
        'message': 'Прошу вибрати шо ви хочете'
    },
    'Polska🇵🇱': {
        'keyboard': ['napisać botu', 'napisać nubu', 'napisać szniuku', 'napisać bluju', 'napisać wacky'],
        'gif': 'gif/polska.mp4',
        'message': 'Proszę wybrać co pan chce'
    },
    'Deutschland🇩🇪': {
        'keyboard': ['schreibe dem Bot', 'schreibe an Noob', 'schreib dem Schnatz', 'schreibe an Blau',
                     'Schreiben Sie an Vatsky'],
        'gif': 'gif/lenni-schnitzel.mp4',
        'message': 'Bitte wählen Sie aus, was Sie möchten'
    },
    'France🇫🇷': {
        'keyboard': ['écrire un bot', 'écrire à noob', 'écrire au vif d\'or', 'écrire pour vomir', 'écrire à Vatsky'],
        'gif': 'gif/france-eiffel-tower.mp4',
        'message': 's\'il te plaît, choisis ce que tu veux'
    }
}


# Functions
def send_message_and_menu(chat_id, text, reply_markup):
    bot.send_message(chat_id, text, reply_markup=reply_markup)


def send_document_and_menu(chat_id, document, reply_markup):
    with open(document, 'rb') as gif:
        bot.send_document(chat_id, gif, reply_markup=reply_markup)


def start_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Україна🇺🇦')
    btn2 = types.KeyboardButton('Polska🇵🇱')
    btn3 = types.KeyboardButton('Deutschland🇩🇪')
    btn4 = types.KeyboardButton('France🇫🇷')
    markup.add(btn1, btn2, btn3, btn4)
    send_document_and_menu(message.chat.id, 'gif/dancing-monkeys.mp4', markup)
    USER_STATES[message.chat.id] = '1'


def language_selection(message):
    user_id = message.chat.id
    language = message.text
    if language in LANGUAGES:
        options = LANGUAGES[language]
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for option in options['keyboard']:
            markup.add(types.KeyboardButton(option))
        send_document_and_menu(user_id, options['gif'], markup)
        send_message_and_menu(user_id, options['message'], markup)
        USER_STATES[user_id] = "2"
    else:
        send_document_and_menu(user_id, 'gif/tony-stark-court.mp4', None)
        bot.send_message(user_id, message.from_user.username + ' додік')
        start_menu(message)


def sending(message):
    user_id = message.chat.id
    text = message.text
    if_sent = False
    for guy in GUYS:
        if text in GUYS[guy]['options']:
            options = GUYS[guy]
            recipient_id = int(guy)
            ready_message = options['message']
            bot.send_message(recipient_id, f'{ready_message}\nВід {message.from_user.username}')
            gif = options['gif']
            send_document_and_menu(user_id, gif, None)
            bot.send_message(user_id, 'Delivered')
            if_sent = True
            start_menu(message)
            break
    if not if_sent:
        send_document_and_menu(user_id, 'gif/tony-stark-court.mp4', None)
        bot.send_message(user_id, message.from_user.username + ' додік')
        start_menu(message)


print('Here we go')


# Handlers
@bot.message_handler(commands=['start'])
def handle_start(message):
    start_menu(message)


@bot.message_handler(content_types=['text'])
def handle_text_messages(message):
    user_id = message.chat.id
    if USER_STATES[user_id] == "1":
        language_selection(message)
    elif USER_STATES[user_id] == "2":
        sending(message)
    else:
        start_menu(message)


@bot.message_handler(content_types=['photo', 'sticker', 'voice', 'video', 'animation', 'video_note', 'audio'])
def handle_other_messages(message):
    bot.reply_to(message, 'даун?')
    start_menu(message)


bot.polling(none_stop=True, interval=0)
