import sys, os, serial, glob, datetime, logging, logging.handlers
from configparser import ConfigParser
from PySide6.QtWidgets import (QApplication, QMainWindow, 
    QMessageBox, QLineEdit, QPushButton, QFileDialog, QFileSystemModel,
    QButtonGroup)
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

        self.port = 'COM1'
        self.baud_rate = 9600
        self.byte_size = 8
        self.parity = 'N' # N - None, E - Even, O - Odd
        self.stop_bits = 1.0
        self.x_on_x_off = False
        self.i_start_discharge_list = [0.025, 0.025, 0.025, 0.025]
        self.u_stop_discharge_list = [10.8, 10.8, 10.8, 10.8]
        self.i_stop_charge_list = [0.025, 0.025, 0.025, 0.025]

        # Создание окна логов тестирования
        self.logs = LogsWindow(self)
        # Создание окна настроек программы
        self.settings = SettingsPortWindow(self)
        # Создание окна настроек канала
        self.settings_ch = SettingsChWindow(self)
        # Создание окна просмотра лога программы
        self.alerts = AlertsWindow(self)

        # Запуск системы логирования
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s | %(process)s | %(levelname)s | %(message)s', datefmt='%d-%m-%Y %H-%M-%S')
        handler = logging.handlers.RotatingFileHandler('log.txt', encoding='utf-8', maxBytes=5000000, backupCount=5)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        self.insert_text_to_log(logging.INFO, 'Программа тестирования запущена')

        # Папка хранения логов тестирования
        self.path_logs = os.path.abspath(os.curdir) + '\\logs'
        # Назначаем папку логов в окне просмотра логов тестирования
        self.logs.line_path_logs.setText(self.path_logs)

        # Количество попыток обнаружения COM-портов
        self.count_location_ports = 0

        # Чтение и применение настроек из ini-файла
        self.get_settings_ini_file()

        self.serial = serial.Serial()

        # Список COM-портов
        self.list_com_saved = []
        # Создание списка доступных в системе COM-портов
        self.list_com_update()

        # Таймер обновления списка COM-портов
        self.timer_upd_com_list = QTimer()

        # Изменение текущего COM-порта в списке
        self.list_com.currentIndexChanged.connect(self.list_com_changed)
        # Обновление списка COM-портов по таймеру
        self.timer_upd_com_list.timeout.connect(self.list_com_update)
        # Старт таймера обновления списка COM-портов (1 сек)
        self.timer_upd_com_list.start(1000)
        # Нажатие на кнопку "Подключиться"
        self.btn_connect.clicked.connect(self.btn_connect_clicked)
        # Нажатие на кнопку "Настройки порта"
        self.btn_settings_port.clicked.connect(self.btn_settings_port_clicked)
        # Нажатие на кнопку "Лог работы программы"
        self.btn_alerts.clicked.connect(self.btn_alerts_clicked)
        # Нажатие на кнопку "Просмотр логов"
        self.btn_logs.clicked.connect(self.btn_logs_clicked)

        # Обработка нажатия на одну из 4-х кнопок btn_settings_ch_XX
        self.button_ch_group = QButtonGroup()
        self.button_ch_group.addButton(self.btn_settings_ch_1)
        self.button_ch_group.addButton(self.btn_settings_ch_2)
        self.button_ch_group.addButton(self.btn_settings_ch_3)
        self.button_ch_group.addButton(self.btn_settings_ch_4)
        self.button_ch_group.buttonClicked.connect(self.btn_settings_ch_clicked)

    # Вывод информационных сообщений
    def insert_text_to_log(self, level, text):
        # Вывод сообщения в лог
        self.logger.log(level, text)

        # Текущая дата для формирования сообщения в окне логов
        datetime_mess = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')

        if level == 50 or level == 40 or level == 0: # CRITICAL, ERROR или NOTSET
            # Вывод сообщения в окно логов
            self.alerts.text_log.setHtml(self.alerts.text_log.toHtml() + '<a style="color: rgb(255, 55, 30); font-weight: bold;">' + datetime_mess + ' > '  + text + '</a>')
            # Вывод сообщения в окне программы
            self.lbl_messages.setStyleSheet('color: rgb(255, 55, 30); font-weight: bold;')
            self.lbl_messages.setText(text)
        elif level == 30: # WARNING
            # Вывод сообщения в окно логов
            self.alerts.text_log.setHtml(self.alerts.text_log.toHtml() + '<a style="color: rgb(0, 130, 30); font-weight: normal;">' + datetime_mess + ' > '  + text + '</a>')
            # Вывод сообщения в окне программы
            self.lbl_messages.setStyleSheet('color: rgb(0, 130, 30); font-weight: normal;')
            self.lbl_messages.setText(text)
        elif level == 20: # INFO
            # Вывод сообщения в окно логов
            if self.alerts.text_log.toPlainText() == '':
                self.alerts.text_log.setHtml('<a>' + datetime_mess + ' > '  + text + '</a>')
            else:
                self.alerts.text_log.setHtml(self.alerts.text_log.toHtml() + '<a>' + datetime_mess + ' > '  + text + '</a>')

    def initUI(self):
        # Установка стиля текста в полях вывода данных тестирования
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
        # Если список COM-портов изменился или пустой
        if (self.list_com_saved != serial_ports()) or (len(self.list_com_saved) == 0):
            # Очищаем список
            self.list_com.clear()
            # Обновляем список COM-портов
            self.list_com.addItems(serial_ports())
            self.port = self.list_com.currentText()
            # Сохраняем список COM-портов
            self.list_com_saved = serial_ports()

            if len(self.list_com_saved) == 0:
                if self.count_location_ports == 0:
                    self.insert_text_to_log(logging.ERROR, 'В системе нет ни одного свободного COM-порта')

                self.count_location_ports += 1
                
                self.list_com.setCurrentIndex(-1)
                self.port = ''
                self.list_com.setEnabled(False)
                self.btn_settings_port.setEnabled(False)
                self.btn_connect.setEnabled(False)
                self.frm_ch_1.setEnabled(False)
                self.frm_ch_2.setEnabled(False)
                self.frm_ch_3.setEnabled(False)
                self.frm_ch_4.setEnabled(False)
            else:
                self.insert_text_to_log(logging.WARNING, f'В системе обнаружены свободные COM-порты: {', '.join(self.list_com_saved)}')
                self.insert_text_to_log(logging.NOTSET, 'Подключитесь к системе тестирования')

                self.count_location_ports = 0

                self.list_com.setEnabled(True)
                self.btn_settings_port.setEnabled(True)
                self.btn_connect.setEnabled(True)
                self.frm_ch_1.setEnabled(True)
                self.frm_ch_2.setEnabled(True)
                self.frm_ch_3.setEnabled(True)
                self.frm_ch_4.setEnabled(True)

    # Подключение к COM-порту
    def btn_connect_clicked(self):
        try:

            if not self.serial.isOpen():

                self.serial = serial.Serial(self.port, self.baud_rate, self.byte_size, self.parity, self.stop_bits, self.x_on_x_off)

                # Стоп таймера обновления списка COM-портов
                self.timer_upd_com_list.stop()
                
                self.list_com.setEnabled(False)
                self.btn_settings_port.setEnabled(False)
                self.btn_connect.setText('Отключиться')

                self.insert_text_to_log(logging.WARNING, 'Установлено подключение к порту ' + self.port)
            else:
                self.serial.close()

                # Запуск таймера обновления списка COM-портов
                self.timer_upd_com_list.start(1000)

                self.list_com.setEnabled(True)
                self.btn_settings_port.setEnabled(True)
                self.btn_connect.setText('Подключиться')

                self.insert_text_to_log(logging.WARNING, 'Произведено отключение от порта ' + self.port)
                self.insert_text_to_log(logging.NOTSET, 'Подключитесь к системе тестирования')

        except Exception as e:
            # QMessageBox.warning(self, 'Предупреждение', 'Ошибка подключения к порту ' + self.port + '\n' + str(e))
            self.insert_text_to_log(logging.ERROR, 'Ошибка подключения к порту ' + self.port + '. ' + str(e).replace('\n', ' '))
        
    # Открытие окна логов зарядки
    def btn_logs_clicked(self):
        self.logs.show()

    # Открытие окна настроек порта
    def btn_settings_port_clicked(self):
        self.settings.show()

    # Открытие окна просмотра лога программы
    def btn_alerts_clicked(self):
        self.alerts.show()

    # Чтение настроек из ini-файла
    def get_settings_ini_file(self):
        try:
            config = ConfigParser()
            config.read('settings.ini')
            
            # Если назначена папка логов в ini-файле и она существует
            if (config.has_option('GENERAL', 'path_logs')) and (os.path.isdir(config.get('GENERAL', 'path_logs'))):
                # то присваиваем её переменной path_logs
                self.path_logs = config.get('GENERAL', 'path_logs')
            else:
                # Иначе указываем папку логов в текущей директории
                self.path_logs = os.path.abspath(os.curdir) + '\\logs'
            # Назначаем папку логов в окне просмотра логов зарядки
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

            if config.has_option('COM', 'baud_rate'):
                self.baud_rate = config.getint('COM', 'baud_rate')
            self.settings.cb_baud_rate.setCurrentText(str(self.baud_rate))

            if config.has_option('COM', 'byte_size'):
                self.byte_size = config.getint('COM', 'byte_size')
            self.settings.cb_byte_size.setCurrentText(str(self.byte_size))

            parity = {'N': 0, 'E': 1, 'O': 2}
            if config.has_option('COM', 'Parity'):
                self.parity = config.get('COM', 'Parity')
            self.settings.cb_parity.setCurrentIndex(parity.get(self.parity))

            if config.has_option('COM', 'stop_bits'):
                self.stop_bits = config.getfloat('COM', 'stop_bits')
            self.settings.cb_stop_bits.setCurrentText(str(self.stop_bits))
            
            if config.has_option('COM', 'x_on_x_off'):
                self.x_on_x_off = config.getboolean('COM', 'x_on_x_off')
            self.settings.cb_x_on_x_off.setChecked(self.x_on_x_off)

            # for i in range(0, 3):

            #     if config.has_option('CH1', 'i_start_discharge'):
            #         self.i_start_discharge_list[0] = config.getfloat('CH1', 'i_start_discharge')
            #         # self.settings_ch.edit_i_start_discharge.setText(str(self.i_start_discharge_list))
            #     else:
            #         self.i_start_discharge_list[0] = 0.025
            #         # self.settings_ch.edit_i_start_discharge.setText('0.025')

            #     if config.has_option('CH1', 'u_stop_discharge'):
            #         self.u_stop_discharge_list[0] = config.getfloat('CH1', 'u_stop_discharge')
            #         # self.settings_ch.edit_u_stop_discharge.setText(str(self.u_stop_discharge_list))
            #     else:
            #         self.u_stop_discharge_list[0] = 10.8
            #         # self.settings_ch.edit_u_stop_discharge.setText('10.8')

            #     if config.has_option('CH1', 'i_stop_charge'):
            #         self.i_stop_charge_list[0] = config.getfloat('CH1', 'i_stop_charge')
            #         # self.settings_ch.edit_i_stop_charge.setText(str(self.i_stop_charge_list))
            #     else:
            #         self.u_stop_discharge_list[0] = 0.025
            #         # self.settings_ch.edit_i_stop_charge.setText('0.025')


        except Exception as e:
            # QMessageBox.warning(self, 'Предупреждение', 'Ошибка чтения настроек из ini-файла:\n' + str(e))
            self.insert_text_to_log(logging.ERROR, 'Ошибка чтения настроек из ini-файла. ' + str(e).replace('\n', ' '))

    # Запись настроек в ini-файл
    def set_settings_ini_file(self):
        try:
            config = ConfigParser()
            config.add_section('GENERAL')
            config.set('GENERAL', 'path_logs', win.path_logs)

            config.add_section('COM')
            config.set('COM', 'Port', win.port)
            config.set('COM', 'baud_rate', str(win.baud_rate))
            config.set('COM', 'byte_size', str(win.byte_size))
            config.set('COM', 'Parity', win.parity)
            config.set('COM', 'stop_bits', str(win.stop_bits))
            config.set('COM', 'x_on_x_off', str(win.x_on_x_off))

            # config.add_section('CH1')
            # config.set('CH1', 'i_start_discharge', str(win.i_start_discharge_list[0]))
            # config.set('CH1', 'u_stop_discharge', str(win.u_stop_discharge_list[0]))
            # config.set('CH1', 'i_stop_charge', str(win.i_stop_charge_list[0]))

            # config.add_section('CH2')
            # config.set('CH2', 'i_start_discharge', str(win.i_start_discharge_list[1]))
            # config.set('CH2', 'u_stop_discharge', str(win.u_stop_discharge_list[1]))
            # config.set('CH2', 'i_stop_charge', str(win.i_stop_charge_list[1]))

            # config.add_section('CH3')
            # config.set('CH3', 'i_start_discharge', str(win.i_start_discharge_list[2]))
            # config.set('CH3', 'u_stop_discharge', str(win.u_stop_discharge_list[2]))
            # config.set('CH3', 'i_stop_charge', str(win.i_stop_charge_list[2]))

            # config.add_section('CH4')
            # config.set('CH4', 'i_start_discharge', str(win.i_start_discharge_list[3]))
            # config.set('CH4', 'u_stop_discharge', str(win.u_stop_discharge_list[3]))
            # config.set('CH4', 'i_stop_charge', str(win.i_stop_charge_list[3]))

            with open('settings.ini', 'w', encoding='utf-8') as config_file:
                config.write(config_file)

        except Exception as e:
            # QMessageBox.warning(self, 'Предупреждение', 'Ошибка записи настроек в ini-файл:\n' + str(e))
            self.insert_text_to_log(logging.ERROR, 'Ошибка записи настроек в ini-файл. ' + '. ' + str(e).replace('\n', ' '))

    # Открытие окна настроек каналов
    def btn_settings_ch_clicked(self, btn):
        # Получение номера канала из текста кнопки
        number_ch = int(btn.text())
        # self.settings_ch.setWindowTitle(f'Настройки канала {number_ch}')
        self.settings_ch.channel = number_ch
        self.settings_ch.show()

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
            self.insert_text_to_log(logging.INFO, 'Программа тестирования закрыта')
            event.accept()
        if exit_alert.clickedButton() == no_close_btn:
            event.ignore()


