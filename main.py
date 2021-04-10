import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from database import DataBase as DB

bot = telebot.TeleBot('1715413219:AAG-psejdspI_Q1HsXq6nMbhF6H80AQXe7o')
# '1779226494:AAGL57Uum34BXc_aROCwusZDb9Fvf4uDxZw'


mark = InlineKeyboardMarkup(row_width=3)
one = InlineKeyboardButton('1', callback_data=1)
two = InlineKeyboardButton('2', callback_data=2)
tri = InlineKeyboardButton('3', callback_data=3)
cheture = InlineKeyboardButton('4', callback_data=4)
five = InlineKeyboardButton('5', callback_data=5)
mark.add(one, two, tri, cheture, five)

begin = ReplyKeyboardMarkup(resize_keyboard = True)
info = KeyboardButton("Начать")
begin.add(info)


@bot.message_handler(commands=['start', 'help'])
def start(message):
    db = DB()
    try:
        ans = db.getAns(message.chat.id)
        if ans != 0:
            db.setAns(message.chat.id, 0)
    except Exception as e:
        print(e)
    bot.send_message(message.chat.id,
                     f'Привет, {message.from_user.first_name}! Я Рефлексор. Я могу отразить твое настроение. Для '
                     f'этого по возможности пиши мне о своем состоянии. Также в будущем ты сможешь увидеть настроение '
                     f'других, когда создатели сделают Калейдоскоп Душ. Хочешь узнать обо мне больше заходи на сайт: '
                     f'http://reflectmood.tilda.ws/', reply_markup=begin)
    db.setAns(message.chat.id, 0)
    print(message.from_user.first_name)
    db.AddUser(message.from_user.id)


@bot.callback_query_handler(func=lambda c: True)
def keyboard(c):
    db = DB()
    if c.data == '1' or c.data == '2' or c.data == '3' or c.data == '4' or c.data == '5':
        ans = db.getAns(c.message.chat.id)
        a = ans + 1
        bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text='Хорошо. Идем дальше.')
        db.setAns(c.message.chat.id, a)
        db.setMark(c.message.chat.id, c.data)
        messages(c.message)


@bot.message_handler()
def messages(message):
    db = DB()
    db.AddMessage(message.chat.id, message.text)
    ans = db.getAns(message.chat.id)
    a = ans + 1
    db.setAns(message.chat.id, a)
    mes = {
        0: {
            "message": "Давай начнём. Расскажи немного о своём состоянии. Насколько ты устал? 1 - бодр и полон сил, "
                       "5 - готов упасть и лежать.",
            "buttons": True,
            "wait_ans": True
        },
        1: {
            "message": "Понял тебя. А как сильно ты сейчас нуждаешься в моральной поддержке? 1 - у меня всё хорошо, "
                       "5 - мне очень плохо и одиноко.",
            "buttons": True,
            "wait_ans": True
        },
        2: {
            "message": "Хм, ясно. И последний вопрос. Можно ли сказать, что сегодня не твой день? 1 - нет, всё идёт "
                       "отлично, 5 - да, удача обошла меня стороной.",
            "buttons": True,
            "wait_ans": True
        },
        3: {
            "message": "Чтобы я мог лучше понять твоё настроение, опиши своё состояние в нескольких словах",
            "buttons": False,
            "wait_ans": True
        },
        4: {
            "message": "Спасибо за ответы). Пиши снова, когда захочешь. ",
            "buttons": False,
            "wait_ans": True
            },
        5: {
            "message": "Рад, что ты написал. Я ждал тебя. ",
            "buttons": False,
            "wait_ans": True
            }
        }
    if mes[ans]["buttons"]:
        if ans != 0:
            an = ans - 1
        else:
            an = ans
        bot.send_message(message.chat.id, mes[an]["message"], reply_markup=mark)
    else:
        if ans != 0:
            an = ans - 1
        else:
            an = ans
        bot.send_message(message.chat.id, mes[an]["message"])
        ans = db.getAns(message.chat.id)
        a = ans + 1
        db.setAns(message.chat.id, a)
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет. Как дела?')
    if ans == mes[max][0]:
        db.setAns(message.chat.id, 0)
    if message.text != 'Начать':
        db.AddMessage(message.chat.id, message.text)


bot.polling()
