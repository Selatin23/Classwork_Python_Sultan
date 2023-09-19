from PyQt6.QtCore import QThread

class UDPReceiver(QThread):
    def run(self):
        print("UdpReceiver запущен")