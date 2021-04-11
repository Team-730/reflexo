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

begin = ReplyKeyboardMarkup(resize_keyboard=True)
info = KeyboardButton("Начать")
begin.add(info)


@bot.message_handler(commands=['start', 'help'])
def start(message):
    db = DB()
    try:
        ans = db.getAns(message.chat.id)
        if ans != 0:
            db.setAns(message.chat.id, 0)
    except:
        pass
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}! Я Рефлексо. Я могу отразить твое '
                                      f'настроение. Для '
                                      f'этого по возможности пиши мне о своем состоянии. Также в будущем ты сможешь '
                                      f'увидеть настроение '
                                      f'других, когда создатели сделают Калейдоскоп Душ. Хочешь узнать обо мне больше '
                                      f'заходи на сайт: '
                                      f'http://reflexo-ai.tilda.ws/page18650718.html', reply_markup=begin)
    db.setAns(message.chat.id, 0)
    # (message.from_user.first_name)
    db.AddUser(message.from_user.id)


@bot.callback_query_handler(func=lambda c: True)
def keyboard(c):
    db = DB()
    if c.data == '1' or c.data == '2' or c.data == '3' or c.data == '4' or c.data == '5':
        ans = db.getAns(c.message.chat.id)
        a = ans
        bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text='Хорошо. Идем дальше.')
        db.setAns(c.message.chat.id, a)
        db.setMark(c.message.chat.id, c.data)
        messages(c.message)


@bot.message_handler()
def messages(message):
    db = DB()
    db.AddMessage(message.chat.id, message.text)
    ans = db.getAns(message.chat.id)
    a = ans
    b = ans + 1
    db.setAns(message.chat.id, b)
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Рад, что ты написал. Я ждал тебя.')
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
            "message": "Чтобы я мог лучше понять твоё настроение, опиши своё состояние в нескольких словах.",
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
            "wait_ans": False
        },
        6: {
            "message": "Как прошло твоё время? Ты доволен собой? 1 - Я доволен собой, 5 - Недовольнее некуда.",
            "buttons": True,
            "wait_ans": True
        },
        7: {
            "message": "Хорошо, следующий вопрос. На сколько ты бодр? 1 - Готов бегать всю ночь, 5 - Коала бодрее.",
            "buttons": True,
            "wait_ans": True
        },
        8: {
            "message": "Окей, подходим к концу. Готов ли ты сейчас поболтать с кем-нибудь. 1 - оставьте меня в покое, "
                       "5 - да, жажду общения.",
            "buttons": True,
            "wait_ans": True
        },
        9: {
            "message": "Опиши пожалуйста своё состояние несколькими словами, это поможет мне точнее определить твоё "
                       "настроение.",
            "buttons": False,
            "wait_ans": True
        },
        10: {
            "message": "Спасибо что написал). Буду ждать следующего диалога с тобой.",
            "buttons": False,
            "wait_ans": True
        }
    }
    try:
        if message.text != 'Пока':
            if mes[a]["buttons"]:
                bot.send_message(message.chat.id, mes[a]["message"], reply_markup=mark)
            else:
                bot.send_message(message.chat.id, mes[a]["message"])
                ans = db.getAns(message.chat.id)
                a = ans + 1
                db.setAns(message.chat.id, a)
            if message.text == 'Привет':
                bot.send_message(message.chat.id, 'Привет. Как дела?')

            f = 0
            for el in mes:
                print(el)
                if message.text != 'Начать' and message.text != el and f == 0:
                    db.AddMessage(message.chat.id, message.text)
                    f = 1
        else:
            bot.send_message(message.chat.id, 'До новых встреч.')
    except:
        db.setAns(message.chat.id, 0)


bot.polling()
