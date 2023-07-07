from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QTabWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tabbed Window Example")

        tab_widget = QTabWidget()
        self.setCentralWidget(tab_widget)

        tab1 = QWidget()
        tab2 = QWidget()

        tab_widget.addTab(tab1, "Tab 1")
        tab_widget.addTab(tab2, "Tab 2")

        # Add objects/widgets to each tab
        layout1 = QVBoxLayout(tab1)
        layout2 = QVBoxLayout(tab2)
        layout1.addWidget(QPushButton("Button 1"))
        layout2.addWidget(QPushButton("Button 2"))

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
