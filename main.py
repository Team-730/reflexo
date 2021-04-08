import telebot
import database as db


bot = telebot.TeleBot('1715413219:AAG-psejdspI_Q1HsXq6nMbhF6H80AQXe7o')


@bot.message_handler(commands = ['start', 'help'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}! Я бот, созданный чтобы вы могли выразить ваши эмоции и поделиться своими проблемами или успехами.')
    bot.send_message(message.chat.id, 'Напиши о том что ты чувствуешь, или чем бы ты хотел поделиться.')
    print(message.from_user.first_name)
    db.AddUser(message.from_user.id)

@bot.message_handler()
def messages(message):
    if message.chat.id == 1169621316:
        for users in db.getAll():
            user = str(users)
            id = user.replace('(', '')
            id = id.replace(',', '')
            id = id.replace(')', '')
            print(id)
            bot.send_message(id, message.text)
    db.AddMessage(message.chat.id, message.text)


bot.polling()