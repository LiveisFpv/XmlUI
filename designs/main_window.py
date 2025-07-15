from PyQt6 import QtCore, QtGui, QtWidgets
from designs.select_button import SelectButton
from designs.submit_button import SubmitButton
from designs.edit_button import EditButton
from designs.delete_button import DeleteButton
from designs.scroll_item import ScrollItem


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(969, 809)
        MainWindow.setStyleSheet("background-color: #eee;\n"
"color: black;\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.actions = QtWidgets.QWidget(parent=self.centralwidget)
        self.actions.setStyleSheet("padding: 10px 12px;\n"
"background: #f2f2f2;\n"
"border-top-left-radius: 32px;\n"
"border-top-right-radius: 32px;\n"
"border: 1px solid #ddd;")
        self.actions.setObjectName("actions")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.actions)
        self.verticalLayout_3.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_3.setSpacing(12)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.value_button = SelectButton(parent=self.actions)
        self.value_button.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)

        self.value_button.setCheckable(True)
        self.value_button.setObjectName("value_button")
        self.verticalLayout_3.addWidget(self.value_button)
        self.phrases_button = SelectButton(parent=self.actions)
        self.phrases_button.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        
        self.phrases_button.setCheckable(True)
        self.phrases_button.setChecked(True)
        self.phrases_button.setObjectName("phrases_button")
        self.verticalLayout_3.addWidget(self.phrases_button)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout.addWidget(self.actions)
        self.new_window = QtWidgets.QWidget(parent=self.centralwidget)
        self.new_window.setStyleSheet("padding: 10px 12px;\n"
"background: #f2f2f2;\n"
"border-bottom-left-radius: 32px;\n"
"border-bottom-right-radius: 32px;\n"
"border: 1px solid #ddd;\n"
"border-top: none;")
        self.new_window.setObjectName("new_window")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.new_window)
        self.verticalLayout_4.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.add_new = QtWidgets.QLabel(parent=self.new_window)
        self.add_new.setStyleSheet("font: 18pt \"Segoe UI\";\n"
"font-weight: 700;\n"
"text-align: left;\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;")
        self.add_new.setObjectName("add_new")
        self.verticalLayout_4.addWidget(self.add_new)
        self.key_field = QtWidgets.QLineEdit(parent=self.new_window)
        self.key_field.setStyleSheet("font: 14pt \"Segoe UI\";\n"
"text-align: left;\n"
"padding: 5px 12px;\n"
"border: 1px solid #aaa;\n"
"border-radius: 15px;\n"
"background-color: #f2f2f2;\n"
"color: black;")
        self.key_field.setText("")
        self.key_field.setObjectName("key_field")
        self.verticalLayout_4.addWidget(self.key_field)
        self.text_field = QtWidgets.QPlainTextEdit(parent=self.new_window)
        self.text_field.setMaximumSize(QtCore.QSize(16777215, 125))
        self.text_field.setStyleSheet("font: 14pt \"Segoe UI\";\n"
"text-align: left;\n"
"border-radius: 20px;\n"
"border: 1px solid #aaa;\n"
"padding: 5px 12px;")
        self.text_field.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.text_field.setObjectName("text_field")
        self.verticalLayout_4.addWidget(self.text_field)
        self.add_button = SubmitButton(parent=self.new_window)

        self.add_button.setObjectName("add_button")
        self.verticalLayout_4.addWidget(self.add_button)
        self.verticalLayout.addWidget(self.new_window)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout_7.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.selected_frame = QtWidgets.QWidget(parent=self.centralwidget)
        self.selected_frame.setStyleSheet("padding: 10px 12px;\n"
"background: #f2f2f2;\n"
"border-top-left-radius: 32px;\n"
"border-top-right-radius: 32px;\n"
"border: 1px solid #ddd;")
        self.selected_frame.setObjectName("selected_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.selected_frame)
        self.horizontalLayout_2.setContentsMargins(16, 16, 16, 16)
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_name = QtWidgets.QLabel(parent=self.selected_frame)
        self.frame_name.setStyleSheet("font: 18pt \"Segoe UI\";\n"
"font-weight: 700;\n"
"text-align: left;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"border: none")
        self.frame_name.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.frame_name.setObjectName("frame_name")
        self.horizontalLayout_2.addWidget(self.frame_name)
        self.frame_text = QtWidgets.QLabel(parent=self.selected_frame)
        self.frame_text.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.frame_text.setStyleSheet("font: 11pt \"Segoe UI\";\n"
"font-weight: 400;\n"
"text-align: right;\n"
"color: #444;\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px")
        self.frame_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.frame_text.setObjectName("frame_text")
        self.horizontalLayout_2.addWidget(self.frame_text)
        self.verticalLayout_2.addWidget(self.selected_frame)
        self.frame_values = QtWidgets.QWidget(parent=self.centralwidget)
        self.frame_values.setStyleSheet("padding: 10px 12px;\n"
"background: #f2f2f2;\n"
"border-bottom-left-radius: 32px;\n"
"border-bottom-right-radius: 32px;\n"
"border: 1px solid #ddd;\n"
"border-top: none;")
        self.frame_values.setObjectName("frame_values")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_values)
        self.verticalLayout_6.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_6.setSpacing(12)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.search_frane = QtWidgets.QWidget(parent=self.frame_values)
        self.search_frane.setStyleSheet("border: none;")
        self.search_frane.setObjectName("search_frane")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.search_frane)
        self.horizontalLayout_3.setContentsMargins(8, 0, 8, 0)
        self.horizontalLayout_3.setSpacing(12)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.search_field = QtWidgets.QLineEdit(parent=self.search_frane)
        self.search_field.setStyleSheet("font: 12pt \"Segoe UI\";\n"
"text-align: left;\n"
"padding: 5px 6px;\n"
"border: 1px solid #aaa;\n"
"border-radius: 10px;\n"
"background-color: #f2f2f2;\n"
"color: black;")
        self.search_field.setObjectName("search_field")
        self.horizontalLayout_3.addWidget(self.search_field)
        self.search_button = SubmitButton(parent=self.search_frane)

        self.search_button.setObjectName("search_button")
        self.horizontalLayout_3.addWidget(self.search_button)
        self.verticalLayout_6.addWidget(self.search_frane)
        self.scrollArea = QtWidgets.QScrollArea(parent=self.frame_values)
        self.scrollArea.setStyleSheet("border: none;\n"
"margin: 0px;\n"
"padding: 8px;\n"
"background: #f2f2f2;")
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setStyleSheet("")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        # self.widget = ScrollItem(parent=self.scrollAreaWidgetContents)

        self.scroll_layout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.scroll_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_layout.setSpacing(12)
        # self.scroll_layout.addWidget(self.widget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_6.addWidget(self.scrollArea)
        self.verticalLayout_2.addWidget(self.frame_values)
        self.verticalLayout_2.setStretch(1, 9)
        self.verticalLayout_7.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 969, 33))
        self.menubar.setStyleSheet("margin: 0px;\n"
"padding: 0px;\n"
"text-align: center;\n"
"font-size: 11px;")
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setStyleSheet("margin: 0px;\n"
"padding: 0px;\n"
"text-align: center;\n"
"font-size: 11px;")
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtGui.QAction(parent=MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(parent=MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtGui.QAction(parent=MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionNew_file = QtGui.QAction(parent=MainWindow)
        self.actionNew_file.setMenuRole(QtGui.QAction.MenuRole.TextHeuristicRole)
        self.actionNew_file.setIconVisibleInMenu(True)
        self.actionNew_file.setShortcutVisibleInContextMenu(True)
        self.actionNew_file.setObjectName("actionNew_file")
        self.menuFile.addAction(self.actionNew_file)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.setStyleSheet("""
            QMenu {
                background-color: #f2f2f2;
                border: 1px solid #ddd;
                border-radius: 10px;
                padding: 8px;
                font-size: 13px;
            }
            QMenu::item {
                padding: 6px 24px;
                padding-left: 12px;
                background-color: transparent;
                color: #222;
            }
            QMenu::item:selected {
                background-color: #e0e0e0;
                color: #0078d7;
                border-radius: 6px;
            }
        """)
        self.menubar.setStyleSheet("""
            QMenuBar {
                margin: 0px;
                padding: 0px;
                text-align: center;
                font-size: 11px;
                background: #eee;
            }
            QMenuBar::item {
                background: transparent;
                color: #222;
                padding: 6px 24px;
                border-radius: 6px;
            }
            QMenuBar::item:selected {
                background: #e0e0e0;
                color: #0078d7;
            }
        """)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.value_button.setText(_translate("MainWindow", "Значения"))
        self.phrases_button.setText(_translate("MainWindow", "Фразы"))
        self.add_new.setText(_translate("MainWindow", "Добавить новый элемент"))
        self.key_field.setPlaceholderText(_translate("MainWindow", "Ключ"))
        self.text_field.setPlaceholderText(_translate("MainWindow", "Значение"))
        self.add_button.setText(_translate("MainWindow", "Добавить"))
        self.frame_name.setText(_translate("MainWindow", "Фразы"))
        self.frame_text.setText(_translate("MainWindow", "Текстовые шаблоны с параметрами"))
        self.search_field.setPlaceholderText(_translate("MainWindow", "Начните писать..."))
        self.search_button.setText(_translate("MainWindow", "Найти"))
        self.menuFile.setTitle(_translate("MainWindow", "Файл"))
        self.actionOpen.setText(_translate("MainWindow", "Открыть файл"))
        self.actionSave.setText(_translate("MainWindow", "Сохранить"))
        self.actionSave_as.setText(_translate("MainWindow", "Сохранить как"))
        self.actionNew_file.setText(_translate("MainWindow", "Новый файл"))
