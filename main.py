import telebot
from database import DataBase as DB


bot = telebot.TeleBot('1779226494:AAGL57Uum34BXc_aROCwusZDb9Fvf4uDxZw')
#'1715413219:AAG-psejdspI_Q1HsXq6nMbhF6H80AQXe7o'

@bot.message_handler(commands=['start', 'help'])
def start(message):
    db = DB()
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}! Я Рефлексор. Я могу отразить твое настроение. Для этого по возможности пиши мне о своем состояниию Также в будущем ты сможешь увидеть настроение других, когда создатели сделают Калейдоскоп Душ. Хочешь узнать обо мне больше заходи на сайт: http://reflectmood.tilda.ws/')
    bot.send_message(message.chat.id, 'Расскажи немного о своём состоянии. Насколько ты устал?')
    db.setAns(message.chat.id, '+')
    print(message.from_user.first_name)
    db.AddUser(message.from_user.id)

@bot.message_handler()
def messages(message):
    db = DB()
    db.AddMessage(message.chat.id, message.text)
    db.setAns(message.chat.id, '+')
    ans = db.getAns(message.chat.id)
    if ans == 1:
        bot.send_message(message.chat.id, 'Хорошо. Идем дальше.')
        bot.send_message(message.chat.id, 'Как ты думаешь насколько ты полезен в комманде?')
    if ans == 2:
        bot.send_message(message.chat.id, 'Принято.')
        bot.send_message(message.chat.id, 'Доволен ли ты своей работой? Нравится ли тебе твоя роль?')
    if ans == 3:
        bot.send_message(message.chat.id, 'Спасибо за разговор. Всегда жду, когда напишешь.')

    # if message.chat.id == 1169621316:
    #     for user in db.getAll():
    #         bot.send_message(user, message.text)


bot.polling()