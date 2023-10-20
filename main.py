import sys
import threading

from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication

from backend import ChatBot


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.chat_bot = ChatBot()

        self.setMinimumSize(700, 500)

        # VBoxLayout()

        # Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)
        self.chat_area.setText("")

        # Add the input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 400, 40)
        self.input_field.returnPressed.connect(self.send_message)

        # Add the button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(420, 340, 70, 40)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append("Me: " + user_input + "\n")

        # Create a thread to get the chatbot response
        thread = threading.Thread(target=self.get_chatbot_response, args=(user_input,))
        thread.start()

    def get_chatbot_response(self, user_input):
        response = self.chat_bot.get_response(user_input)
        self.chat_area.append("Bot: " + response + "\n")

app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())