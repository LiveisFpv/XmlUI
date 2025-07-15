from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPlainTextEdit, QDialogButtonBox
from models.phrase import Phrase
from models.value import Value

class EditPhraseDialog(QDialog):
    def __init__(self, parent=None, phrase : Phrase|None=None):
        super().__init__(parent)
        self.setWindowTitle("Редактировать фразу")
        self.setStyleSheet("""
            background-color: #f2f2f2;
            color: black;
        """)
        
        # Основной layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)
        
        # Заголовок
        self.title_label = QLabel("Редактировать элемент")
        self.title_label.setStyleSheet("""
            font: 18pt "Segoe UI";
            font-weight: 700;
            text-align: left;
            border: none;
            margin: 0px;
            padding: 0px;
        """)
        layout.addWidget(self.title_label)
        
        # Поле для ключа
        self.key_label = QLabel("Ключ:")
        self.key_label.setStyleSheet("""
            font: 12pt "Segoe UI";
            border: none;
        """)
        layout.addWidget(self.key_label)
        
        self.key_edit = QLineEdit()
        self.key_edit.setStyleSheet("""
            font: 14pt "Segoe UI";
            text-align: left;
            padding: 5px 12px;
            border: 1px solid #aaa;
            border-radius: 15px;
            background-color: #f2f2f2;
            color: black;
        """)
        self.key_edit.setText(phrase.key if phrase else "")
        layout.addWidget(self.key_edit)
        
        # Поле для текста
        self.text_label = QLabel("Текст:")
        self.text_label.setStyleSheet("""
            font: 12pt "Segoe UI";
            border: none;
        """)
        layout.addWidget(self.text_label)
        
        self.text_edit = QPlainTextEdit()
        self.text_edit.setStyleSheet("""
            font: 14pt "Segoe UI";
            text-align: left;
            border-radius: 20px;
            border: 1px solid #aaa;
            padding: 5px 12px;
            background-color: #f2f2f2;
        """)
        self.text_edit.setPlainText(phrase.text if phrase else "")
        layout.addWidget(self.text_edit)
        
        # Кнопки
        self.button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        self.button_box.setStyleSheet("""
            QPushButton {
                font: 12pt "Segoe UI";
                padding: 5px 15px;
                border-radius: 10px;
                min-width: 80px;
                outline: none;
            }
        """)
        
        # Применяем стили к конкретным кнопкам
        ok_button = self.button_box.button(QDialogButtonBox.StandardButton.Ok)
        ok_button.setStyleSheet("""
            QPushButton {
                background-color: #388E3C;
                color: white;
                border: 1px solid #2E7D32;
            }
            QPushButton:hover {
                background-color: #2E7D32;
            }
        """)
        
        cancel_button = self.button_box.button(QDialogButtonBox.StandardButton.Cancel)
        cancel_button.setStyleSheet("""
            QPushButton {
                background-color: #D32F2F;
                color: white;
                border: 1px solid #C62828;
            }
            QPushButton:hover {
                background-color: #C62828;
            }
        """)
        
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        layout.addWidget(self.button_box)
        
    def get_phrase(self):
        """Возвращает объект Phrase с данными из формы"""
        from models.phrase import Phrase
        return Phrase(
            key=self.key_edit.text(),
            text=self.text_edit.toPlainText()
        )
    
class EditValueDialog(QDialog):
    def __init__(self, parent=None, value:Value|None=None):
        super().__init__(parent)
        self.setWindowTitle("Редактировать параметр")
        
        self.setStyleSheet("""
            background-color: #f2f2f2;
            color: black;
        """)
        
        # Основной layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)
        
        # Заголовок
        self.title_label = QLabel("Редактировать элемент")
        self.title_label.setStyleSheet("""
            font: 18pt "Segoe UI";
            font-weight: 700;
            text-align: left;
            border: none;
            margin: 0px;
            padding: 0px;
        """)
        layout.addWidget(self.title_label)
        
        # Поле для ключа
        self.key_label = QLabel("Ключ:")
        self.key_label.setStyleSheet("""
            font: 12pt "Segoe UI";
            border: none;
        """)
        layout.addWidget(self.key_label)
        
        self.key_edit = QLineEdit()
        self.key_edit.setStyleSheet("""
            font: 14pt "Segoe UI";
            text-align: left;
            padding: 5px 12px;
            border: 1px solid #aaa;
            border-radius: 15px;
            background-color: #f2f2f2;
            color: black;
        """)
        self.key_edit.setText(value.key if value else "")
        layout.addWidget(self.key_edit)
        
        # Поле для текста
        self.text_label = QLabel("Текст:")
        self.text_label.setStyleSheet("""
            font: 12pt "Segoe UI";
            border: none;
        """)
        layout.addWidget(self.text_label)
        
        self.text_edit = QPlainTextEdit()
        self.text_edit.setStyleSheet("""
            font: 14pt "Segoe UI";
            text-align: left;
            border-radius: 20px;
            border: 1px solid #aaa;
            padding: 5px 12px;
            background-color: #f2f2f2;
        """)
        self.text_edit.setPlainText(value.text if value else "")
        layout.addWidget(self.text_edit)
        
        # Кнопки
        self.button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        self.button_box.setStyleSheet("""
            QPushButton {
                font: 12pt "Segoe UI";
                padding: 5px 15px;
                border-radius: 10px;
                min-width: 80px;
            }
        """)
        
        # Применяем стили к конкретным кнопкам
        ok_button = self.button_box.button(QDialogButtonBox.StandardButton.Ok)
        ok_button.setStyleSheet("""
            QPushButton {
                background-color: #388E3C;
                color: white;
                border: 1px solid #2E7D32;
            }
            QPushButton:hover {
                background-color: #2E7D32;
            }
        """)
        
        cancel_button = self.button_box.button(QDialogButtonBox.StandardButton.Cancel)
        cancel_button.setStyleSheet("""
            QPushButton {
                background-color: #D32F2F;
                color: white;
                border: 1px solid #C62828;
            }
            QPushButton:hover {
                background-color: #C62828;
            }
        """)
        
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        layout.addWidget(self.button_box)
    
    def get_value(self):
        """Возвращает объект Value с данными из формы"""
        return Value(
            key=self.key_edit.text(),
            text=self.text_edit.toPlainText()
        )