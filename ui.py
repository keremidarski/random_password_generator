from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QTextEdit, QPushButton
from PyQt5 import uic
from random_password_generator import RandomPasswordGenerator


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("window.ui", self)

        self.title_label = self.findChild(QLabel, "title_label")
        self.pass_length_label = self.findChild(QLabel, "pass_length_label")
        self.pass_length_text_edit = self.findChild(QTextEdit, "pass_length_text_edit")
        self.generate_button = self.findChild(QPushButton, "generate_button")
        self.copy_button = self.findChild(QPushButton, "copy_button")
        self.password_label = self.findChild(QLabel, "password_label")

        self.copy_button.clicked.connect(self.copy_to_clipboard)
        self.generate_button.clicked.connect(self.clicker)
        self.show()

    def clicker(self):
        self.result = RandomPasswordGenerator(
            int(self.pass_length_text_edit.toPlainText())
        )
        self.password_label.setText(f"{self.result}")

    def copy_to_clipboard(self):
        cb = QApplication.clipboard()
        cb.setText(f"{self.result}")
