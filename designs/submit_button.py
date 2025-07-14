from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtCore import pyqtSlot
class SubmitButton(QPushButton):
    def __init__(self,text="", parent=None):
        super().__init__(text, parent)
        self.enterEvent = self.on_button_enter
        self.leaveEvent = self.on_button_leave
        self.style_default = """font: 12pt \"Segoe UI\";
                            text-align: center;
                            padding: 9px 16px;
                            border: none;
                            border-radius: 15px;
                            background-color: #2563eb;
                            color: #fff;"""
        self.style_hover = """font: 12pt \"Segoe UI\";
                            text-align: center;
                            padding: 9px 16px;
                            border: none;
                            border-radius: 15px;
                            background-color: #1d4ed8;
                            color: #fff;"""
        self.onload_styles()
    
    def onload_styles(self):
        self.setStyleSheet(self.style_default)

    @pyqtSlot()
    def on_button_enter(self, event):
        self.setStyleSheet(self.style_hover)
        self.update()
    
    @pyqtSlot()
    def on_button_leave(self, event):
        self.setStyleSheet(self.style_default)
        self.update()