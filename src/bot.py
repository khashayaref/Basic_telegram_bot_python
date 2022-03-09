
import os

import emoji
import telebot
from telebot import apihelper, types

from src.utils.constants import keyboards
from src.utils.io import write_json


class Bot:
    """Telegram bot for connection randomly two strangers to talk
    """
    def __init__(self):
        self.bot = telebot.TeleBot(os.environ.get('NASHENAS_BOT_TOKEN'))
        self.echo_all = self.bot.message_handler(func=lambda message: True)(self.echo_all)
    
    def run(self):
        self.bot.infinity_polling(timeout=40)
        
    def echo_all(self, message):
        print(emoji.demojize(message.text))
        write_json(message.json, 'message.json')
        self.bot.send_message(message.chat.id, message.text,reply_markup=keyboards.main)
        

		 			

if __name__ == '__main__':
	bot = Bot()
	bot.run()
