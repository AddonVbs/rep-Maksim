import telebot
from telebot import types
import requests
from Tokenkey import Token_password

TOKEN = Token_password

bot = telebot.TeleBot(TOKEN)

city_name = 'Tomsk'	

def send_wether(city_name):
	response = requests.get(f"https://wttr.in/{city_name}?format=3")
	if response.status_code == 200:
		return response.text
	return None

@bot.message_handler(commands=["start"])
def start (message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	tupe1 = types.KeyboardButton('help')
	tupe2 = types.KeyboardButton('weather')
	markup.add(tupe1,tupe2)

	bot.send_message(message.chat.id, "Здравствуй {0.first_name}, и добро пожаловать ! ".format(message.from_user), reply_markup = markup )

@bot.message_handler(content_types=['text'])
def send_massage_buttons_or_tups(message):
		if message.text == 'help':
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			tupe_help1 = types.KeyboardButton('Кто разробатовал этого Бота ?')
			tupe_help2 = types.KeyboardButton('что этот бот умеет ?')
			back_help = types.KeyboardButton('Вернутся назад ⬅')
		
			markup.add(tupe_help1,tupe_help2,back_help)
			bot.send_message(message.chat.id, "Задайте мне вопрос ?".format(message.from_user), reply_markup = markup )
		if message.text == 'Кто разробатовал этого Бота ?':
			bot.send_message(message.chat.id,'его разробатовал Максим')

		if message.text == 'что этот бот умеет ?':
			bot.send_message(message.chat.id,'пока этот бот особо не чего не умеет')

		elif message.text == 'Вернутся назад ⬅':
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			tupe1 = types.KeyboardButton('help')
			tupe2 = types.KeyboardButton('weather')
		
			markup.add(tupe1,tupe2)
			bot.send_message(message.chat.id, "вы переместились назад".format(message.from_user), reply_markup = markup )
		
		if message.text == 'weather':
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			tupe_wether = types.KeyboardButton('Томск')
			tupe_wether_back = types.KeyboardButton('Вернутся назад')
			
			markup.add(tupe_wether, tupe_wether_back)
			bot.send_message(message.chat.id,"какой город ? ".format(message.from_user), reply_markup = markup)
		if message.text == 'Томск':
			bot.send_message(message.chat.id, send_wether("Tomsk"))
		elif message.text == 'Вернутся назад':
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			tupe1 = types.KeyboardButton('help')
			tupe2 = types.KeyboardButton('weather')
			
			markup.add(tupe1,tupe2)
			bot.send_message(message.chat.id, "вы переместились назад".format(message.from_user), reply_markup = markup )



bot.polling(none_stop=True)
 