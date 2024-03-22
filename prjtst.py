from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import sys

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Регистрация")
        self.resize(300, 200)

        self.layout = QVBoxLayout()

        self.lb_last_name = QLabel("Фамилия:")
        self.lb_last_name.setStyleSheet("font-size: 16pt;")
        self.edit_last_name = QLineEdit()

        self.lb_first_name = QLabel("Имя:")
        self.lb_first_name.setStyleSheet("font-size: 16pt;")
        self.edit_first_name = QLineEdit()

        self.lb_patronymic = QLabel("Отчество:")
        self.lb_patronymic.setStyleSheet("font-size: 16pt;")
        self.edit_patronymic = QLineEdit()

        self.lb_email = QLabel("E-mail:")
        self.lb_email.setStyleSheet("font-size: 16pt;")
        self.edit_email = QLineEdit()

        self.lb_password = QLabel("Пароль:")
        self.lb_password.setStyleSheet("font-size: 16pt;")
        self.edit_password = QLineEdit()
        self.edit_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.button_register = QPushButton("Зарегистрироваться")
        self.button_register.setStyleSheet("font-size: 16pt;")
        self.button_register.clicked.connect(self.register)

        self.layout.addWidget(self.lb_last_name)
        self.layout.addWidget(self.edit_last_name)

        self.layout.addWidget(self.lb_first_name)
        self.layout.addWidget(self.edit_first_name)

        self.layout.addWidget(self.lb_patronymic)
        self.layout.addWidget(self.edit_patronymic)

        self.layout.addWidget(self.lb_email)
        self.layout.addWidget(self.edit_email)

        self.layout.addWidget(self.lb_password)
        self.layout.addWidget(self.edit_password)

        self.layout.addWidget(self.button_register)

        self.setLayout(self.layout)

        self.login_form = LoginForm()

    def register(self):
        self.login_form.show()
        self.close()

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Вход")
        self.resize(300, 100)

        self.layout = QVBoxLayout()

        self.lb_email = QLabel("E-mail:")
        self.lb_email.setStyleSheet("font-size: 16pt;")
        self.edit_email = QLineEdit()

        self.lb_password = QLabel("Пароль:")
        self.lb_password.setStyleSheet("font-size: 16pt;")
        self.edit_password = QLineEdit()
        self.edit_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.button_login = QPushButton("Вход")
        self.button_login.setStyleSheet("font-size: 16pt;")
        self.button_login.clicked.connect(self.login)

        self.button_register = QPushButton("Регистрация")
        self.button_register.setStyleSheet("font-size: 16pt;")
        self.button_register.clicked.connect(self.goto_register_form)

        self.button_forgot_password = QPushButton("Забыли пароль?")
        self.button_forgot_password.setStyleSheet("font-size: 16pt;")
        self.button_forgot_password.clicked.connect(self.forgot_password)

        self.layout.addWidget(self.lb_email)
        self.layout.addWidget(self.edit_email)

        self.layout.addWidget(self.lb_password)
        self.layout.addWidget(self.edit_password)

        self.layout.addWidget(self.button_login)
        self.layout.addWidget(self.button_register)
        self.layout.addWidget(self.button_forgot_password)

        self.setLayout(self.layout)

    def login(self):
        email = self.edit_email.text()
        password = self.edit_password.text()

    def goto_register_form(self):
        self.close()
        self.register_form = RegistrationForm()
        self.register_form.show()

    def forgot_password(self):
        print('test')
        # Добавить логику для восстановления пароля

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_form = LoginForm()
    login_form.show()

    sys.exit(app.exec())