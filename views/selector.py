from designs.select_button import SelectButton
from PyQt6.QtCore import QObject, pyqtSignal

class Selector(QObject):
    """Селектор кнопок, позволяющий выбрать только одну кнопку из списка"""
    selection_changed = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        self.__selected : SelectButton  = None
        self.__select_buttons : list[SelectButton] = []
    
    def add_select_button(self, button: SelectButton, selected: bool = False):
        """Добавляет кнопку в селектор"""
        self.__select_buttons.append(button)
        button.setChecked(selected)
        if selected:
            if self.__selected is not None and self.__selected != button:
                self.__selected.setChecked(False)
            self.__selected = button
            self.selection_changed.emit(button)  
        
        button.clicked.connect(self.__on_button_clicked)
    
    def __on_button_clicked(self):
        """Обработчик нажатия на кнопку"""
        button = self.sender()
        if button.isChecked():
            if self.__selected is not None and self.__selected != button:
                self.__selected.setChecked(False)
            self.__selected = button
        else:
            self.__selected = None

        self.selection_changed.emit(self.__selected)
    
    def get_selected(self) -> SelectButton:
        """Возвращает выбранную кнопку"""
        return self.__selected
    
    def get_select_buttons(self) -> list[SelectButton]:
        """Возвращает список всех кнопок селектора"""
        return self.__select_buttons
    
    def clear_selection(self):
        """Сброс текущего выбора"""
        if self.__selected:
            self.__selected.setChecked(False)
        self.__selected = None
        self.selection_changed.emit(None)