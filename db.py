import mysql.connector
import hashlib

class DB:
    def __init__(self):
        self.db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',#qwerty123456
        database='tests'
        )
        
    def reg(self, ln, fn, mn, e, l, p):
        h = hashlib.new('SHA256')
        h.update(p.encode())
        p_h = h.hexdigest()

        cursor = self.db.cursor()
        cursor.execute('INSERT INTO teachers (last_name, first_name, mid_name, email, login, password) VALUES (%s, %s, %s, %s, %s, %s)', (ln, fn, mn, e, l, p_h))
        self.db.commit()

    def add_test(self, name, description, time, questions, answers, imgs, t_id):
        cursor = self.db.cursor()
        cursor.execute('INSERT INTO tests (name, description, time, teachers_id) VALUES (%s, %s, %s, %s)', (name, description, time, t_id))
        #self.db.commit()

        self.test_id = cursor.lastrowid

        i = 0
        for question in questions:
            cursor.execute('INSERT INTO questions (name, image) VALUES (%s, %s)', (question, imgs.get(i)))
            self.question_id = cursor.lastrowid
            cursor.execute('INSERT INTO tests_questions (tests_id, questions_id) VALUES (%s, %s)', (self.test_id, self.question_id))
            cursor.execute('INSERT INTO answers (name) VALUES (%s)', (answers[i],))
            self.answer_id = cursor.lastrowid
            cursor.execute('INSERT INTO questions_answers (questions_id, answers_id) VALUES (%s, %s)', (self.question_id, self.answer_id))
            i += 1

        self.db.commit()
        self.db.close()

    def login(self, l, p):
        h = hashlib.new('SHA256')
        h.update(p.encode())
        p_h = h.hexdigest()

        cursor = self.db.cursor()
        cursor.execute(f'SELECT id, login, password, first_name, mid_name FROM tests.teachers WHERE login = \"{l}\" AND password = \"{p_h}\"')
        t_data = cursor.fetchone()

        self.db.close()
        return t_data
    
    def view_tests(self, id):
        cursor = self.db.cursor()
        cursor.execute(f'SELECT name, description, time FROM tests.tests WHERE teachers_id = {id}')
        data = cursor.fetchall()
        self.db.close()
        return data
    
    def get_email_by_login(self, l):
        cursor = self.db.cursor()
        cursor.execute(f'SELECT email FROM teachers WHERE login = \"{l}\"')
        email = cursor.fetchone()[0]
        return email