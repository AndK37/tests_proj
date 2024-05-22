import mysql.connector
import hashlib

class DB:
    def __init__(self):
        self.db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='qwerty123456',
        database='tests'
        )
        
    def reg(self, ln, fn, mn, e, l, p):
        h = hashlib.new('SHA256')
        h.update(p.encode())
        p_h = h.hexdigest()

        cursor = self.db.cursor()
        cursor.execute('INSERT INTO teachers (last_name, first_name, mid_name, email, login, password) VALUES (%s, %s, %s, %s, %s, %s)', (ln, fn, mn, e, l, p_h))
        self.db.commit()

    def add_test(self, name, description, time, questions, answers):
        cursor = self.db.cursor()
        cursor.execute('INSERT INTO tests (name, description, time) VALUES (%s, %s, %s)', (name, description, time))
        #self.db.commit()

        self.test_id = cursor.lastrowid

        i = 0
        for question in questions:
            cursor.execute('INSERT INTO questions (name) VALUES (%s)', (question,))
            #self.db.commit()
    
            self.question_id = cursor.lastrowid

            cursor.execute('INSERT INTO tests_questions (tests_id, questions_id) VALUES (%s, %s)', (self.test_id, self.question_id))
            #self.db.commit()

            
            cursor.execute('INSERT INTO answers (name) VALUES (%s)', (answers[i],))
                #self.db.commit()
            
            self.answer_id = cursor.lastrowid
                
            cursor.execute('INSERT INTO questions_answers (questions_id, answers_id) VALUES (%s, %s)', (self.question_id, self.answer_id))
                #self.db.commit()
            i += 1

        self.db.commit()
        self.db.close()