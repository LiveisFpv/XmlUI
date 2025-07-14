from PyQt6.QtWidgets import QMainWindow
from designs.main_window import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("XML редактор")
        self.setGeometry(100, 100, 800, 720)
        