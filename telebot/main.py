import telebot
import database as db


bot = telebot.TeleBot('1715413219:AAG-psejdspI_Q1HsXq6nMbhF6H80AQXe7o')
num = 0


@bot.message_handler(commands = ['start', 'help'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}! ')
    print(message.from_user.first_name)
    db.AddUser(message.from_user.id)

@bot.message_handler()
def messages(message):
    db.AddMessage(message.chat.id, message.text)


bot.polling()