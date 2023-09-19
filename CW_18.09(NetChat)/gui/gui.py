from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import *
from PyQt6 import uic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/main.ui", self)

class Gui(QThread):
    sendMessage = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.window = MainWindow()
        self.window.show()

    def run(self):
        print("Gui запущен")
        button = self.window.findChild(QPushButton, "pushButton")
        button.setText("OLOLO")

        button.clicked.connect(self.send_message)

    def send_message(self):
        print("Button clicked")
        textedit = self.window.findChild(QTextEdit, "MessageToSend")
        message = textedit.text()
        self.sendMessage.emit(message)
        textedit.clear()
        