import telebot
import mysql.connector
from telebot import types
import os
import time
import threading
import datetime
from os import getenv
from dotenv import load_dotenv

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='qwerty123456',
    database='tests'
)
cursor = db.cursor()

load_dotenv()
TOKEN = str(getenv('TG_TOKEN'))
bot = telebot.TeleBot(TOKEN) #@EduTestsBot

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать! Введите /help, для того чтобы получить список доступных команд')

@bot.message_handler(commands=['help'])
def show_help(message):
    bot.reply_to(message, 'Команды: \n/list - вывод списка доступных тестов \n/test <название_теста> - поиск теста по названию')

@bot.message_handler(commands=['list'])
def list_tests(message):
    cursor.execute('SELECT * FROM tests')
    tests = cursor.fetchall()

    markup = types.InlineKeyboardMarkup()
    tests_btns = []
    if tests:
        test_list = 'Список доступных тестов:\n'
        for test in tests:
            #test_list += f'{test[1]}\n'
            tests_btns.append(types.InlineKeyboardButton(f'{test[1]}', callback_data=f'start_test:{test[1]}'))
            markup.add(tests_btns[len(tests_btns) - 1])
        bot.send_message(message.chat.id, test_list, reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'В базе данных нет доступных тестов.')
    
# @bot.message_handler(commands=['test'])
# def answer_test(message):
    

