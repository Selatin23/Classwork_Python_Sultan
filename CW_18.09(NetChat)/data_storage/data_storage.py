from PyQt6.QtCore import QThread

class DataStorage(QThread):
    def run(self):
        print("DataStorage запущен")