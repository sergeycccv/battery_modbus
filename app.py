import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow
from ui_logs import Ui_LogsWindow
from ui_settings import Ui_SettingsWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.initUI()
        
        # Создаём окно логов
        self.logs = LogsWindow(self)
        # Создаём окно настроек программы
        self.settings = SettingsWindow(self)

        # Нажатие на кнопку "Просмотр логов"
        self.btn_logs.clicked.connect(self.btn_logs_clicked)
        # Нажатие на кнопку "Настройки программы"
        self.tbtn_settings.clicked.connect(self.btn_settings_clicked)

    def initUI(self):
        self.show()

    # Показываем окно логов
    def btn_logs_clicked(self):
        self.logs.show()

    # Показываем окно настроек программы
    def btn_settings_clicked(self):
        self.settings.show()


class LogsWindow(QMainWindow, Ui_LogsWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Нажатие на кнопку "Закрыть окно"
        self.btn_close.clicked.connect(self.btn_close_clicked)
    
    # Закрываем окно логов
    def btn_close_clicked(self):
        self.close()


class SettingsWindow(QMainWindow, Ui_SettingsWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec())
