from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtCore import pyqtSlot, pyqtSignal
class SelectButton(QPushButton):
    
    checkedStateChanged = pyqtSignal(bool)

    def __init__(self,text="", parent=None):
        super().__init__(text, parent)
        

        self.style_enabled = """font: 14pt \"Segoe UI\";
                                    text-align: left;
                                    padding: 8px 16px;
                                    border: none;
                                    border-radius: 20px;
                                    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0.6, y2:0, stop:0 #93c5fd, stop:1 #f2f2f2);
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
    
        # Инициализация стиля
        self.update_style()
        
        self.toggled.connect(self.__handle_toggle)
    
    def onload_styles(self):
        self.update_style()
    
    def enterEvent(self, event):
        if not self.isChecked():
            self.setStyleSheet(self.style_hover)
        super().enterEvent(event)
    
    def leaveEvent(self, event):
        self.update_style()
        super().leaveEvent(event)
    
    def update_style(self):
        """Обновляет стиль в зависимости от состояния кнопки"""
        if self.isChecked():
            self.setStyleSheet(self.style_enabled)
        else:
            self.setStyleSheet(self.style_disabled)

    def __handle_toggle(self, checked):
        """Внутренний обработчик изменения состояния"""
        self.checkedStateChanged.emit(checked)
        self.update_style()