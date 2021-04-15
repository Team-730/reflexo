import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from database import DataBase as DB
from analyzer import DostN as NN
import puzzle_generator as pg

<<<<<<< HEAD
bot = telebot.TeleBot('1727515629:AAHc2_h5XxrvRM6QFhdGEVdLtWABn97ZWQ0')
db = DB()
print(db.getMatrix(0))
=======
bot = telebot.TeleBot('1715413219:AAG-psejdspI_Q1HsXq6nMbhF6H80AQXe7o')
>>>>>>> 74f16b784dbacde49e37146cd8f9b2a30418e408

mark = InlineKeyboardMarkup(row_width=3)
one = InlineKeyboardButton('1', callback_data=1)
two = InlineKeyboardButton('2', callback_data=2)
tri = InlineKeyboardButton('3', callback_data=3)
mark.add(one, two, tri)

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
    except Exception as e:
        print(e, 28)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}! Я Рефлексо. Я могу отразить твое '
                                      f'настроение. Для '
                                      f'этого по возможности пиши мне о своем состоянии. Также в будущем ты сможешь '
                                      f'увидеть настроение '
                                      f'других, когда создатели сделают Калейдоскоп Душ. Хочешь узнать обо мне больше '
                                      f'заходи на сайт: '
                                      f'http://reflexo-ai.tilda.ws/page18650718.html', reply_markup=begin)
    db.setAns(message.chat.id, 1)
    # (message.from_user.first_name)
    db.AddUser(message.from_user.id)
    db.AddID(message.chat.id)


@bot.callback_query_handler(func=lambda c: True)
def keyboard(c):
    db = DB()
    if c.data == '1' or c.data == '2' or c.data == '3':
        ans = db.getAns(c.message.chat.id)
        bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text='Хорошо. Идем дальше.')
        db.setAns(c.message.chat.id, ans)
        messages(c.message)
        if ans == 1 or ans == 5:
            db.setParam1(c.message.chat.id, c.data)
        elif ans == 2 or ans == 6:
            db.setParam2(c.message.chat.id, c.data)
        elif ans == 3 or ans == 7:
            db.setParam3(c.message.chat.id, c.data)


@bot.message_handler()
def messages(message):
    db = DB()
    nn = NN()
    db.AddMessage(message.chat.id, message.text)
    ans = db.getAns(message.chat.id)
    a = ans
    b = ans + 1
    db.setAns(message.chat.id, b)
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет. Как дела?')
    mes = {
        0: {
            "message": "Давай начнём. Расскажи немного о своём состоянии. Насколько ты устал? 1 - бодр и полон сил, "
                       "3 - готов упасть и лежать.",
            "buttons": True,
            "wait_ans": True
        },
        1: {
            "message": "Понял тебя. А как сильно ты сейчас нуждаешься в моральной поддержке? 1 - у меня всё хорошо, "
                       "3 - мне очень плохо и одиноко.",
            "buttons": True,
            "wait_ans": True
        },
        2: {
            "message": "Хм, ясно. И последний вопрос. Можно ли сказать, что сегодня не твой день? 1 - нет, всё идёт "
                       "отлично, 3 - да, удача обошла меня стороной.",
            "buttons": True,
            "wait_ans": True
        },
        3: {
            "message": "Чтобы я мог лучше понять твоё настроение, опиши своё состояние в нескольких словах.",
            "buttons": False,
            "wait_ans": True
        },
        4: {
            "message": "Спасибо за ответы). Скоро в 4 холе появится Калейдоскоп душ, где ты сможешь увидеть "
                       "визуализацию настроений всех учасников смены. Пиши снова, когда захочешь.",
            "buttons": False,
            "wait_ans": False
        },
        5: {
            "message": "Как прошло твоё время? Ты доволен собой? 1 - Я доволен собой, 3 - Недовольнее некуда.",
            "buttons": True,
            "wait_ans": True
        },
        6: {
            "message": "Хорошо, следующий вопрос. На сколько ты бодр? 1 - Готов бегать всю ночь, 3 - Коала бодрее.",
            "buttons": True,
            "wait_ans": True
        },
        7: {
            "message": "Окей, подходим к концу. Готов ли ты сейчас поболтать с кем-нибудь. 1 - оставьте меня в покое, "
                       "3 - да, жажду общения.",
            "buttons": True,
            "wait_ans": True
        },
        8: {
            "message": "Опиши пожалуйста своё состояние несколькими словами, это поможет мне точнее определить твоё "
                       "настроение.",
            "buttons": False,
            "wait_ans": True
        },
        9: {
            "message": "Спасибо что написал). Буду ждать следующего диалога с тобой. Скоро в 4 холе появится "
                       "Калейдоскоп душ, где ты сможешь посмотреть визуализацию настроений всех учасников смены.",
            "buttons": False,
            "wait_ans": True
        }
    }
    bot_mes = []
    for merely in mes:
        bot_mes.append(mes[merely]['message'])
    try:
        if message.text != 'Пока':
            if mes[a]["buttons"]:
                bot.send_message(message.chat.id, mes[a]["message"], reply_markup=mark)
            else:
                bot.send_message(message.chat.id, mes[a]["message"])
            if message.text != 'Начать' and message.chat.id == message.from_user.id:
                db.AddMessage(message.chat.id, message.text)
                nn.ready_msg([message.text], message.chat.id)
        else:
            bot.send_message(message.chat.id, 'До новых встреч.')
        if ans == 4 or ans == 9:
            pg()
    except Exception as e:
        print(e, 145)
        db.setAns(message.chat.id, 0)


bot.polling()
