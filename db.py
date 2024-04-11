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

    def add_test(self, name, description, time, questions):
        cursor = self.db.cursor()
        cursor.execute('INSERT INTO tests (name, description, time) VALUES (%s, %s, %s)', (name, description, time))
        self.db.commit()

        test_id = cursor.lastrowid

        for question in questions:
            cursor.execute('INSERT INTO questions (name, description, image) VALUES (%s, %s, %s)', (question.get('name', ''), question.get('description', ''), question.get('image', '')))
            self.db.commit()
    
            question_id = cursor.lastrowid

            cursor.execute('INSERT INTO tests_questions (test_id, question_id) VALUES (%s, %s)', (test_id, question_id))
            self.db.commit()
    
            answers = question.get('answers', [])

            for answer in answers:
                cursor.execute('INSERT INTO answers (name) VALUES (%s)', (answer,))
                self.db.commit()
            
                answer_id = cursor.lastrowid
                
                cursor.execute('INSERT INTO questions_answers (question_id, answer_id) VALUES (%s, %s)', (question_id, answer_id))
                self.db.commit()

        self.db.commit()