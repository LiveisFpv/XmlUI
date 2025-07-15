from views.main_window import MainWindow
from storage.storage import StorageInterface
class BaseController:
    """
    Base controller class that provides common functionality for all controllers.
    """

    def __init__(self, view: MainWindow, storage:StorageInterface):
        self._view = view
        self._storage = storage
    
    def _clear_scroll_area(self):
        """Очищает scroll area от всех элементов"""
        # Удаляем все виджеты из scroll_layout
        while self._view.scroll_layout.count():
            child = self._view.scroll_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
    
    def _hide_frame(self):
        """Скрыть текущий фрейм"""
        for i in range(self._view.verticalLayout_2.count()):
            widget = self._view.verticalLayout_2.itemAt(i).widget()
            if widget:
                widget.hide()
        

    def _show_frame(self):
        for i in range(self._view.verticalLayout_2.count()):
            widget = self._view.verticalLayout_2.itemAt(i).widget()
            if widget:
                widget.show()