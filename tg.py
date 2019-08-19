import telebot
import time
from threading import Thread
import sqlite3
#conn.row_factory = sqlite2.Row
conn = sqlite3. connect('C:/Users/kassi/WebstormProjects/re-prime/mydatabase.db')
cursor = conn.cursor()
sqlite3.connect(":memory:", check_same_thread = False)

token = "961643868:AAGb5APlwnEXo4vh1BFWQr0P99rYojhCXyA"
telebot.apihelper.proxy = {'https': 'socks5h://geek:socks@t.geekclass.ru:7777'}
bot = telebot.TeleBot(token=token)
users = []

@bot.message_handler(commands=['start', 'help'])
def start(message):
    user = message.chat.id
    bot.send_message(user, "Привет," + message.from_user.first_name + "!Этот бот поможет тебе подготовиться к ЕГЭ и просто потренировать свои мозги.Напиши мне /tasks")


@bot.message_handler(commands=['tasks'])
def add_user(message):
    user = message.chat.id
    if user not in users:
        users.append(user)
    bot.send_message(user,"теперь вы будете получать задачи.Это происходит несколько раз за день,ваша цель отвечать на них быстрее других,за это вы будете получать баллы.По нажатию на кнопку Site вы сможете увидеть таблицу лидеров.Первые 3 места получат небольшое вознаграждение в конце смены")
    sql = "SELECT * FROM mydatabase WHERE hardlevel=?"
    cursor.execute(sql, [("2")])
    a = cursor.fetchone()
    bot.send_message(user,a)

@bot.message_handler(commands=['refuse'])
def remove_user(message):
    user = message.chat.id
    users.remove(user)
    bot.send_message(user, "рассылка прекращена")

def spam():
    while True:
        for user in users:
            bot.send_message(user,conn)
        time.sleep(10800)

def polling():
    bot.polling(none_stop=True)

print(users)
polling_thread = Thread(target=polling)
spam_thread = Thread(target=spam)

polling_thread.start()
spam_thread.start()