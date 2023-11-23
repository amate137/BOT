import telebot

bot = telebot.TeleBot('6436780166:AAHW9zwJ03YDY_2V6IrxGDCwQ_VaRM_Kjoc')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f"Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>"
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler()
def ingo(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f"Привет {message.from_user.first_name} {message.from_user.last_name} ", parse_mode='html')
@bot.message_handler()
def main(message):
    if message.text == f"Hello":
        bot.send_message(message.chat.id, f"И тебе привет!", parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Твой ID {message.from_user.id}", parse_mode='html')
    elif message.text == "фото":
        photo = open('', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю :/", parse_mode='html')





bot.polling(none_stop=True)23321321
