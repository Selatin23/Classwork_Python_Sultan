from PyQt6.QtCore import QObject

from logger import Logger

#from data_storage.data import DataStorage
from data_storage import DataStorage

#from gui.gui import Gui
from gui import Gui


#from udp_reciever.udp_receiver import UdpReceiver
from udp_receiver import UDPReceiver

#from udp_sender.udp_sender import UdpSender
from udp_sender import UdpSender


class Router(QObject):
    def __init__(self):
        super().__init__()
        self.data_storage = DataStorage()
        self.gui = Gui()
        self.udp_reciver = UDPReceiver()
        self.udp_sender = UdpSender()

        # Здесь будем роутить сигналы

    def start(self):
        self.data_storage.start()
        self.gui.start()
        self.udp_reciver.start()
        self.udp_sender.start()
    
    def stop(self):   
        self.udp_sender.stop
        self.udp_reciver.stop()
        self.gui.stop()
        self.data_storage.stop()

