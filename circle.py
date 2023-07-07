from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor

class CircleWidget(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # Enable anti-aliasing for smoother edges
        painter.setBrush(QColor(255, 0, 0))  # Set the fill color of the circle
        painter.setPen(Qt.NoPen)  # Disable drawing the outline of the circle
        radius = min(self.width(), self.height()) / 2  # Calculate the radius based on widget size
        center = self.rect().center()  # Get the center point of the widget
        painter.drawEllipse(center, radius, radius)  # Draw the circle

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Circle Example")

        circle_widget = CircleWidget(self)
        self.setCentralWidget(circle_widget)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
