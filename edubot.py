import telebot
import mysql.connector
from telebot import types
import os
import time

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='qwerty123456',
    database='tests'
)
cursor = db.cursor()

TOKEN = None
with open('token.txt') as f:
    TOKEN = f.read().strip()
bot = telebot.TeleBot(TOKEN) #@EduTestsBot

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать!')
    
    cursor.execute('SELECT * FROM tests')
    tests = cursor.fetchall()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for test in tests:
        test_btn = types.KeyboardButton(test[1])
        markup.add(test_btn)
    
    bot.send_message(message.chat.id, 'Выберите тест', reply_markup=markup)

@bot.message_handler(commands=['answer'])
def answer(message):
    answers[i] = message.text.split()[1:][0]

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    cursor.execute('SELECT * FROM tests WHERE name=%s', (message.text,))
    selected_test = cursor.fetchone()

    markup = types.InlineKeyboardMarkup()
    start_btn = types.InlineKeyboardButton('Начать тестирование', callback_data='start_test')
    markup.add(start_btn)
    info_btn = types.InlineKeyboardButton('Описание', callback_data='info')
    markup.add(info_btn)
    
    bot.send_message(message.chat.id, f'Выбран тест: {selected_test[1]}', reply_markup=markup)
    global selection
    selection = selected_test[0]

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    global i
    global questions
    global msg
    global answers

    if call.data == 'info':
        cursor.execute('SELECT * FROM tests')
        selected_test = cursor.fetchone()
        test_description = selected_test[2]
        if selected_test:
            bot.reply_to(call.message, f'Описание теста: {test_description}')

    if call.data == 'start_test':
        i = 0
        cursor.execute(f'SELECT tests.questions.name, tests_id FROM tests.questions JOIN tests.tests_questions ON tests.questions.id = tests.tests_questions.questions_id WHERE tests_id = {selection}')
        questions = cursor.fetchall()
        questions = [n[0] for n in questions]
        markup = types.InlineKeyboardMarkup()
        markup.row_width = 3
        markup.add(types.InlineKeyboardButton("⬅️", callback_data="left"), 
                   types.InlineKeyboardButton(f"{i + 1}/{len(questions)}", callback_data="pagination"), 
                   types.InlineKeyboardButton("➡️", callback_data="right"), 
                   types.InlineKeyboardButton("Ответы", callback_data="answer"), 
                   types.InlineKeyboardButton("Закончить тест", callback_data="exit"))
        msg = bot.send_message(call.message.chat.id, f'{questions[i]}', reply_markup=markup)
        answers = {}


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
        bot.edit_message_text(chat_id=call.message.chat.id, text=questions[i], message_id=msg.message_id, reply_markup=markup)

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
        bot.edit_message_text(chat_id=call.message.chat.id, text=questions[i], message_id=msg.message_id, reply_markup=markup)

    if call.data == 'answer':
        for answer in answers:
            bot.send_message(call.message.chat.id, f'{answer + 1}) {list(answers.values())[answer]}')


    if call.data == 'exit':
        #TODO: бд функционал
        pass 


bot.infinity_polling()
