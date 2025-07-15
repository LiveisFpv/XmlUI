from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import pyqtSignal

class SelectButton(QPushButton):
    checkedStateChanged = pyqtSignal(bool)

    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setCheckable(True)
        self.setStyleSheet("""
            QPushButton {
                font: 14pt "Segoe UI";
                text-align: left;
                padding: 8px 16px;
                border: none;
                border-radius: 20px;
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:0.6, y2:0, stop:0 #e1e1e1, stop:1 #f2f2f2);
                color: black;
                outline: none;
            }
            QPushButton:hover {
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:0.6, y2:0, stop:0 #dbeaef, stop:1 #f2f2f2);
                color: black;
            }
            QPushButton:checked {
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:0.6, y2:0, stop:0 #93c5fd, stop:1 #f2f2f2);
                color: #1D4ED8;
            }
        """)
        self.toggled.connect(self.__handle_toggle)

    def __handle_toggle(self, checked):
        self.checkedStateChanged.emit(checked)
