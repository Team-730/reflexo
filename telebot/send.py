import telebot
import time

bot = telebot.TeleBot('1715413219:AAG-psejdspI_Q1HsXq6nMbhF6H80AQXe7o')

for i in range(0, 1000000):
    bot.send_message('1169621316', f'Привет! ')
    #time.sleep(250)

bot.polling()