import telebot as tb
from telebot import types
import random as rd
import time
# import datetime as dt
import logging
import sqlite3

# Сценарии
priv = ['Добрый день, товарищ', 'Приветствую вас', 'Здравтсуйте, друг мой', 'День добрый', 'Хэллоу']
net = ['Извините, отказано', 'Ответ системы - "Нет"', 'Товарищ, отказано']
da = ['Статус - "ДА', 'Естествено', 'TRUE (Da)']
bot_pohval = ['Лучший помощник', 'JARVIS только лучше', 'Супер мега пупер помощник', 'Танос среди помщников в мире']
fakt = [['Интересный факт: Первый человек в космоесу был из СССР', 'Факт про космос'],
        ['В начале у тебя 20 кирок', 'Факт про майнкрафт']]

# Токен бота
token = '6282629918:AAGxRTkieARpHeQyliDtn4y0k2UHr8Wh4wE'
bot = tb.TeleBot(token)

# Уведомление о запуске
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


# Факт
def fak(message):
    if 1 == rd.randint(0, 5):
        bot.send_message(message.chat.id, f'{fakt[rd.randint(0, 1)][1]}. Хотите узнать?')


# Подтверждение о готовности
@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = types.KeyboardButton('Да')
    b2 = types.KeyboardButton('Нет')
    b4 = types.KeyboardButton('Почему такое название бота?')
    b3 = types.KeyboardButton('Сайт - для регистрации.')
    keyboard.add(b1, b2, b3, b4)
    bot.send_message(message.chat.id, f'{priv[rd.randint(0, 4)]}. Вы готовы к общению?', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def keyboard_gotov(message):
    global bn1, bn2, bn3
    if message.text == 'Сайт - для регистрации.':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b2 = types.KeyboardButton('Назад в ад')
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Сайт Хабр", url='http://127.0.0.1:8080/')
        button2 = types.InlineKeyboardButton("Сайт Хабр правила", url='http://127.0.0.1:8080/rules')
        button3 = types.InlineKeyboardButton("Сайт Хабр регистрация", url='http://127.0.0.1:8080/Cams')
        markup.add(button1, button2, button3)
        keyboard.add(b2)

        a = bot.send_message(message.chat.id,
                             f"Сэр {message.from_user.username} - Лучше всего перейти на сайт по кнопке")
        a1 = bot.send_photo(message.chat.id,
                            'https://www.meme-arsenal.com/memes/8813fd8b7aa8f1efd97c435c679fa3e1.jpg'.format(
                                message.from_user),
                            reply_markup=markup)
        a2 = bot.send_audio(message.chat.id,
                            'https://mp3minusovki.com/music/fhvndfjwserjgt/8f58cee79c35b16d1f8de40659394245/f5135242a10a5f2b7966b355846b8adb.mp3',
                            reply_markup=keyboard)

        # Готов
    if message.text == 'Почему такое название бота?':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        n1 = bot.send_message(message.chat.id, 'А тебе это важно?', reply_markup=keyboard)
        time.sleep(1)
        n2 = bot.send_photo(message.chat.id,
                            'https://risovach.ru/upload/2014/06/mem/tvoe-vyrazhenie-lica_53549909_orig_.jpeg')
        time.sleep(2)
        n3 = bot.send_message(message.chat.id, 'Всё поняли.....')
        n = [n1, n2, n3]
        for i in n:
            time.sleep(1.6)
            bot.delete_message(message.chat.id, i.id)
        start_message(message)
        # Помощник

    if message.text == 'Нет':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, 'Всмысле не можешь.', reply_markup=keyboard)
        time.sleep(2)
        bot.send_photo(message.chat.id, 'https://risovach.ru/upload/2014/01/mem/kakoy-pacan_41226535_orig_.jpeg')
        b1 = types.KeyboardButton('Назад в ад')
        b2 = types.KeyboardButton('хотите факт')
        b3 = types.KeyboardButton('О боте')
        keyboard.add(b1, b3, b2)
        bot.send_message(message.chat.id, f'Куда дальше',
                         reply_markup=keyboard)

    if message.text == 'хотите факт':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        c = types.KeyboardButton('Назад в ад')
        keyboard.add(c)
        r = rd.randint(0, 4)
        bot.send_message(message.chat.id, f'Хотите факт о {fakt[r][1]}', reply_markup=keyboard)
        time.sleep(1)
        bot.send_message(message.chat.id, f'{fakt[r][0]}', reply_markup=keyboard)

    if message.text.lower() == 'о боте':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,
                               f'{priv[rd.randint(0, 3)]} Если вы не поняли то я......{priv[rd.randint(0, 3)]}')
        bot.send_photo(message.chat.id,
                             'https://timeweb.com/ru/community/article/f9/f9126325726f89cede1e0ec2c3f8e501.jpg')
        b1 = types.KeyboardButton('Понял')
        keyboard.add(b1)
        bot.send_message(message.chat.id, f'Я есть {bot_pohval[rd.randint(0, 3)]}', reply_markup=keyboard)

    if message.text == 'Назад в ад':
        start_message(message)

    if message.text == 'Понял':
        bn1 = bot.send_message(message.chat.id, f"Хорошо")
        time.sleep(2)
        bot.delete_message(message.chat.id, bn1.id)
        start_message(message)

    if message.text == 'Да':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b1 = types.KeyboardButton('Добавить')
        b2 = types.KeyboardButton('Изменить')
        b3 = types.KeyboardButton('Узнать')
        b4 = types.KeyboardButton('Назад в ад')
        keyboard.add(b1, b2, b3, b4)
        bot.send_message(message.chat.id, 'Выберети что хотите сделать', reply_markup=keyboard)

    if message.text == 'Узнать':
        types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, 'Введите логин и пароль')
        bot.register_next_step_handler(message, car_name)

    if message.text == 'Добавить':
        types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, 'Введите новый - логин и пароль')
        bot.register_next_step_handler(message, new_name)

    if message.text == 'Изменить':
        types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, 'Введите логи и пароль того пользватеоя которого хотите изменить')
        bot.register_next_step_handler(message, up_name)


