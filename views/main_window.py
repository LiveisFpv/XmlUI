from PyQt6.QtWidgets import QMainWindow
from designs.main_window import Ui_MainWindow
from views.selector import Selector


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.selector = Selector()
        self.setupUi(self)
        self.init_ui()
        
        

    def init_ui(self):
        """Инициализация пользовательского интерфейса"""
        self.setWindowTitle("XML редактор")
        self.setGeometry(100, 100, 800, 720)

        self.selector.add_select_button(self.value_button, selected=False)
        self.selector.add_select_button(self.phrases_button, selected=True)
        