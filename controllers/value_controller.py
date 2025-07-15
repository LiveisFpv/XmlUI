import PyQt6
from designs.scroll_item import ScrollItem
from views.main_window import MainWindow
from models.value import Value
from storage.storage import StorageInterface
from controllers.base_controller import BaseController
from designs.edit_dialog import EditValueDialog
from utils.validator import Validator

class ValueController(BaseController):
    def __init__ (self,view :MainWindow,storage:StorageInterface):
        super().__init__(view, storage)
    
    def show_values(self):
        """Показать параметры"""
        self._show_frame()
        self._view.frame_name.setText("Параметры")
        self._view.frame_text.setText("Параметры с дефолтными значениями")
        
        # Очищаем предыдущие элементы
        self._clear_scroll_area()

        # Получаем значения из хранилища
        values : list[Value]
        values, error = self._storage.get_values()
        if error:
            PyQt6.QtWidgets.QMessageBox.critical(self._view, "Ошибка", error)
            return
        
        for value in values:
            item = ScrollItem(
                value.key,
                description=value.text,
            )
            item.set_callbacks(
                edit_callback=self.handle_edit_value,
                delete_callback=self.handle_delete_value
            )
            self._view.scroll_layout.addWidget(item)
    
    def add_value(self, value: Value):
        error = self._storage.add_value(value)
        if error:
            PyQt6.QtWidgets.QMessageBox.critical(self._view, "Ошибка", error)
        else:
            self.show_values()
    
    def edit_value(self, old_key: str, new_value: Value):
        """Редактировать значение"""
        # Валидация ключа и текста
        if not Validator.ValueValidator.is_valid_key(new_value.key):
            PyQt6.QtWidgets.QMessageBox.warning(self._view, "Ошибка", "Ключ должен содержать только буквы, цифры и символы подчеркивания")
            return
        if not Validator.ValueValidator.is_valid_text(new_value.text):
            PyQt6.QtWidgets.QMessageBox.warning(self._view, "Ошибка", "Текст не должен содержать специальные символы")
            return
        error = self._storage.edit_value(old_key, new_value)
        if error:
            PyQt6.QtWidgets.QMessageBox.critical(self._view, "Ошибка", error)
        else:
            self.show_values()
    
    def delete_value(self, key: str):
        """Удалить значение"""
        error = self._storage.delete_value(key)
        if error:
            PyQt6.QtWidgets.QMessageBox.critical(self._view, "Ошибка", error)
        else:
            self.show_values()
    
    def handle_edit_value(self, key: str):
        """Обработчик редактирования значения"""
        value, error = self._storage.get_value_by_key(key)
        if error:
            PyQt6.QtWidgets.QMessageBox.critical(self._view, "Ошибка", error)
            return
        if not value:
            return
        
        dialog = EditValueDialog(self._view, value)
        if dialog.exec():
            new_value = dialog.get_value()
            self.edit_value(key, new_value)
    
    def handle_delete_value(self, key: str):
        """Обработчик удаления значения"""
        reply = PyQt6.QtWidgets.QMessageBox.question(
            self._view, 
            "Подтверждение", 
            f"Вы уверены, что хотите удалить фразу '{key}'?",
            PyQt6.QtWidgets.QMessageBox.StandardButton.Yes | PyQt6.QtWidgets.QMessageBox.StandardButton.No
        )

        if reply == PyQt6.QtWidgets.QMessageBox.StandardButton.Yes:
            self.delete_value(key)
        else:
            PyQt6.QtWidgets.QMessageBox.information(self._view, "Отмена", "Удаление отменено")