import sys

from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(700, 500)

        # VBoxLayout()

        # Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # Add the input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 400, 40)

        # Add the button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(420, 340, 70, 40)

        self.show()

class ChatBot:
    pass

app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())