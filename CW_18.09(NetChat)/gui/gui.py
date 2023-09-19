from PyQt6.QtCore import QThread
from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/main.ui", self)

class Gui(QThread):
    def __init__(self):
        super().__init__()
        self.window = MainWindow()
        self.window.show()

    def run(self):
        print("Gui запущен")
        
        