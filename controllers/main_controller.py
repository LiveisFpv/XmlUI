from views.main_window import MainWindow
import PyQt6.QtWidgets
from designs.select_button import SelectButton
from storage.storage import StorageInterface

class MainController:
    def __init__(self, view: MainWindow, storage:StorageInterface):
        self.__view = view
        self.__storage = storage
        self.__view.selector.selection_changed.connect(self.__on_selection_changed)
        self.__view.actionSave_as.triggered.connect(self.__save_to_file)
        self.__view.actionOpen.triggered.connect(self.__load_from_file)

    
    def __on_selection_changed(self, button:SelectButton|None):
        """Обработчик изменения выбора кнопки"""
        if button:
            if button.objectName() == "value_button":
                self.__show_values()
                print("Value button selected")
            elif button.objectName() == "phrases_button":
                self.__show_phrases()
                print("Phrases button selected")
            else:
                print(f"Selected button: {button.objectName()}")
        else:
            self.__no_selection()
            print("No button selected")

    def __no_selection(self):
        self.__hide_frame()
    
    def __show_phrases(self):
        """Показать фразы"""
        self.__show_frame()
        self.__storage.get_phrases()
        self.__view.frame_name.setText("Фразы")
        self.__view.frame_text.setText("Текстовые шаблоны с параметрами")


    def __show_values(self):
        """Показать параметры"""
        self.__show_frame()
        self.__storage.get_values()
        self.__view.frame_name.setText("Параметры")
        self.__view.frame_text.setText("Параметры с дефолтными значениями")

    def __hide_frame(self):
        """Скрыть текущий фрейм"""
        for i in range(self.__view.verticalLayout_2.count()):
            widget = self.__view.verticalLayout_2.itemAt(i).widget()
            if widget:
                widget.hide()

    def __show_frame(self):
        for i in range(self.__view.verticalLayout_2.count()):
            widget = self.__view.verticalLayout_2.itemAt(i).widget()
            if widget:
                widget.show()

    def __load_from_file(self):
        """Загрузить данные из файла"""
        filepath, _ = PyQt6.QtWidgets.QFileDialog.getOpenFileName(self.__view, "Открыть файл", "", "XML Files (*.xml);;All Files (*)")
        if filepath:
            error = self.__storage.load_data(filepath)
            if error:
                PyQt6.QtWidgets.QMessageBox.critical(self.__view, "Ошибка", f"Не удалось загрузить данные: {error}")
            else:
                self.__view.selector.clear_selection()
                self.__no_selection()
    
    def __save_to_file(self):
        """Сохранить данные в файл"""
        filepath, _ = PyQt6.QtWidgets.QFileDialog.getSaveFileName(self.__view, "Сохранить файл", "", "XML Files (*.xml);;All Files (*)")
        if filepath:
            error = self.__storage.save_data(filepath)
            if error:
                PyQt6.QtWidgets.QMessageBox.critical(self.__view, "Ошибка", f"Не удалось сохранить данные: {error}")
            else:
                PyQt6.QtWidgets.QMessageBox.information(self.__view, "Успех", "Данные успешно сохранены")