@bot.message_handler(content_types=["text"])
def answer(message):
    answers[i + 1] = message.text

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    global i
    global questions
    global msg
    global answers
    global photos

    if call.data.startswith('start_test:'):
        cursor.execute('SELECT * FROM tests')
        tests = cursor.fetchall()
        test_name = call.data.split(':')[1]
        global found_test
        found_test = None
        for test in tests:
            if test[1] == test_name:
                found_test = test
                break

        if found_test:
            markup = types.InlineKeyboardMarkup()
            start_btn = types.InlineKeyboardButton('Начать тестирование', callback_data='start_test')
            markup.add(start_btn)
            info_btn = types.InlineKeyboardButton('Описание', callback_data='info')
            markup.add(info_btn)
        
            bot.send_message(call.message.chat.id, f'Выбран тест: {found_test[1]}\nВремя: {found_test[3]} мин.', reply_markup=markup)
            global selection
            selection = found_test[0]
            global tg
            tg = call.message.from_user.username
        else:
            bot.send_message(call.message.chat.id, f"Тест с названием '{test_name}' не найден.")

    if call.data == 'info':
        bot.reply_to(call.message, f'Описание теста: {found_test[2]}')

    if call.data == 'start_test':
        global exit_test
        exit_test = False
        global x
        def test_time():
            d = datetime.timedelta(minutes=found_test[3])
            n = datetime.datetime.now()
            n += d
            while True:
                if exit_test:
                    return 0
                if str(datetime.datetime.now().strftime("%H:%M")) == str(n.strftime("%H:%M")):
                    bot.delete_message(msg.chat.id, msg.message_id)
                    global result
                    j = 0
                    p = 0
                    s = ''
                    for _ in answers:
                        if str(list(answers.values())[j]) == str(answer_t[j]):
                            p += 1
                            s += f'✅ {j + 1}: {answer_t[j]}\n'
                        else:
                            s += f'❌ {j + 1}: {list(answers.values())[j]}\n'
                        j += 1
                    result = f'{p}/{len(questions)}'
                    s += f'Тест окончен\nРезультат: {result}'
                    bot.send_message(call.message.chat.id, s)

                    cursor.execute("INSERT INTO students_tests (tests_id, students_id, result) VALUES (%s, %s, %s)", (found_test[0], call.message.from_user.username, result))
                    db.commit()

        x = threading.Thread(target=test_time)
        x.start()
        i = 0
        cursor.execute(f'SELECT tests.questions.name, tests_id, tests.questions.image FROM tests.questions JOIN tests.tests_questions ON tests.questions.id = tests.tests_questions.questions_id WHERE tests_id = {selection}')
        questions = cursor.fetchall()
        photos = [n[2] for n in questions]
        questions = [n[0] for n in questions]
        markup = types.InlineKeyboardMarkup()
        markup.row_width = 3
        markup.add(types.InlineKeyboardButton("⬅️", callback_data="left"), 
                   types.InlineKeyboardButton(f"{i + 1}/{len(questions)}", callback_data="pagination"), 
                   types.InlineKeyboardButton("➡️", callback_data="right"), 
                   types.InlineKeyboardButton("Ответы", callback_data="answer"), 
                   types.InlineKeyboardButton("Закончить тест", callback_data="exit"))
        with open('misc\\placeholder.png', 'rb') as f:
            if photos[i] != None:
                msg = bot.send_photo(call.message.chat.id, photo=photos[i], caption=f'{questions[i]}', reply_markup=markup)
            else:
                msg = bot.send_photo(call.message.chat.id, photo=f, caption=f'{questions[i]}', reply_markup=markup)
        
        answers = {}
        for k in range(len(questions)):
            answers[k + 1] = 'Нет ответа'

        global answer_t
        cursor.execute(f"SELECT answers.name FROM questions_answers JOIN questions ON questions.id = questions_id JOIN answers ON answers.id = answers_id JOIN tests_questions ON questions_answers.questions_id = tests_questions.questions_id WHERE tests_id = {found_test[0]}")
        answer_t = cursor.fetchall()
        answer_t = [n[0] for n in answer_t]

        # print(answers)
        # print(answer_t)

    if call.data == 'left':
        if i == 0:
            pass
        else:
            i -= 1
        markup = types.InlineKeyboardMarkup()
        markup.row_width = 3
        markup.add(types.InlineKeyboardButton("⬅️", callback_data="left"), 
                   types.InlineKeyboardButton(f"{i + 1}/{len(questions)}", callback_data="pagination"), 
                   types.InlineKeyboardButton("➡️", callback_data="right"), 
                   types.InlineKeyboardButton("Ответы", callback_data="answer"), 
                   types.InlineKeyboardButton("Закончить тест", callback_data="exit"))
        with open('misc\\placeholder.png', 'rb') as f:
            if photos[i] != None:
                bot.edit_message_media(chat_id=call.message.chat.id, message_id=msg.message_id, media=types.InputMediaPhoto(media=photos[i], caption = f'{questions[i]}'), reply_markup=markup)
            else:
                bot.edit_message_media(chat_id=call.message.chat.id, message_id=msg.message_id, media=types.InputMediaPhoto(media=f, caption = f'{questions[i]}'), reply_markup=markup)

    if call.data == 'right':
        if i == len(questions):
            pass
        else:
            i += 1
        markup = types.InlineKeyboardMarkup()
        markup.row_width = 3
        markup.add(types.InlineKeyboardButton("⬅️", callback_data="left"), 
                   types.InlineKeyboardButton(f"{i + 1}/{len(questions)}", callback_data="pagination"), 
                   types.InlineKeyboardButton("➡️", callback_data="right"), 
                   types.InlineKeyboardButton("Ответы", callback_data="answer"), 
                   types.InlineKeyboardButton("Закончить тест", callback_data="exit"))
        with open('misc\\placeholder.png', 'rb') as f:
            if photos[i] != None:
                bot.edit_message_media(chat_id=call.message.chat.id, message_id=msg.message_id, media=types.InputMediaPhoto(media=photos[i], caption = f'{questions[i]}'), reply_markup=markup)
            else:
                bot.edit_message_media(chat_id=call.message.chat.id, message_id=msg.message_id, media=types.InputMediaPhoto(media=f, caption = f'{questions[i]}'), reply_markup=markup)

    if call.data == 'answer':
        a = 0
        for _ in answers:
            bot.send_message(call.message.chat.id, f'{a + 1}) {list(answers.values())[a]}')
            a += 1

    if call.data == 'exit':
        exit_test = True
        bot.delete_message(msg.chat.id, msg.message_id)
        global result
        j = 0
        p = 0
        s = ''
        for _ in answers:
            if str(list(answers.values())[j]) == str(answer_t[j]):
                p += 1
                s += f'✅ {j + 1}: {answer_t[j]}\n'
            else:
                s += f'❌ {j + 1}: {list(answers.values())[j]}\n'
            j += 1
        result = f'{p}/{len(questions)}'
        s += f'Тест окончен\nРезультат: {result}'
        bot.send_message(call.message.chat.id, s)

        cursor.execute("INSERT INTO students (tg_id) VALUES (%s)", (tg,))
        cursor.execute("INSERT INTO students_tests (tests_id, students_id, result) VALUES (%s, %s, %s)", (found_test[0], cursor.lastrowid, p))
        db.commit()

bot.infinity_polling()