class LogsWindow(QMainWindow, Ui_LogsWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
        # Настройка модели файловой системы для отображения содержимого папки
        self.file_model = QFileSystemModel()
        self.file_model.setNameFilters(['*.log', '*.txt']) # фильтр по расширению
        self.file_model.setNameFilterDisables(False)
        self.list_file_logs.setModel(self.file_model)
        self.list_file_logs.hideColumn(1)
        self.list_file_logs.setColumnWidth(0, 320)
        self.list_file_logs.setColumnWidth(2, 140)
        self.list_file_logs.setColumnWidth(3, 90)

        # Нажатие на кнопку "Выбрать папку"
        self.btn_path_logs.clicked.connect(self.btn_path_logs_clicked)
        # Нажатие на кнопку "Закрыть окно"
        self.btn_close.clicked.connect(self.btn_close_clicked)
        
    # Выбор папки хранения логов
    def btn_path_logs_clicked(self):
        directory = QFileDialog.getExistingDirectory(self, 'Выберите папку', win.path_logs)
        if directory != '':
            win.path_logs = directory
            self.line_path_logs.setText(directory)
            # Отображение содержимого папки
            self.showEvent(self)
            # Запись настроек в ini-файл
            win.set_settings_ini_file()

    # Закрытие окна логов
    def btn_close_clicked(self):
        self.close()

    def showEvent(self, event):
        # Показ содержимого папки логов
        self.file_model.setRootPath(win.path_logs)
        self.list_file_logs.setRootIndex(self.file_model.index(win.path_logs))


class SettingsPortWindow(QMainWindow, Ui_SettingsPortWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # Нажатие на кнопку "Отмена"
        self.btn_cancel.clicked.connect(self.btn_cancel_clicked)
        # Нажатие на кнопку "Сохранить"
        self.btn_save.clicked.connect(self.btn_save_clicked)
    
    # Закрытие окна без сохранения настроек
    def btn_cancel_clicked(self):
        self.isSaved = False
        self.close()

    # Сохранение настроек
    def btn_save_clicked(self):
        self.isSaved = True
        self.close()

    # При открытии окна "Настройки порта" запомнить текущие настройки
    def showEvent(self, event):
        self.buff_baud_rate = self.cb_baud_rate.currentText()
        self.buff_byte_size = self.cb_byte_size.currentText()
        self.buff_parity = self.cb_parity.currentIndex()
        self.buff_stop_bits = self.cb_stop_bits.currentText()
        self.buff_x_on_x_off = self.cb_x_on_x_off.isChecked()
        # Для сохранения, либо отмены сохранения настроек при закрытии окна
        self.isSaved = False

    # При закрытии окна "Настройки порта"
    def closeEvent(self, event):
        if self.isSaved:
            # Сохранение новых настроек
            win.baud_rate = int(self.cb_baud_rate.currentText())
            win.byte_size = int(self.cb_byte_size.currentText())
            parity = {0:'N', 1:'E', 2:'O'}
            win.parity = parity.get(self.cb_parity.currentIndex())
            win.stop_bits = float(self.cb_stop_bits.currentText())
            win.x_on_x_off = self.cb_x_on_x_off.isChecked()
            win.set_settings_ini_file()
            settings_port_before = '«' + str(self.buff_baud_rate) + '», ' + '«' + str(self.buff_byte_size) + \
                                '», ' + '«' + str(self.buff_parity) + '», ' + '«' + str(self.buff_stop_bits) + \
                                '», ' + '«' + str(self.buff_x_on_x_off) + '»'
            settings_port_after = '«' + str(win.baud_rate) + '», ' + '«' + str(win.byte_size) + \
                                '», ' + '«' + str(win.parity) + '», ' + '«' + str(win.stop_bits) + \
                                '», ' + '«' + str(win.x_on_x_off) + '»'
            MainWindow.insert_text_to_log(win, logging.INFO, 'Были изменены настройки порта. До сохранения: ' + \
                                          settings_port_before + '. После сохранения: ' + settings_port_after)

        else:
            # Восстановление старых настроек
            self.cb_baud_rate.setCurrentText(self.buff_baud_rate)
            self.cb_byte_size.setCurrentText(self.buff_byte_size)
            self.cb_parity.setCurrentIndex(self.buff_parity)
            self.cb_stop_bits.setCurrentText(self.buff_stop_bits)
            self.cb_x_on_x_off.setChecked(self.buff_x_on_x_off)


class AlertsWindow(QMainWindow, Ui_AlertsWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class SettingsChWindow(QMainWindow, Ui_SettingsChWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # Нажатие на кнопку "Отмена"
        self.btn_cancel.clicked.connect(self.btn_cancel_clicked)
        # Нажатие на кнопку "Записать"
        self.btn_write.clicked.connect(self.btn_write_clicked)
        # Нажатие на кнопку "Прочитать"
        self.btn_read.clicked.connect(self.btn_read_clicked)
    
    # Закрытие окна без записи настроек
    def btn_cancel_clicked(self):
        self.isSaved = False
        self.close()

    # Чтение настроек канала из прибора
    def btn_read_clicked(self):
        # Вывод информационного сообщения
        self.lbl_info.setStyleSheet('color: rgb(0, 130, 30); font-weight: bold;')
        self.lbl_info.setText('Прочитано из канала ' + str(self.channel))

    # Запись настроек канала в прибор
    def btn_write_clicked(self):
        self.isSaved = True
        # self.close()

    # При открытии окна "Настройки канала" запомнить текущие настройки
    def showEvent(self, event):
        # Запомнить текущие настройки
        self.buff_i_start_discharge = win.i_start_discharge_list
        self.buff_u_stop_discharge = win.u_stop_discharge_list
        self.buff_i_stop_charge = win.i_stop_charge_list

        self.edit_i_start_discharge.setText(str(win.i_start_discharge_list[self.channel - 1]))
        self.edit_u_stop_discharge.setText(str(win.u_stop_discharge_list[self.channel - 1]))
        self.edit_i_stop_charge.setText(str(win.i_stop_charge_list[self.channel - 1]))

        # Вывод информационного сообщения
        self.lbl_info.setStyleSheet('color: rgb(0, 130, 30); font-weight: bold;')
        self.lbl_info.setText('Прочитано из канала ' + str(self.channel))
        # self.lbl_info.setStyleSheet('color: rgb(255, 55, 30); font-weight: bold;')
        # self.lbl_info.setText('Не прочитано из канала ' + str(self.channel))

        # Для сохранения, либо отмены сохранения настроек при закрытии окна
        self.isSaved = False

    # При закрытии окна "Настройки канала"
    def closeEvent(self, event):
        if self.isSaved:
            # Сохранение новых настроек
            win.i_start_discharge_list[self.channel - 1] = float(self.edit_i_start_discharge.text())
            win.u_stop_discharge_list[self.channel - 1] = float(self.edit_u_stop_discharge.text())
            win.i_stop_charge_list[self.channel - 1] = float(self.edit_i_stop_charge.text())
            # win.set_settings_ini_file()
        else:
            # Восстановление старых настроек
            self.edit_i_start_discharge.setText(str(self.buff_i_start_discharge[self.channel - 1]))
            self.edit_u_stop_discharge.setText(str(self.buff_u_stop_discharge[self.channel - 1]))
            self.edit_i_stop_charge.setText(str(self.buff_i_stop_charge[self.channel - 1]))


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
