from views.main_window import MainWindow
import PyQt6.QtWidgets

class MainController:
    def __init__(self, view: MainWindow):
        self.view = view