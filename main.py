from PyQt6.QtWidgets import QApplication
import sys

from views.main_window import MainWindow
from controllers.main_controller import MainController
from storage.storage import Storage

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()

    storage = Storage()

    # Создаем главный Controller и передаем в него View и Storage
    controller = MainController(main_window, storage)

    main_window.show()

    sys.exit(app.exec())