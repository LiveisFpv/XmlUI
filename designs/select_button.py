from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtCore import pyqtSlot
class SelectButton(QPushButton):
    def __init__(self,text="", parent=None):
        super().__init__(text, parent)
        self.enterEvent = self.on_button_enter
        self.leaveEvent = self.on_button_leave
        self.style_enabled = """font: 14pt \"Segoe UI\";
                                    text-align: left;
                                    padding: 8px 16px;
                                    border: none;
                                    border-radius: 20px;
                                    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0.6, y2:0, stop:0 #dbeaef, stop:1 #f2f2f2);
                                    color: #1D4ED8;
                                    """
        self.style_disabled = """font: 14pt \"Segoe UI\";
                                    text-align: left;
                                    padding: 8px 16px;
                                    border: none;
                                    border-radius: 20px;
                                    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0.6, y2:0, stop:0 #e1e1e1, stop:1 #f2f2f2);
                                    color: black;
                                    """
        self.style_hover = """font: 14pt \"Segoe UI\";
                                    text-align: left;
                                    padding: 8px 16px;
                                    border: none;
                                    border-radius: 20px;
                                    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0.6, y2:0, stop:0 #dbeaef, stop:1 #f2f2f2);
                                    color: black;
                                    """
    
    def onload_styles(self):
        if self.isChecked():
            self.setStyleSheet(self.style_enabled)
        else:
            self.setStyleSheet(self.style_disabled)

    @pyqtSlot()
    def on_button_enter(self, event):
        self.setStyleSheet(self.style_hover)
        self.update()
    
    @pyqtSlot()
    def on_button_leave(self, event):
        if self.isChecked():
            self.setStyleSheet(self.style_enabled)
        else:
            self.setStyleSheet(self.style_disabled)
        self.update()