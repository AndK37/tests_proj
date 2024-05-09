import telebot
import mysql.connector
from telebot import types

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='qwerty123456',
    database='tests'
)
cursor = db.cursor()

bot = telebot.TeleBot('7133925834:AAEhUDDIlK8oBv-97m2-ZnUMvNgSqUbBV3k') #@EduTestsBot

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

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    cursor.execute('SELECT * FROM tests')
    selected_test = cursor.fetchone()
    if call.data == 'info':
        test_description = selected_test[2]
        if selected_test:
            bot.reply_to(call.message, f'Описание теста: {test_description}')

bot.infinity_polling()
