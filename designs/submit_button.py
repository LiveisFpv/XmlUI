from PyQt6.QtWidgets import QPushButton

class SubmitButton(QPushButton):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("""
            QPushButton {
                font: 12pt "Segoe UI";
                text-align: center;
                padding: 9px 16px;
                border: none;
                border-radius: 15px;
                background-color: #2563eb;
                color: #fff;
                outline: none;
            }
            QPushButton:hover {
                background-color: #1d4ed8;
                color: #fff;
            }
        """)
