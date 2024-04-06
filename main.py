import sys
from db import DB
from ui_main_scene import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow

class ExecuteTracker(QMainWindow):
    def __init__(self):
        super(ExecuteTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExecuteTracker()
    window.show()

    sys.exit(app.exec())