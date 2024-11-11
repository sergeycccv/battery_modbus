import sys
from configparser import ConfigParser
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit
from ui_main import Ui_MainWindow
from ui_logs import Ui_LogsWindow
from ui_settings_port import Ui_SettingsPortWindow
from ui_alert import Ui_AlertsWindow
from ui_settings_ch import Ui_SettingsChWindow



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.initUI()
        # Создаём окно логов
        self.logs = LogsWindow(self)
        # Создаём окно настроек программы
        self.settings = SettingsPortWindow(self)
        # Создаём окно просмотра лога программы
        self.alerts = AlertsWindow(self)
        # Создаём окно настроек канала
        self.settings_ch = SettingsChWindow(self)
        # Нажатие на кнопку "Просмотр логов"
        self.btn_logs.clicked.connect(self.btn_logs_clicked)
        # Нажатие на кнопку "Настройки программы"
        self.tbtn_settings_port.clicked.connect(self.btn_settings_port_clicked)
        # Нажатие на кнопку "Лог работы программы"
        self.btn_alerts.clicked.connect(self.btn_alerts_clicked)
        # Нажатие на кнопку "Настройки канала"
        self.tbtn_settings_ch_1.clicked.connect(self.btn_settings_ch_clicked)

    def initUI(self):
        for widget in self.findChildren(QLineEdit):
            if widget.property('channel') in {'ch1', 'ch2', 'ch3', 'ch4'}:
                widget.setText('00,000')
                if widget.objectName() == 'edit_1_Ustart':
                    widget.setProperty('styleSheet', 'color: rgb(200, 200, 200); background-color: black;')
                if widget.objectName() == 'edit_1_Ucurrent':
                    widget.setProperty('styleSheet', 'color: rgb(0, 255, 30); background-color: black;')
                if widget.objectName() == 'edit_1_Icurrent':
                    widget.setProperty('styleSheet', 'color: rgb(0, 255, 30); background-color: black;')
                if widget.objectName() == 'edit_1_Pcurrent':
                    widget.setProperty('styleSheet', 'color: rgb(0, 255, 30); background-color: black;')
                if widget.objectName() == 'edit_1_Crecharge':
                    widget.setProperty('styleSheet', 'color: rgb(200, 200, 200); background-color: black;')
                if widget.objectName() == 'edit_1_Wrecharge':
                    widget.setProperty('styleSheet', 'color: rgb(200, 200, 200); background-color: black;')
                if widget.objectName() == 'edit_1_Cdischarge':
                    widget.setProperty('styleSheet', 'color: rgb(255, 140, 140); background-color: black;')
                if widget.objectName() == 'edit_1_Wdischarge':
                    widget.setProperty('styleSheet', 'color: rgb(255, 140, 140); background-color: black;')
                if widget.objectName() == 'edit_1_Ccharge':
                    widget.setProperty('styleSheet', 'color: rgb(0, 255, 30); background-color: black;')
                if widget.objectName() == 'edit_1_Wcharge':
                    widget.setProperty('styleSheet', 'color: rgb(0, 255, 30); background-color: black;')
        self.show()

    # Показываем окно логов
    def btn_logs_clicked(self):
        self.logs.show()

    # Показываем окно настроек программы
    def btn_settings_port_clicked(self):
        self.settings.show()

    # Показываем окно просмотра лога программы
    def btn_alerts_clicked(self):
        self.alerts.show()

    # Показываем окно настроек канала
    def btn_settings_ch_clicked(self):
        self.settings_ch.show()


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
            # print(config['DEFAULT']['PachLogsError'])
            pass


class AlertsWindow(QMainWindow, Ui_AlertsWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class SettingsChWindow(QMainWindow, Ui_SettingsChWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec())
