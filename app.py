import sys
from configparser import ConfigParser
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_main import Ui_MainWindow
from ui_logs import Ui_LogsWindow
from ui_settings_port import Ui_SettingsPortWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.initUI()
        # Создаём окно логов
        self.logs = LogsWindow(self)
        # Создаём окно настроек программы
        self.settings = SettingsPortWindow(self)
        # Нажатие на кнопку "Просмотр логов"
        self.btn_logs.clicked.connect(self.btn_logs_clicked)
        # Нажатие на кнопку "Настройки программы"
        self.tbtn_settings_port.clicked.connect(self.btn_settings_port_clicked)

    def initUI(self):
        self.show()

    # Показываем окно логов
    def btn_logs_clicked(self):
        self.logs.show()

    # Показываем окно настроек программы
    def btn_settings_port_clicked(self):
        self.settings.show()

 # Обработка закрытия главного окна
    def closeEvent(self, event):
        warr = QMessageBox(self)
        warr.setWindowTitle('Внимание!')
        warr.setText('<p><strong>В данный момент тестируется батарея!</strong></p> \
                     <p>Вы действительно хотите прервать тестирование и закрыть программу?</p>')
        warr.setIcon(warr.Icon.Warning)
        warr.addButton('Нет', warr.ButtonRole.NoRole)
        warr.addButton('  Закрыть программу  ', warr.ButtonRole.YesRole)
        warr.exec()
        button = warr.clickedButton().text()
        if button == '  Закрыть программу  ':
            event.accept()
        if button == 'Нет':
            event.ignore()


class LogsWindow(QMainWindow, Ui_LogsWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Нажатие на кнопку "Закрыть окно"
        self.btn_close.clicked.connect(self.btn_close_clicked)
    
    # Закрываем окно логов
    def btn_close_clicked(self):
        self.close()


class SettingsPortWindow(QMainWindow, Ui_SettingsPortWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Чтение настроек из ini-файла
        config = ConfigParser()
        config.read('settings.ini')
        if config.has_option('DEFAULT', 'PachLogsError'):
            print(config['DEFAULT']['PachLogsError'])############################


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec())
