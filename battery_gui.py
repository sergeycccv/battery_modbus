import sys, glob, serial, modbus_tk, time
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit, QDialog
from PySide6 import QtCore
import ui_main, ui_logs


# Список доступных в системе COM-портов
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


def get_modbus_data(port='COM3', baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0):
    logger = modbus_tk.utils.create_logger('console')
    try:
        master = modbus_rtu.RtuMaster(
            serial.Serial(port, baudrate, bytesize, parity, stopbits, xonxoff)
        )
        master.set_timeout(5.0)
        master.set_verbose(True)
        logger.info(f'Подключено к {port}')
        p = master.execute(3, cst.READ_INPUT_REGISTERS, 0, 25)
        logger.info(p)
    except modbus_tk.modbus.ModbusError as exc:
        logger.error(f'{exc} - Code = {exc.get_exception_code()}')
    return p


class MainApp(QMainWindow, ui_main.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # # Создание окна просмотра логов
        # self.logs_window = LogsApp()

        # Список COM-портов
        self.list_com.addItems(serial_ports())

        # self.statusBar.showMessage('Ожидание подключения батарей...')

        # Нажатие на кнопку "Просмотр логов"
        self.btn_logs.clicked.connect(self.btn_logs_clicked)

        # Нажатие на кнопку "Начать тестирование"
        self.btn_start_test_1.clicked.connect(self.btn_start_test_clicked)

        # Инициализация текста в полях ввода и их стиля
        for widget in self.findChildren(QLineEdit):
            # if isinstance(widget, QLineEdit):
            if widget.property('channel') in {'ch1', 'ch2', 'ch3', 'ch4'}:
                # widget.setProperty('text', '------')
                widget.setText('00,000')
                # print(f'{widget.objectName()} - {widget.text()} - {widget.property("channel")}')
                # widget.setProperty('styleSheet', 'color: rgb(0, 255, 30); background-color: black;')
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
        
        # Нажатие на кнопку "Подключиться"
        self.btn_connect.clicked.connect(self.btn_connect_clicked)


    # Обработка нажатия на кнопку "Подключиться"
    def btn_connect_clicked(self, checked):
        reg_modbus = ()
        reg_modbus = get_modbus_data(self.list_com.currentText())
        # Получение Ustart с устройства тестирования
        self.edit_1_Ustart.setText(str(round(reg_modbus[1] * 0.00125, 3)))


    # Обработка нажатия на кнопку "Просмотр логов"
    def btn_logs_clicked(self):
        # self.w = LogsApp(self)
        # self.w.show()
        self.logs_window = LogsApp(self)#QDialog(self)
        self.logs_window.show()


    # Обработка нажатия на кнопку "Начать тестирование"
    def btn_start_test_clicked(self):
        warr = QMessageBox(self)
        warr.setWindowTitle('Внимание!')
        warr.setText('Подключитесь к системе тестирования')
        warr.setIcon(QMessageBox.Warning)
        # self.statusBar.showMessage('Ожидание подключения батарей...')
        warr.exec()
        # warr.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # button = warr.exec()
        # if button == QMessageBox.Ok:
        #     self.statusBar.showMessage('Ожидание подключения...')

    
    # Обработка закрытия главного окна
    def closeEvent(self, event):
        # answer = QMessageBox.question(self, 'Выход', 'Вы уверены, что хотите выйти из приложения?',
        # QMessageBox.StandardButton.No | \
        # QMessageBox.StandardButton.Yes,
        # QMessageBox.StandardButton.Yes)
        # if answer == QMessageBox.StandardButton.Yes:
        #     event.accept()
        # if answer == QMessageBox.StandardButton.No:
        #     event.ignore()
        warr = QMessageBox(self)
        warr.setWindowTitle('Внимание!')
        warr.setText('<p><strong>В данный момент тестируется батарея!</strong></p><p>Вы действительно хотите прервать тестирование и закрыть программу?</p>')
        warr.setIcon(warr.Icon.Warning)
        warr.addButton('Нет', warr.ButtonRole.NoRole)
        warr.addButton('  Закрыть программу  ', warr.ButtonRole.YesRole)
        warr.exec()
        button = warr.clickedButton().text()
        if button == '  Закрыть программу  ':
            event.accept()
        if button == 'Нет':
            event.ignore()


class LogsApp(QMainWindow, ui_logs.Ui_LogsWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Оставить только кнопку закрытия окна
        self.setWindowFlags(self.windowFlags() & QtCore.Qt.CustomizeWindowHint)
        self.setWindowFlags(self.windowFlags() & QtCore.Qt.WindowCloseButtonHint)
        # self.setWindowFlags(self.windowFlags() & QtCore.Qt.WindowMaximizeButtonHint)
        # self.move(self.geometry().center() - self.rect().center() - QtCore.QPoint(40, 30))
        # self.move(0, 0)
        # self.resize(1130, 601)
        # self.geometry = QtCore.QRect(0, 0, 1130, 601)
        # print(self.geometry().getCoords())


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
