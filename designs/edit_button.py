from PyQt6.QtWidgets import QPushButton

class EditButton(QPushButton):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("""
            QPushButton {
                font: 12pt "Segoe UI";
                border: none;
                padding: 5px;
                border-radius: 4px;
                color: black;
                outline: none;
            }
            QPushButton:hover {
                background-color: #93c5fd;
                color: #1D4ED8;
            }
        """)
