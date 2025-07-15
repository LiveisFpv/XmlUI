from views.main_window import MainWindow
import PyQt6.QtWidgets
from designs.select_button import SelectButton
from storage.storage import StorageInterface
from designs.scroll_item import ScrollItem
from models.value import Value
from models.phrase import Phrase
from controllers.phrase_controller import PhraseController
from controllers.value_controller import ValueController
from controllers.base_controller import BaseController
from utils.validator import Validator

class MainController(BaseController):
    def __init__(self, view: MainWindow, storage:StorageInterface):
        super().__init__(view, storage)
        self.__loaded_filepath = None
        self.__phraseController = PhraseController(view,storage)
        self.__valueController = ValueController(view,storage)
        self._view.selector.selection_changed.connect(self.__on_selection_changed)
        self._view.actionSave_as.triggered.connect(lambda: self.__save_to_file(None))
        self._view.actionSave.triggered.connect(lambda: self.__save_to_file(self.__loaded_filepath))
        self._view.actionOpen.triggered.connect(self.__load_from_file)
        self._view.add_button.clicked.connect(self.__add_rec)
        self._view.search_button.clicked.connect(lambda: self.__on_search(self._view.selector.get_selected()))

    
    def __on_selection_changed(self, button:SelectButton|None):
        """Обработчик изменения выбора кнопки"""
        if button:
            if button.objectName() == "value_button":
                self.__valueController.show_values()
                print("Value button selected")
            elif button.objectName() == "phrases_button":
                self.__phraseController.show_phrases()
                print("Phrases button selected")
            else:
                print(f"Selected button: {button.objectName()}")
        else:
            self.__no_selection()
            print("No button selected")

    def __on_search(self, button:SelectButton|None):
        """Обработчик поиска"""
        search_text = self._view.search_field.text().strip()
        if not search_text:
            PyQt6.QtWidgets.QMessageBox.warning(self._view, "Ошибка", "Поле поиска не может быть пустым")
            return
        
        if button.objectName() == "value_button":
            self.__valueController.show_values(search_text)
        elif button.objectName() == "phrases_button":
            self.__phraseController.show_phrases(search_text)
        else:
            PyQt6.QtWidgets.QMessageBox.warning(self._view, "Ошибка", "Выберите категорию для поиска")

    def __no_selection(self):
        self._hide_frame()


    def __load_from_file(self):
        """Загрузить данные из файла"""
        filepath, _ = PyQt6.QtWidgets.QFileDialog.getOpenFileName(self._view, "Открыть файл", "", "XML Files (*.xml);;All Files (*)")
        if filepath:
            error = self._storage.load_data(filepath)
            if error:
                PyQt6.QtWidgets.QMessageBox.critical(self._view, "Ошибка", f"Не удалось загрузить данные: {error}")
            else:
                self.__on_selection_changed(self._view.selector.get_selected())
                self.__loaded_filepath = filepath
    
    def __save_to_file(self,filepath: str | None):
        """Сохранить данные в файл"""
        if not filepath:
            filepath, _ = PyQt6.QtWidgets.QFileDialog.getSaveFileName(self._view, "Сохранить файл", "", "XML Files (*.xml);;All Files (*)")
        if filepath:
            error = self._storage.save_data(filepath)
            if error:
                PyQt6.QtWidgets.QMessageBox.critical(self._view, "Ошибка", f"Не удалось сохранить данные: {error}")
            else:
                PyQt6.QtWidgets.QMessageBox.information(self._view, "Успех", "Данные успешно сохранены")
                self.__loaded_filepath = filepath

    def __add_rec(self):
        """Добавить запись"""
        key = self._view.key_field.text().strip()
        if not key:
            PyQt6.QtWidgets.QMessageBox.warning(self._view, "Ошибка", "Ключ не может быть пустым")
            return
        text = self._view.text_field.toPlainText().strip()
        if not text:
            PyQt6.QtWidgets.QMessageBox.warning(self._view, "Ошибка", "Текст не может быть пустым")
            return
        button = self._view.selector.get_selected()
        if button.objectName() == "value_button":
            if not Validator.ValueValidator.is_valid_key(key):
                PyQt6.QtWidgets.QMessageBox.warning(self._view, "Ошибка", "Ключ должен содержать только буквы, цифры и символы подчеркивания")
                return
            if not Validator.ValueValidator.is_valid_text(text):
                PyQt6.QtWidgets.QMessageBox.warning(self._view, "Ошибка", "Текст не должен содержать специальные символы")
                return
            value = Value(key, text)
            self.__valueController.add_value(value)
        elif button.objectName() == "phrases_button":
            if not Validator.PhraseValidator.is_valid_key(key):
                PyQt6.QtWidgets.QMessageBox.warning(self._view, "Ошибка", "Ключ должен содержать только буквы, цифры и символы подчеркивания")
                return
            if not Validator.PhraseValidator.is_valid_text(text):
                PyQt6.QtWidgets.QMessageBox.warning(self._view, "Ошибка", "Текст не должен содержать символы &, [, ]")
                return
            self.__phraseController.add_phrase(key, text)
        else:
            PyQt6.QtWidgets.QMessageBox.warning(self._view, "Ошибка", "Выберите категорию для добавления записи")