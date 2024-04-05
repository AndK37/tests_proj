import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QFormLayout, QTimeEdit, QMessageBox

class TestForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Добавление теста")
        self.setGeometry(100, 100, 400, 200)

        self.test_name_label = QLabel("Название теста:")
        self.test_name_input = QLineEdit()

        self.timer_label = QLabel("Время на ответ")
        self.timer_input = QTimeEdit()

        self.question_label = QLabel("Вопрос:")
        self.question_input = QLineEdit()

        self.options_labels = []
        self.options_inputs = []
        self.options_scores = []
        self.add_option_button = QPushButton("Добавить вариант ответа")
        self.submit_button = QPushButton("Добавить тест")

        layout = QFormLayout()
        layout.addRow(self.test_name_label, self.test_name_input)
        layout.addRow(self.timer_label, self.timer_input)
        layout.addRow(self.question_label, self.question_input)

        for i in range(2):
            option_label = QLabel(f"Вариант ответа {i + 1}:")
            option_input = QLineEdit()
            option_score = QLineEdit()
            self.options_labels.append(option_label)
            self.options_inputs.append(option_input)
            self.options_scores.append(option_score)
            layout.addRow(option_label, option_input)
            layout.addRow(QLabel("Баллы:"), option_score)

        layout.addWidget(self.add_option_button)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

        self.add_option_button.clicked.connect(self.add_option)
        self.submit_button.clicked.connect(self.submit_test)

    def add_option(self):
        new_option_label = QLabel(f"Вариант ответа {len(self.options_labels) + 1}:")
        new_option_input = QLineEdit()
        new_option_score = QLineEdit()
        self.options_labels.append(new_option_label)
        self.options_inputs.append(new_option_input)
        self.options_scores.append(new_option_score)

        index = self.layout().count() - 2
        self.layout().insertRow(index, new_option_label, new_option_input)
        self.layout().insertRow(index + 1, QLabel("Баллы:"), new_option_score)

    def submit_test(self):
        test_name = self.test_name_input.text()
        timer = self.timer_input.time().toString()
        question = self.question_input.text()
        options = [(input.text(), score.text()) for input, score in zip(self.options_inputs, self.options_scores)]

        # Добавление теста в базу данных

        msg = QMessageBox()
        msg.setWindowTitle("Успех")
        msg.setText("Тест успешно добавлен")
        msg.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    add_test_form = TestForm()
    add_test_form.show()
    sys.exit(app.exec())
