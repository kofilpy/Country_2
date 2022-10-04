import telebot
from pycountry import countries
from geopy.geocoders import Nominatim
from deep_translator import GoogleTranslator

bot = telebot.TeleBot('5444646569:AAEtwS00Vsnxvb96RicQm8NdGb7c-JP3w0s')


@bot.message_handler(commands=['start'])
def start(message: telebot.types.ChatMemberUpdated):
    mess = f"Привіт, <b>{message.from_user.username}</b>"
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_user_text(message: telebot.types.ChatMemberUpdated):
    translated_message = GoogleTranslator(source='auto', target='en').translate(message.text)
    if countries.get(name=f"{translated_message}")\
            or countries.get(official_name=f"{translated_message}")\
            or countries.get(alpha_3=f"{translated_message}") \
            is not None:
        bot.send_message(message.chat.id,
                         f"https://www.google.com/maps/place/{translated_message}",
                         parse_mode='html')
    else:
        bot.send_message(message.chat.id,
                         f"{message.text} - невірна назва країни",
                         parse_mode='html')


# @bot.message_handler(content_types=['text'])
# def get_user_text(message: telebot.types.ChatMemberUpdated):
#     if message.text == "Hello":
#         bot.send_message(message.chat.id, "Привіт", parse_mode='html')
#     elif message.text == "id":
#         bot.send_message(message.chat.id, f"id - {message.from_user.id}", parse_mode='html')
#     elif message.text == "photo":
#         photo = open("logo.png", 'rb')
#         bot.send_photo(message.chat.id, photo)
#     elif message.text == "location":
#         bot.send_location(message.chat.id, 39.7837304, -100.445882)
#     else:
#         bot.send_message(message.chat.id, f"I don't understand you", parse_mode='html')


# @bot.message_handler(content_types=['photo'])
# def get_user_photo(message: telebot.types.ChatMemberUpdated):
#     bot.send_message(message.chat.id, f"{message.from_user.username}, nice photo")
#
#
# @bot.message_handler(commands=['website'])
# def website(message: telebot.types.ChatMemberUpdated):
#     markup = telebot.types.InlineKeyboardMarkup()
#     markup.add(telebot.types.InlineKeyboardButton("Відвідати сайт", url="https://www.google.com"))
#     bot.send_message(message.chat.id, "Sait", reply_markup=markup)
#
#
# @bot.message_handler(commands=['help'])
# def website(message: telebot.types.ChatMemberUpdated):
#     markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#     website = telebot.types.KeyboardButton("Веб сайт")
#     start = telebot.types.KeyboardButton("Start")
#     markup.add(website, start)
#     bot.send_message(message.chat.id, "Sait", reply_markup=markup)


bot.polling(none_stop=True)
