'''
pyside6-uic ui\main.ui -o ui_main.py
pyside6-uic ui\logs.ui -o ui_logs.py
pyside6-rcc ui/res.qrc -o res_rc.py
pysyde6-designer
'''

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit
from PySide6 import QtCore
import sys, glob, serial
import ui_main, ui_logs

FLAG_CH_1 = True
FLAG_CH_2 = False
FLAG_CH_3 = True
FLAG_CH_3 = False

# Список доступных в системе COM-портов
def serial_ports():
    """ Lists serial port names
        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


class MainApp(QMainWindow, ui_main.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

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
                widget.setText('------')
                # print(f'{widget.objectName()} - {widget.text()} - {widget.property("channel")}')
                widget.setProperty('styleSheet', 'color: rgb(0, 255, 30); background-color: black;')
            

    # Обработка нажатия на кнопку "Просмотр логов"
    def btn_logs_clicked(self, checked):
        self.w = LogsApp()
        self.w.show()


    # Обработка нажатия на кнопку "Начать тестирование"
    def btn_start_test_clicked(self):
        warr = QMessageBox(self)
        warr.setWindowTitle('Внимание!')
        warr.setText('Подключитесь к системе тестирования')
        warr.setIcon(QMessageBox.Warning)
        self.statusBar.showMessage('Ожидание подключения батарей...')
        warr.exec()
        # warr.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # button = warr.exec()
        # if button == QMessageBox.Ok:
        #     self.statusBar.showMessage('Ожидание подключения...')

class LogsApp(QMainWindow, ui_logs.Ui_LogsWindow):
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
