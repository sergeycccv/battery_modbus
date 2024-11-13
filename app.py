import sys, os, serial, glob
from configparser import ConfigParser
from PySide6.QtWidgets import (QApplication, QMainWindow, 
    QMessageBox, QLineEdit, QPushButton)
from ui_main import Ui_MainWindow
from ui_logs import Ui_LogsWindow
from ui_settings_port import Ui_SettingsPortWindow
from ui_alert import Ui_AlertsWindow
from ui_settings_ch import Ui_SettingsChWindow

from PySide6.QtCore import QTimer


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.initUI()

        self.path_logs = ''
        self.port = 'COM1'
        self.baudrate = 9600
        self.bytesize = 8
        self.parity = 'N' # N - None, E - Even, O - Odd
        self.stopbits = 1
        self.xonxoff = False

        # Список COM-портов
        self.list_com_saved = []
        # Создаём список COM-портов
        self.list_com_update()

        # Таймер обновления списка COM-портов
        self.timer_upd_com_list = QTimer()

        # Создаём окно логов
        self.logs = LogsWindow(self)
        # Создаём окно настроек программы
        self.settings = SettingsPortWindow(self)
        # Создаём окно просмотра лога программы
        self.alerts = AlertsWindow(self)
        # Создаём окно настроек канала
        self.settings_ch = SettingsChWindow(self)
        
        # Получаем настройки из ini-файла
        self.get_settings_ini_file()


        # Изменение текущего COM-порта в списке
        self.list_com.currentIndexChanged.connect(self.list_com_changed)
        # Обновления списка COM-портов по таймеру
        self.timer_upd_com_list.timeout.connect(self.list_com_update)
        # Нажатие на кнопку "Подключиться"
        self.btn_connect.clicked.connect(self.btn_connect_clicked)
        # Нажатие на кнопку "Настройки порта"
        self.tbtn_settings_port.clicked.connect(self.btn_settings_port_clicked)
        # Нажатие на кнопку "Лог работы программы"
        self.btn_alerts.clicked.connect(self.btn_alerts_clicked)
        # Нажатие на кнопку "Просмотр логов"
        self.btn_logs.clicked.connect(self.btn_logs_clicked)
        # Нажатие на кнопку "Настройки канала"
        self.tbtn_settings_ch_1.clicked.connect(self.btn_settings_ch_clicked)

        # Старт таймера обновления списка COM-портов (1 секунда)
        self.timer_upd_com_list.start(1000)

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

    # Изменение текущего COM-порта в списке
    def list_com_changed(self):
        self.port = self.list_com.currentText()

    # Обновление списка COM-портов по таймеру
    def list_com_update(self):
        try:
            # Если список COM-портов изменился или пустой
            if (self.list_com_saved != serial_ports()) or (len(self.list_com_saved) == 0):
                # Очищаем список
                self.list_com.clear()
                # Обновляем список COM-портов
                self.list_com.addItems(serial_ports())
                self.port = self.list_com.currentText()
                # Сохраняем список COM-портов
                self.list_com_saved = serial_ports()
        except Exception as e:
            QMessageBox.warning(self, 'Предупреждение', 'В системе нет ни одного свободного COM-порта\n' + str(e))
            self.list_com.setCurrentIndex(-1)
            self.port = ''

    # Подключение к COM-порту
    def btn_connect_clicked(self):
        try:
            self.serial = serial.Serial(self.port, self.baudrate, self.bytesize, self.parity, self.stopbits, self.xonxoff)
        except serial.SerialException as e:
            QMessageBox.warning(self, 'Предупреждение', 'Ошибка подключения к COM-порту\n' + str(e))

    # Показываем окно логов
    def btn_logs_clicked(self):
        self.logs.show()

    # Показываем окно настроек порта
    def btn_settings_port_clicked(self):
        self.settings.show()

    # Показываем окно просмотра лога программы
    def btn_alerts_clicked(self):
        self.alerts.show()

    # Показываем окно настроек канала
    def btn_settings_ch_clicked(self):
        self.settings_ch.show()

    # Чтение настроек из ini-файла
    def get_settings_ini_file(self):
        try:
            config = ConfigParser()
            config.read('settings.ini')
            
            if config.has_option('DEFAULT', 'PathLogs'):
                self.path_logs = config.get('DEFAULT', 'PathLogs')
                self.logs.line_path_logs.setText(self.path_logs)
            else:
                self.path_logs = os.path.abspath(os.curdir)
                self.logs.line_path_logs.setText(self.path_logs)
            
            if config.has_option('COM', 'Port'):
                self.port = config.get('COM', 'Port')
                item = self.list_com.findText(self.port)
                # Если порт из ini-файла существует в списке, а значит и в системе
                if  item != -1:
                    self.list_com.setCurrentIndex(item)
                else:
                    # Иначе выбираем первый из списка
                    self.list_com.setCurrentIndex(0)
                    self.port = self.list_com.currentText()
            else:
                self.list_com.setCurrentIndex(0)
                self.port = self.list_com.currentText()

            if config.has_option('COM', 'BaudRate'):
                self.baudrate = config.getint('COM', 'BaudRate')
                self.settings.edit_buadrate.setText(str(self.baudrate))
            else:
                self.baudrate = 9600
                self.settings.edit_buadrate.setText('9600')

            if config.has_option('COM', 'ByteSize'):
                self.bytesize = config.getint('COM', 'ByteSize')
                self.settings.edit_bytesize.setText(str(self.bytesize))
            else:
                self.bytesize = 8
                self.settings.edit_bytesize.setText('8')

            if config.has_option('COM', 'Parity'):
                parity = {'N': 0, 'E': 1, 'O': 2}
                self.parity = config.get('COM', 'Parity')
                self.settings.cb_parity.setCurrentIndex(parity.get(self.parity))
            else:
                self.parity = 'N'
                self.settings.cb_parity.setCurrentIndex(0)

            if config.has_option('COM', 'StopBits'):
                self.stopbits = config.getint('COM', 'StopBits')
                self.settings.edit_stopbits.setText(str(self.stopbits))
            else:
                self.stopbits = 1
                self.settings.edit_stopbits.setText('1')
            
            if config.has_option('COM', 'XOnXOff'):
                self.xonxoff = config.getboolean('COM', 'XOnXOff')
                self.settings.cb_xonxoff.setChecked(self.xonxoff)
            else:
                self.xonxoff = False
                self.settings.cb_xonxoff.setChecked(False)

        except Exception as e:
            QMessageBox.warning(self, 'Предупреждение', 'Ошибка чтения настроек из ini-файла:\n' + str(e))

    # Запись настроек в ini-файл
    def set_settings_ini_file(self):
        try:
            config = ConfigParser()
            config.add_section('GENERAL')
            config.set('GENERAL', 'PathLogs', win.path_logs)
            config.add_section('COM')
            config.set('COM', 'Port', win.port)
            config.set('COM', 'BaudRate', str(win.baudrate))
            config.set('COM', 'ByteSize', str(win.bytesize))
            config.set('COM', 'Parity', win.parity)
            config.set('COM', 'StopBits', str(win.stopbits))
            config.set('COM', 'XOnXOff', str(win.xonxoff))
            with open('settings.ini', 'w') as configfile:
                config.write(configfile)
        except Exception as e:
            QMessageBox.warning(self, 'Предупреждение', 'Ошибка записи настроек в ini-файл:\n' + str(e))

 # Обработка закрытия главного окна
    def closeEvent(self, event):
        exit_alert = QMessageBox(self)
        exit_alert.setWindowTitle('Внимание!')
        exit_alert.setText('<p><strong>В данный момент тестируется батарея!</strong></p> \
                     <p>Вы действительно хотите прервать тестирование и закрыть программу?</p>')
        exit_alert.setIcon(exit_alert.Icon.Warning)
        yes_close_btn = QPushButton('  Закрыть программу  ')
        no_close_btn = QPushButton('Нет')
        exit_alert.addButton(yes_close_btn, exit_alert.ButtonRole.ActionRole)
        exit_alert.addButton(no_close_btn, exit_alert.ButtonRole.ActionRole)
        exit_alert.setDefaultButton(no_close_btn)
        exit_alert.exec()
        if exit_alert.clickedButton() == yes_close_btn:
            # Записываем настройки в ini-файл
            win.set_settings_ini_file()
            event.accept()
        if exit_alert.clickedButton() == no_close_btn:
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
        # Нажатие на кнопку "Отмена"
        self.btn_cancel.clicked.connect(self.btn_cancel_clicked)
        # Нажатие на кнопку "Сохранить"
        self.btn_save.clicked.connect(self.btn_save_clicked)
    
    # Закрываем окно без сохранения настроек
    def btn_cancel_clicked(self):
        self.isSaved = False
        self.close()

    # Сохраняем настройки
    def btn_save_clicked(self):
        self.isSaved = True
        self.close()

    # При открытии окна "Настройки порта" запоминаем текущие настройки
    def showEvent(self, event):
        self.buff_baudrate = self.edit_buadrate.text()
        self.buff_bytesize = self.edit_bytesize.text()
        self.buff_parity = self.cb_parity.currentIndex()
        self.buff_stopbits = self.edit_stopbits.text()
        self.buff_xonxoff = self.cb_xonxoff.isChecked()
        # Для сохранения, либо отмены сохранения настроек при закрытии окна
        self.isSaved = False

    # При закрытии окна "Настройки порта"
    def closeEvent(self, event):
        if self.isSaved:
            # Сохраняем новые настройки
            win.baudrate = int(self.edit_buadrate.text())
            win.bytesize = int(self.edit_bytesize.text())
            parity = {0:'N', 1:'E', 2:'O'}
            win.parity = parity.get(self.cb_parity.currentIndex())
            win.stopbits = int(self.edit_stopbits.text())
            win.xonxoff = self.cb_xonxoff.isChecked()
            win.set_settings_ini_file()
        else:
            # Восстанавливаем старые настройки
            self.edit_buadrate.setText(self.buff_baudrate)
            self.edit_bytesize.setText(self.buff_bytesize)
            self.cb_parity.setCurrentIndex(self.buff_parity)
            self.edit_stopbits.setText(self.buff_stopbits)
            self.cb_xonxoff.setChecked(self.buff_xonxoff)


class AlertsWindow(QMainWindow, Ui_AlertsWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class SettingsChWindow(QMainWindow, Ui_SettingsChWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


def serial_ports():
    ''' Список всех доступных в системе COM-портов
        :raises EnvironmentError:
            Не поддерживаемая или неизвестная платформа
        :returns:
            Список COM-портов
    '''
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Неподдерживаемая платформа')
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec())
