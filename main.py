from PyQt6.QtWidgets import QApplication
import sys

from views.main_window import MainWindow
# from models.matrix import Matrix
from controllers.main_controller import MainController
from storage.storage import Storage

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()

    storage = Storage()

    # Создаем Controller и передаем в него View и Model
    controller = MainController(main_window, storage)

    main_window.show()

    sys.exit(app.exec())