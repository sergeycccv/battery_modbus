'''
pyside6-uic ui/main.ui -o ui_main.py
pysyde6-designer

'''

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6 import QtCore
import sys
import ui_main, ui_settings


class MainApp(QMainWindow, ui_main.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.statusBar.showMessage('Ожидание подключения батарей...')

        # Нажатие на кнопку "Настройки"
        self.btn_settings.clicked.connect(self.btn_settings_clicked)

        # Нажатие на кнопку "Начать тестирование"
        self.btn_start_test.clicked.connect(self.btn_start_test_clicked)

    def btn_settings_clicked(self, checked):
        self.w = SettingsApp()
        self.w.show()


    # Обработка нажатия на кнопку "Начать тестирование"
    def btn_start_test_clicked(self):
        warr = QMessageBox(self)
        warr.setWindowTitle('Внимание!')
        warr.setText('Установите подключение к системе тестирования')
        warr.setIcon(QMessageBox.Warning)
        self.statusBar.showMessage('Ожидание подключения батарей...')
        warr.exec()
        # warr.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # button = warr.exec()
        # if button == QMessageBox.Ok:
        #     self.statusBar.showMessage('Ожидание подключения...')

class SettingsApp(QMainWindow, ui_settings.Ui_SettingsWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Оставить только кнопку закрытия окна
        self.setWindowFlags(self.windowFlags() & QtCore.Qt.CustomizeWindowHint)
        self.setWindowFlags(self.windowFlags() & QtCore.Qt.WindowCloseButtonHint)
        # self.setWindowFlags(self.windowFlags() & QtCore.Qt.WindowMaximizeButtonHint)



def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
