import \
    sys

from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
window = QMainWindow()

def show_dialog():
    msg = QMessageBox()
    msg.setWindowTitle("Dialogue window")
    msg.setText("Hello, this is dialogue window!")
    msg.exec()

button = QPushButton("Show dialogue")

window.setCentralWidget(button)
window.show()
app.exec()