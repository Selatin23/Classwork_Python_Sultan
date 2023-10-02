from PyQt6.QtCore import QThread, pyqtSignal
import socket
from logger import log

class UDPReceiver(QThread):
    message = pyqtSignal(str, str)
    hello = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.address = ('localhost', 9900)
        self.running = False

    
    def run(self):
        log.i("Ресивер запущен")
        self.socket.bind(self.address)
        self.running = True
        while self.running:
            data, addr = self.socket.recvfrom(4096)
            message = data.decode(encoding="utf-8")
            log.d(f'получено сообщение от {addr}: {message}')
    
    def stop(self):
        self.running = False
        super().stop()