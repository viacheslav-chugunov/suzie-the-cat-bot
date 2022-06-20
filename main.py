from telebot import TeleBot
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton
from utils import *

bot = TeleBot("5542074704:AAGi_awSsh2P6DTHbicr7ZD434l9prbo_00")


@bot.message_handler(commands=["start"], content_types=["text"])
def handle_start_command(message: Message):
    greeting = "Hi there, my name is Anna. This is telegram bot was created for my cat named Suzie 😺. You can speak " \
               "with my kitty and she may send your some great photos of herself 😽. "
    chat_id = message.chat.id
    markup = create_keyboard_workup()
    photo = open('assets/start.jpg', 'rb')
    bot.send_message(chat_id, greeting)
    bot.send_photo(chat_id, photo, reply_markup=markup)


@bot.message_handler(content_types=["text"])
def handle_meow_murr_message(message: Message):
    chat_id = message.chat.id
    markup = create_keyboard_workup()
    text = message.text
    if text == "Photograph":
        photo = get_suzie_photo()
        bot.send_photo(chat_id, photo, reply_markup=markup)
    else:
        phrase = interact_with_suzie(text)
        bot.send_message(chat_id, phrase, reply_markup=markup)


def create_keyboard_workup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    store_button = KeyboardButton("Stroke")
    feed_button = KeyboardButton("Feed")
    play_button = KeyboardButton("Play")
    photograph_button = KeyboardButton("Photograph")
    markup.add(store_button, feed_button, play_button, photograph_button)
    return markup


if __name__ == '__main__':
    bot.polling(none_stop=True)
