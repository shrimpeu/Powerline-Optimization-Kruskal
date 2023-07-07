import sys
# from PyQt5 import QtWidgets  # QMainWindow()
from PyQt5.QtWidgets import *  # QApplication() QMainWindow
from PyQt5.QtCore import Qt  # mousePressEvent


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.width = 1440
        self.height = 810
        self.setWindowTitle("Gridy Algorithm")
        self.setMinimumSize(self.width, self.height)
        self.setMaximumSize(self.width, self.height)
        self.show()

    def mousePressEvent(self, event, **kwargs):
        if event.button() == Qt.LeftButton:
            print("Left mouse button clicked.")
        elif event.button() == Qt.RightButton:
            print("Right mouse button clicked.")
        mouse_pos = event.pos()
        print(str(mouse_pos.x()) + ", " + str(mouse_pos.y()))
    '''def mouseMoveEvent(self, event):
        print("Mouse moved to position:", event.pos())'''


app = QApplication(sys.argv)
window = MainWindow()
app.exec_()
