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
    int(environ.get('ID_OF_DIMA')): {
        'language': 'Україна🇺🇦',
        'gif': 'gif/nub_vahui.MP4',
        'message': 'Нуб лох'
    },int(environ.get('ID_OF_DAVID')): {
        'language': 'Україна🇺🇦',
        'gif': 'gif/bluy_i_bot.MP4',
        'message': 'Блюй лох'
    },int(environ.get('ID_OF_VLAD')): {
        'language': 'Україна🇺🇦',
        'gif': 'gif/vlad_sose.mp4',
        'message': 'Вацкі лох'
    },int(environ.get('ID_OF_TYMOFII')): {
        'language': 'Україна🇺🇦',
        'gif': 'gif/bot_govoryt.mp4',
        'message': 'Бот лох'
    },int(environ.get('ID_OF_MAX')): {
        'language': 'Україна🇺🇦',
        'gif': 'gif/Shnyuk_loh.mp4',
        'message': 'Шнюк лох'
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
    USER_STATES[chat_id] = "1"


def send_document_and_menu(chat_id, document, reply_markup):
    with open(document, 'rb') as gif:
        bot.send_document(chat_id, gif)
    USER_STATES[chat_id] = "1"


def start_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Україна🇺🇦')
    btn2 = types.KeyboardButton('Polska🇵🇱')
    btn3 = types.KeyboardButton('Deutschland🇩🇪')
    btn4 = types.KeyboardButton('France🇫🇷')
    markup.add(btn1, btn2, btn3, btn4)
    send_message_and_menu(message.chat.id, 'Here we go', markup)


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
        options = GUYS[user_id]
        options['language'] = language
        USER_STATES[user_id] = "2"
    else:
        send_document_and_menu(user_id, 'gif/tony-stark-court.mp4', None)
        bot.send_message(user_id, message.from_user.username + ' додік')
        start_menu(message)


def sending(message):
    user_id = message.chat.id
    text = message.text.lower()
    recipients = {
        'написати боту': environ.get('ID_OF_TYMOFII'),
        'написати нубу': environ.get('ID_OF_DIMA'),
        'написати шнюку': environ.get('ID_OF_MAX'),
        'написати блюю': environ.get('ID_OF_DAVID'),
        'написати вацкі': environ.get('ID_OF_VLAD'),
    }
    if text in recipients:
        recipient_id = int(recipients[text])
        bot.send_message(recipient_id, f'{text.capitalize()} лох\nВід {message.from_user.username}')
        gif = f'gif/{text.replace(" ", "_").lower()}.MP4'
        send_document_and_menu(user_id, gif, None)
        bot.send_message(user_id, 'Delivered')
        start_menu(message)
    else:
        send_document_and_menu(user_id, 'gif/tony-stark-court.mp4', None)
        bot.send_message(user_id, message.from_user.username + ' додік')
        start_menu(message)


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


bot.polling(none_stop=True, interval=0)
