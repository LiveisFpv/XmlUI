import PyQt6
from designs.scroll_item import ScrollItem
from views.main_window import MainWindow
from models.phrase import Phrase
from storage.storage import StorageInterface
from controllers.base_controller import BaseController
from designs.edit_dialog import EditPhraseDialog
from utils.validator import Validator

class PhraseController(BaseController):
    def __init__ (self,view :MainWindow,storage:StorageInterface):
        super().__init__(view, storage)
    
    def show_phrases(self):
        """Показать фразы"""
        self._show_frame()
        self._view.frame_name.setText("Фразы")
        self._view.frame_text.setText("Текстовые шаблоны с параметрами")

        # Очищаем предыдущие элементы
        self._clear_scroll_area()

        # Получаем фразы из хранилища
        phrases : list[Phrase]
        phrases, error = self._storage.get_phrases()
        if error:
            PyQt6.QtWidgets.QMessageBox.critical(self._view, "Ошибка", error)
            return
        
        for phrase in phrases:
            item = ScrollItem(
                phrase.key,
                description=phrase.text,
            )

            item.set_callbacks(
                edit_callback=self.handle_edit_phrase,
                delete_callback=self.handle_delete_phrase
            )

            self._view.scroll_layout.addWidget(item)
    
    def add_phrase(self, key: str, text: str):
        phrase = Phrase(key, text, [])
        error = self._storage.add_phrase(phrase)
        if error:
            PyQt6.QtWidgets.QMessageBox.critical(self._view, "Ошибка", error)
        else:
            self.show_phrases()

    def edit_phrase(self, old_key: str, new_phrase: Phrase):
        """Редактировать фразу"""
        # Валидация ключа и текста
        if not Validator.PhraseValidator.is_valid_key(new_phrase.key):
            PyQt6.QtWidgets.QMessageBox.warning(self._view, "Ошибка", "Ключ должен содержать только буквы, цифры и символы подчеркивания")
            return
        if not Validator.PhraseValidator.is_valid_text(new_phrase.text):
            PyQt6.QtWidgets.QMessageBox.warning(self._view, "Ошибка", "Текст не должен содержать символы &, [, ]")
            return
        error = self._storage.edit_phrase(old_key, new_phrase)
        if error:
            PyQt6.QtWidgets.QMessageBox.critical(self._view, "Ошибка", error)
        else:
            self.show_phrases()
    
    def delete_phrase(self, key: str):
        """Удалить фразу"""
        error = self._storage.delete_phrase(key)
        if error:
            PyQt6.QtWidgets.QMessageBox.critical(self._view, "Ошибка", error)
        else:
            self.show_phrases()
        
    def handle_edit_phrase(self, key: str):
        """Обработчик редактирования фразы"""
        # Получаем текущую фразу
        phrase, error = self._storage.get_phrase_by_key(key)
        if error:
            PyQt6.QtWidgets.QMessageBox.critical(self._view, "Ошибка", error)
            return
        
        if not phrase:
            return
        
        # Диалог редактирования
        dialog = EditPhraseDialog(self._view, phrase)
        if dialog.exec():
            new_phrase = dialog.get_phrase()
            self.edit_phrase(key, new_phrase)

    def handle_delete_phrase(self, key: str):
        """Обработчик удаления фразы"""
        # Запрашиваем подтверждение
        reply = PyQt6.QtWidgets.QMessageBox.question(
            self._view, 
            "Подтверждение", 
            f"Вы уверены, что хотите удалить фразу '{key}'?",
            PyQt6.QtWidgets.QMessageBox.StandardButton.Yes | PyQt6.QtWidgets.QMessageBox.StandardButton.No
        )
        
        if reply == PyQt6.QtWidgets.QMessageBox.StandardButton.Yes:
            self.delete_phrase(key)
        else:
            PyQt6.QtWidgets.QMessageBox.information(self._view, "Отмена", "Удаление фразы отменено")
