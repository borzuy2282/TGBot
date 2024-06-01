import pytest
from unittest.mock import MagicMock, patch
from telebot import types
from os import environ
from main import bot, handle_start, handle_text_messages, handle_other_messages, USER_STATES

TEST_USER_ID = 12345

@pytest.fixture
def mock_bot(mocker):
    mocker.patch('telebot.TeleBot.send_message')
    mocker.patch('telebot.TeleBot.send_document')
    mocker.patch('telebot.TeleBot.reply_to')  # Mock reply_to method
    return bot

@pytest.fixture
def mock_message():
    message = MagicMock()
    message.chat.id = TEST_USER_ID
    message.from_user.username = 'test_user'
    message.content_type = 'text'  # Set default content type
    return message

@pytest.fixture(autouse=True)
def setup_user_states():
    USER_STATES[TEST_USER_ID] = "0"
    yield
    USER_STATES.pop(TEST_USER_ID, None)

# Mock open to prevent FileNotFoundError
@patch("builtins.open", new_callable=MagicMock)
def test_handle_start(mock_open, mock_bot, mock_message):
    handle_start(mock_message)
    assert USER_STATES[mock_message.chat.id] == '1'
    mock_bot.send_document.assert_called()
    mock_bot.send_message.assert_not_called()  # send_message is not called directly in handle_start

@patch("builtins.open", new_callable=MagicMock)
def test_language_selection(mock_open, mock_bot, mock_message):
    mock_message.text = 'Україна🇺🇦'
    USER_STATES[mock_message.chat.id] = '1'
    handle_text_messages(mock_message)
    assert USER_STATES[mock_message.chat.id] == '2'
    mock_bot.send_document.assert_called()
    mock_bot.send_message.assert_called()

@patch("builtins.open", new_callable=MagicMock)
def test_sending_valid_option(mock_open, mock_bot, mock_message):
    mock_message.text = 'написати нубу'
    USER_STATES[mock_message.chat.id] = '2'
    handle_text_messages(mock_message)
    mock_bot.send_message.assert_any_call(int(environ.get('ID_OF_DIMA')), 'Нуб лох\nВід test_user')
    mock_bot.send_document.assert_called()
    assert USER_STATES[mock_message.chat.id] == '1'

@patch("builtins.open", new_callable=MagicMock)
def test_sending_invalid_option(mock_open, mock_bot, mock_message):
    mock_message.text = 'invalid option'
    USER_STATES[mock_message.chat.id] = '2'
    handle_text_messages(mock_message)
    mock_bot.send_document.assert_called()
    mock_bot.send_message.assert_any_call(mock_message.chat.id, 'test_user додік')
    assert USER_STATES[mock_message.chat.id] == '1'

@patch("builtins.open", new_callable=MagicMock)
def test_handle_other_messages(mock_open, mock_bot, mock_message):
    mock_message.content_type = 'photo'
    handle_other_messages(mock_message)
    mock_bot.reply_to.assert_called_with(mock_message, 'даун?')  # Ensure reply_to is called with the correct message
    mock_bot.send_document.assert_called()