def new_name(message):
    con = sqlite3.connect('regs.db')
    cur = con.cursor()
    a, b = map(str, message.text.split())
    bot.send_message(message.chat.id, f"{a} --- L {b} --- P")
    result = cur.execute("""SELECT login FROM regs""").fetchall()
    st = bot.send_message(message.chat.id, f"{a} --- L {b} --- P Cтатус: ----")

    if a in result:
        bot.send_message(chat_id=message.chat.id, message_id=st.id,
                         text=f"{a} --- L {b} --- P Cтатус: -- Занято")
        # print(elem)

    if a not in result:
        bot.send_message(chat_id=message.chat.id, message_id=st.id,
                         text=f"{a} --- L {b} --- P Cтатус: -- Занято")
    con.close()


def up_name(message):
    con = sqlite3.connect('regs.db')
    cur = con.cursor()

    a, b = map(str, message.text.split())
    bot.send_message(message.chat.id, f"{a} --- L {b} --- P")
    result = cur.execute("""SELECT * FROM regs""").fetchall()
    st = bot.send_message(message.chat.id, f"{a} --- L {b} --- P Cтатус: ----")

    for elem in result:
        if elem[1] == a:
            if b == elem[2]:
                print('Логн и пароль верны')
                bot.edit_message_text(chat_id=message.chat.id, message_id=st.id,
                                      text=f"{a} --- L {b} --- P Cтатус: --{da[rd.randint(0, 4)]}")
                bot.send_message(message.chat.id, "Введите Логин и Пароль")
                text = message.text
                a1, b1 = map(str, text.split())
                cur.execute("""UPDATE regs SET login = a1 WHERE login == a""").fetchall()
                cur.execute("""UPDATE regs SET password = b1 WHERE password == b""").fetchall()

                con.commit()
                con.close()

            else:
                print('Пароль от логина не верный')
                print(elem)
                bot.edit_message_text(chat_id=message.chat.id, message_id=st.id,
                                      text=f"{a} --- L {b} --- P Cтатус: --{net[rd.randint(0, 4)]}")
        else:
            print('Нет такого логина')
            bot.edit_message_text(chat_id=message.chat.id, message_id=st.id,
                                  text=f"{a} --- L {b} --- P Cтатус: -Логин-{net[rd.randint(0, 4)]}")
    con.close()
    start_message(message)


def car_name(message):
    con = sqlite3.connect('regs.db')
    cu = con.cursor()

    a, b = map(str, message.text.split())
    bot.send_message(message.chat.id, f"{a} --- L {b} --- P")
    result = cu.execute("""SELECT login FROM regs""").fetchall()
    result1 = cu.execute("""SELECT password FROM regs""").fetchall()
    st = bot.send_message(message.chat.id, f"{a} --- L {b} --- P Cтатус: ----")

    if a in result:
        if b in result1:
            print('Логн и пароль верны')
            bot.edit_message_text(chat_id=message.chat.id, message_id=st.id,
                                  text=f"{a} --- L {b} --- P Cтатус: --{da[rd.randint(0, 4)]}")
            # print(elem)
        else:
            print('Пароль от логина не верный')
            # print(elem)
            bot.edit_message_text(chat_id=message.chat.id, message_id=st.id,
                                  text=f"{a} --- L {b} --- P Cтатус: --{net[rd.randint(0, 4)]}")
    else:
        print('Нет такого логина')
        bot.edit_message_text(chat_id=message.chat.id, message_id=st.id,
                              text=f"{a} --- L {b} --- P Cтатус: -Логин-{net[rd.randint(0, 4)]}")
    con.close()
    start_message(message)


bot.polling(non_stop=True)
