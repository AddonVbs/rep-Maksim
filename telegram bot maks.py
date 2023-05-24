import telebot
from telebot import types
import requests
from tokenKEYmaks import Token_password_2

TOKEN = Token_password_2

bot = telebot.TeleBot(TOKEN)

pikture_puhovik = open('https://media.discordapp.net/attachments/1020254641776246785/1110097341890953216/image.png?width=448&height=676', 'rd')


@bot.message_handler(commands=["start"])
def start (message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	tupe1 = types.KeyboardButton('Мужской ')
	tupe2 = types.KeyboardButton('Женский')
	markup.add(tupe1,tupe2)

	bot.send_message(message.chat.id, "Здравствуй {0.first_name}, выберите ваш пол ! ".format(message.from_user), reply_markup = markup )

@bot.message_handler(content_types=['text'])
def send_massage_buttons_or_tups(message):
		if message.text == 'Мужской':
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			tupe_man1 = types.KeyboardButton('Пуховики')
			tupe_man2 = types.KeyboardButton('Горнолыжные куртки')
			tupe_man3 = types.KeyboardButton('Полукомбинезоны')
			tupe_man4 = types.KeyboardButton('Худи')
			tupe_man5 = types.KeyboardButton('Термобелье')
			tupe_man_back = types.KeyboardButton('вернутся назад')
			markup.add(tupe_man1, tupe_man2, tupe_man3, tupe_man4, tupe_man5, tupe_man_back)
			bot.send_message(message.chat.id, "выберите что вы бы хотели".format(message.from_user), reply_markup = markup )
		if message.text == "Пуховики":
			bot.send_photo(chat_id, pikture_puhovik )