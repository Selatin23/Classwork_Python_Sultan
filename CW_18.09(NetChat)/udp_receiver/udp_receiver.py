from PyQt6.QtCore import QThread

class UDPReceiver(QThread):

    def __init__(self):
        super().__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.address = (localhost, 9900)
        

    
    def run(self):
        log.i("Ресивер запущен")
        print("UdpReceiver запущен")
    
    def stop(self):
        self.running = False
        super().stop()