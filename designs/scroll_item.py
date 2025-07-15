from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPlainTextEdit, QSizePolicy, QFrame
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from designs.edit_button import EditButton
from designs.delete_button import DeleteButton

class ScrollItem(QWidget):
    def __init__(self, title: str = "Title", description: str = "Описание...", parent:QWidget=None):
        super().__init__(parent)
        size = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        size.setHorizontalStretch(0)
        size.setVerticalStretch(0)
        size.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(size)

        self.widget = QWidget(parent=self)
        self.widget.setSizePolicy(size)

        self.widget.setStyleSheet("""
            border: 1px solid #bbb;
            border-radius: 20px;
            background: #eee;
        """)

        layout = QVBoxLayout(self.widget)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(6)

        # Верхняя строка с заголовком и кнопками
        top_layout = QHBoxLayout()
        top_layout.setContentsMargins(-1, -1, 12, -1)

        # Заголовок и его настройки
        self.title = QLabel(title, parent=self.widget)
        title_sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        title_sizePolicy.setHorizontalStretch(1)
        title_sizePolicy.setVerticalStretch(0)
        title_sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(title_sizePolicy)
        self.title.setStyleSheet("""
            border: none;
            font-size: 16px;
            font-weight: 600;
        """)
        top_layout.addWidget(self.title)

        button_sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        button_sizePolicy.setHorizontalStretch(0)
        button_sizePolicy.setVerticalStretch(0)
        

        # Кнопка редактирования
        self.edit_button = EditButton(parent=self.widget)
        self.edit_button.setIcon(QIcon("./designs/icons/edit.svg"))
        self.edit_button.setIconSize(QSize(16, 16))
        button_sizePolicy.setHeightForWidth(self.edit_button.sizePolicy().hasHeightForWidth())
        self.edit_button.setSizePolicy(button_sizePolicy)
        top_layout.addWidget(self.edit_button)

        #Кнопка удаления
        self.delete_button = DeleteButton(parent=self.widget)
        self.delete_button.setIcon(QIcon("./designs/icons/delete.svg"))
        self.delete_button.setIconSize(QSize(16, 16))
        button_sizePolicy.setHeightForWidth(self.delete_button.sizePolicy().hasHeightForWidth())
        self.delete_button.setSizePolicy(button_sizePolicy)
        top_layout.addWidget(self.delete_button)

        layout.addLayout(top_layout)

        # Разделительная линия
        self.line = QFrame(self)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line.setStyleSheet("background-color: #ccc;")
        layout.addWidget(self.line)

        # Описание
        self.description = QPlainTextEdit(description, parent=self.widget)
        self.description.setReadOnly(True)
        self.description.setStyleSheet("""
            border: none;
            font: 12pt "Segoe UI";
        """)
        layout.addWidget(self.description)

        self.scroll_layout = QVBoxLayout(self)
        self.scroll_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_layout.setSpacing(12)
        self.scroll_layout.addWidget(self.widget)

        # Сохраняем данные элемента
        self.key = title
        self.description_text = description

        # Подключаем кнопки к слотам
        self.edit_button.clicked.connect(self.on_edit_clicked)
        self.delete_button.clicked.connect(self.on_delete_clicked)

        # Callback-функции, которые будут установлены извне
        self.edit_callback = None
        self.delete_callback = None

    def set_callbacks(self, edit_callback, delete_callback):
        """Установка callback-функций для кнопок"""
        self.edit_callback = edit_callback
        self.delete_callback = delete_callback
    
    def on_edit_clicked(self):
        """Обработчик кнопки редактирования"""
        if self.edit_callback:
            self.edit_callback(self.key)
    
    def on_delete_clicked(self):
        """Обработчик кнопки удаления"""
        if self.delete_callback:
            self.delete_callback(self.key)
    
    