def register(self):
        db = DB()
        db.reg(self.lineEdit_ln.text(), self.lineEdit_fn.text(), self.lineEdit_mn.text(), self.lineEdit_mail.text(), self.lineEdit_log.text(), self.lineEdit_pwd.text())
        
self.btn_reg.clicked.connect(self.register)

import re
#[^@]+@[^@]+\.[^@]+
x = re.search(r'[^@]+@[^@]+\.[^@]+', mail) 

if not le:
        self.w.setStyleSheet(u"color: rgb(255, 0, 0);")

