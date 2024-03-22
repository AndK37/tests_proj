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