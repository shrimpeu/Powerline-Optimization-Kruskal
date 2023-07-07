from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multiple Object Sets Example")

        self.set1_widgets = []
        self.set2_widgets = []

        self.create_set1_widgets()
        self.create_set2_widgets()

        self.show_set1_widgets()

    def create_set1_widgets(self):
        button1 = QPushButton("Button 1", self)
        button1.setGeometry(50, 50, 100, 30)
        button1.clicked.connect(self.show_set2_widgets)
        self.set1_widgets.append(button1)

    def create_set2_widgets(self):
        button2 = QPushButton("Button 2", self)
        button2.setGeometry(50, 50, 100, 30)
        button2.clicked.connect(self.show_set1_widgets)
        self.set2_widgets.append(button2)

    def show_set1_widgets(self):
        for widget in self.set2_widgets:
            widget.hide()
        for widget in self.set1_widgets:
            widget.show()

    def show_set2_widgets(self):
        for widget in self.set1_widgets:
            widget.hide()
        for widget in self.set2_widgets:
            widget.show()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
