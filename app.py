'''
Не устанавливай расширение code runner
pip uninstall -y PyQt6 PyQt6-Qt6 PyQt6-sip PyQt6-WebEngine PyQt6-WebEngine-Qt6
pip uninstall -y PySide6 PySide6-Addons PySide6-Essential shiboken6
pip install PyQt6==6.7.1 PyQt6-Qt6==6.7.1 PyQt6-WebEngine-Qt6==6.7.1 PyQt6-WebEngine
pip install PySide6-Essentials==6.7.1 PySide6==6.7.1 PySide6-Addons==6.7.1 shiboken6==6.7.1
'''
import sys, os, serial, glob, datetime, logging, logging.handlers
from configparser import ConfigParser
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, 
                               QLineEdit, QPushButton, QFileDialog, 
                               QFileSystemModel, QButtonGroup, QToolButton, 
                               QFrame, QLabel)
from PySide6.QtCore import QTimer, QEvent, Qt
from PySide6.QtGui import QFontDatabase, QPixmap
from ui_main import Ui_MainWindow
from ui_logs import Ui_LogsWindow
from ui_settings_port import Ui_SettingsPortWindow
from ui_alert import Ui_AlertsWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.port = 'COM1'
        self.baud_rate = 9600
        self.byte_size = 8
        self.parity = 'N' # N - None, E - Even, O - Odd
        self.stop_bits = 1.0
        self.x_on_x_off = False
        self.i_start_discharge_list = [0.025, 0.025, 0.025, 0.025]
        self.u_stop_discharge_list = [10.8, 10.8, 10.8, 10.8]
        self.i_stop_charge_list = [0.025, 0.025, 0.025, 0.025]
        self.number_channel = ['AKB-001', 'AKB-002', 'AKB-003', 'AKB-004']

        # Создание окна логов тестирования
        self.logs = LogsWindow(self)
        # Создание окна настроек программы
        self.settings = SettingsPortWindow(self)
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
        # Список COM-портов
        self.list_com_saved = []
        # Создание списка доступных в системе COM-портов
        self.list_com_update()
        # Чтение и применение настроек из ini-файла
        self.get_settings_ini_file()
        self.serial = serial.Serial()
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
        # Добавление к текстовой метке lbl_messages подсветку при наведении курсора
        self.lbl_messages.setAttribute(Qt.WidgetAttribute.WA_Hover)
        self.lbl_massages_icon.setAttribute(Qt.WidgetAttribute.WA_Hover)        
        # Нажатие на текстовую метку lbl_messages для просмотра лога программы
        self.lbl_messages.installEventFilter(self)
        self.lbl_massages_icon.installEventFilter(self)
        # Нажатие на кнопку "Просмотр логов"
        self.btn_logs.clicked.connect(self.btn_logs_clicked)

        # Обработка нажатия на одну из 4-х кнопок btn_read_settings_chX (прочитать настройки канала)
        self.button_ch_read_settings_group = QButtonGroup()
        self.button_ch_read_settings_group.addButton(self.btn_read_settings_ch1)
        self.button_ch_read_settings_group.addButton(self.btn_read_settings_ch2)
        self.button_ch_read_settings_group.addButton(self.btn_read_settings_ch3)
        self.button_ch_read_settings_group.addButton(self.btn_read_settings_ch4)
        self.button_ch_read_settings_group.buttonClicked.connect(self.button_ch_read_settings_clicked)

        # Обработка нажатия на одну из 4-х кнопок btn_write_settings_chX (записать настройки канала)
        self.button_ch_write_settings_group = QButtonGroup()
        self.button_ch_write_settings_group.addButton(self.btn_write_settings_ch1)
        self.button_ch_write_settings_group.addButton(self.btn_write_settings_ch2)
        self.button_ch_write_settings_group.addButton(self.btn_write_settings_ch3)
        self.button_ch_write_settings_group.addButton(self.btn_write_settings_ch4)
        self.button_ch_write_settings_group.buttonClicked.connect(self.button_ch_write_settings_clicked)

        # Обработка нажатия на одну из 4-х кнопок btn_start_test_chX (начать тестирование канала)
        self.button_ch_start_test_group = QButtonGroup()
        self.button_ch_start_test_group.addButton(self.btn_start_test_ch1)
        self.button_ch_start_test_group.addButton(self.btn_start_test_ch2)
        self.button_ch_start_test_group.addButton(self.btn_start_test_ch3)
        self.button_ch_start_test_group.addButton(self.btn_start_test_ch4)
        self.button_ch_start_test_group.buttonClicked.connect(self.button_ch_start_test_clicked)

        # Обработка изменения текста в полях ввода настроек тестирования
        self.edit_i_start_discharge_ch1.textChanged.connect(self.edit_i_start_discharge_ch1_changed)
        self.edit_u_stop_discharge_ch1.textChanged.connect(self.edit_u_stop_discharge_ch1_changed)
        self.edit_i_stop_charge_ch1.textChanged.connect(self.edit_i_stop_charge_ch1_changed)
        self.edit_i_start_discharge_ch2.textChanged.connect(self.edit_i_start_discharge_ch2_changed)
        self.edit_u_stop_discharge_ch2.textChanged.connect(self.edit_u_stop_discharge_ch2_changed)
        self.edit_i_stop_charge_ch2.textChanged.connect(self.edit_i_stop_charge_ch2_changed)
        self.edit_i_start_discharge_ch3.textChanged.connect(self.edit_i_start_discharge_ch3_changed)
        self.edit_u_stop_discharge_ch3.textChanged.connect(self.edit_u_stop_discharge_ch3_changed)
        self.edit_i_stop_charge_ch3.textChanged.connect(self.edit_i_stop_charge_ch3_changed)
        self.edit_i_start_discharge_ch4.textChanged.connect(self.edit_i_start_discharge_ch4_changed)
        self.edit_u_stop_discharge_ch4.textChanged.connect(self.edit_u_stop_discharge_ch4_changed)
        self.edit_i_stop_charge_ch4.textChanged.connect(self.edit_i_stop_charge_ch4_changed)

        # Обработка изменения текста в полях ввода инвентарных номеров АКБ
        self.edit_number_ch1.textChanged.connect(self.edit_number_ch1_changed)
        self.edit_number_ch2.textChanged.connect(self.edit_number_ch2_changed)
        self.edit_number_ch3.textChanged.connect(self.edit_number_ch3_changed)
        self.edit_number_ch4.textChanged.connect(self.edit_number_ch4_changed)

        self.initUI()

    # Вывод информационных сообщений
    def insert_text_to_log(self, level, text):
        # Вывод сообщения в лог
        self.logger.log(level, text)
        # Текущая дата для формирования сообщения в окне логов
        datetime_mess = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
        if level == 50 or level == 40 or level == 0: # CRITICAL, ERROR или NOTSET
            # Вывод сообщения в окно логов
            self.alerts.text_log.setHtml(self.alerts.text_log.toHtml() + \
                                         '<a style="color: rgb(255, 55, 30); font-weight: bold;">' + \
                                            datetime_mess + ' > '  + text + '</a>')
            # Вывод сообщения в окне программы
            self.lbl_messages.setStyleSheet('color: rgb(255, 55, 30); font-weight: bold;')
            self.lbl_messages.setText(text)
        elif level == 30: # WARNING
            # Вывод сообщения в окно логов
            self.alerts.text_log.setHtml(self.alerts.text_log.toHtml() + \
                                         '<a style="color: rgb(0, 130, 30); font-weight: normal;">' + \
                                            datetime_mess + ' > '  + text + '</a>')
            # Вывод сообщения в окне программы
            self.lbl_messages.setStyleSheet('color: rgb(0, 130, 30); font-weight: normal;')
            self.lbl_messages.setText(text)
        elif level == 20: # INFO
            # Вывод сообщения в окно логов
            if self.alerts.text_log.toPlainText() == '':
                self.alerts.text_log.setHtml('<a>' + datetime_mess + ' > '  + text + '</a>')
            else:
                self.alerts.text_log.setHtml(self.alerts.text_log.toHtml() + '<a>' + datetime_mess + ' > '  + text + '</a>')
        self.style_sheet_messages_alerts = self.lbl_messages.styleSheet()

    # Установка styleSheet для индикаторов
    def set_styleSheet_indicator(self, color: str):
        if self.led_digital_font != None:
            styleSheet = f'font-family: "{self.led_digital_font}"; ' + \
                         f'color: rgb({color}); ' + \
                         'font-size: 18px; ' + \
                         'padding-top: 2px; ' + \
                         'background-color: black;'
        else:
            styleSheet = f'color: rgb({color}); ' + \
                         'font-size: 15px; ' + \
                         'background-color: black;'
        return styleSheet

    def initUI(self):
        # Установка шрифта для вывода параметров тестирования
        font_path = 'led_digital_font.ttf'
        try:
            fp = QFontDatabase.addApplicationFont(font_path)
            font_digits = QFontDatabase.applicationFontFamilies(fp)[0]
            self.led_digital_font = font_digits
        except Exception as e:
            self.led_digital_font = None
            self.insert_text_to_log(logging.INFO, 'Ошибка загрузки шрифта для индикаторов. ' + \
                                    'Файл шрифта "led_digital_font.ttf" должен находиться в одном каталоге с программой. ' + \
                                    'Проверьте наличие и целостность этого файла. Будет загружен системный шрифт.')

        def colorize_indicator(channel: str):
            indicators = ['u_start_',
                          'u_current_',
                          'i_current_',
                          'p_current_',
                          'c_recharge_',
                          'w_recharge_',
                          'c_discharge_',
                          'w_discharge_',
                          'c_charge_',
                          'w_charge_',]
            for indicator in indicators:
                if widget.objectName() == indicator + channel:
                    widget.setProperty('styleSheet', self.set_styleSheet_indicator('100, 100, 100'))

        # Установка текста и стиля индикаторов тестирования на всех каналах
        for widget in self.findChildren(QLineEdit):
            channels = ['ch1', 'ch2', 'ch3', 'ch4']
            for channel in channels:
                if widget.property('channel') in channels:
                    widget.setText('00.000')
                    colorize_indicator(channel)

        self.frm_ch1.setEnabled(False)
        self.frm_ch2.setEnabled(False)
        self.frm_ch3.setEnabled(False)
        self.frm_ch4.setEnabled(False)

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
            else:
                self.insert_text_to_log(logging.WARNING, f'В системе обнаружены свободные COM-порты: {', '.join(self.list_com_saved)}')
                self.insert_text_to_log(logging.NOTSET, 'Подключитесь к системе тестирования')
                self.count_location_ports = 0
                self.list_com.setEnabled(True)
                self.btn_settings_port.setEnabled(True)
                self.btn_connect.setEnabled(True)

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
            self.insert_text_to_log(logging.ERROR, 'Ошибка подключения к порту ' + self.port + '. ' + str(e).replace('\n', ' '))
        
    # Открытие окна логов зарядки
    def btn_logs_clicked(self):
        self.logs.show()

    # Открытие окна настроек порта
    def btn_settings_port_clicked(self):
        self.settings.show()

    # Обработка событий мыши «нажатие на текстовую метку lbl_messages»
    # и наведение курсора на неё
    # При нажатии на текстовую метку выводится окно с информационными сообщениями
    def eventFilter(self, source, event):
            # Если курсор мыши над текстовой меткой lbl_messages
            # и нажата левая кнопка мыши
            if ((source is self.lbl_messages) or (source is self.lbl_massages_icon)) and \
                (event.type() == QEvent.MouseButtonRelease) and \
                (Qt.MouseButton.LeftButton == event.button()):
                self.alerts.show()
            # Добавление к текстовой метке lbl_messages подсветки при наведении курсора
            if (event.type() == QEvent.HoverEnter) and ((source is self.lbl_messages) or (source is self.lbl_massages_icon)):
                # Получение стилей текстовой метки из style_sheet_messages_alerts, сохранённой при добавлении строки в лог
                color_msg = self.style_sheet_messages_alerts.split(';')[0].split(':')[1]
                bold_msg = self.style_sheet_messages_alerts.split(';')[1].split(':')[1]
                self.lbl_messages.setStyleSheet(f'color: {color_msg}; font-weight: {bold_msg}; ' + 
                                                'border: 1px solid rgb(100, 100, 100); background-color: rgb(220, 220, 220); ')
                self.lbl_massages_icon.setStyleSheet('background-color: rgb(220, 220, 220); ') 
            elif (event.type() == QEvent.HoverLeave) and ((source is self.lbl_messages) or (source is self.lbl_massages_icon)):
                self.lbl_messages.setStyleSheet(self.style_sheet_messages_alerts)
                self.lbl_massages_icon.setStyleSheet('')
            return QMainWindow.eventFilter(self, source, event)

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
                # Создаем папку логов
                os.makedirs(self.path_logs, exist_ok=True)
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

        except Exception as e:
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

            with open('settings.ini', 'w', encoding='utf-8') as config_file:
                config.write(config_file)

        except Exception as e:
            self.insert_text_to_log(logging.ERROR, 'Ошибка записи настроек в ini-файл. ' + '. ' + str(e).replace('\n', ' '))

    # Обработка закрытия главного окна
    def closeEvent(self, event):
        if self.serial.isOpen():
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
                self.serial.close()
                self.insert_text_to_log(logging.WARNING, 'Произведено отключение от порта ' + self.port)
                self.insert_text_to_log(logging.INFO, 'Программа тестирования закрыта')
                event.accept()
                return
            if exit_alert.clickedButton() == no_close_btn:
                event.ignore()
                return
        # Записываем настройки в ini-файл
        win.set_settings_ini_file()
        self.insert_text_to_log(logging.INFO, 'Программа тестирования закрыта')


    # Обработка нажатия на одну из кнопок btn_read_settings_chX (прочитать настройки канала)
    def button_ch_read_settings_clicked(self, btn):
        # Получение номера канала из текста кнопки
        number_ch = int(btn.text())
        # Вызов функции, соответствующей кнопке
        self.btn_read_settings_channel(number_ch)

    # Прочитать настройки канала
    def btn_read_settings_channel(self, channel: int):
        # Читаем настройки
        buff_i_start_discharge = str(self.i_start_discharge_list[channel - 1])
        buff_u_stop_discharge = str(self.u_stop_discharge_list[channel - 1]) 
        buff_i_stop_charge = str(self.i_stop_charge_list[channel - 1])
        # Размещаем их в соответствующих полях
        for i in range(1, 5):
            if i == channel:
                child = self.findChild(QLineEdit, f'edit_i_start_discharge_ch{i}')
                child.setText(str(buff_i_start_discharge))
                child = self.findChild(QLineEdit, f'edit_u_stop_discharge_ch{i}')
                child.setText(str(buff_u_stop_discharge))
                child = self.findChild(QLineEdit, f'edit_i_stop_charge_ch{i}')
                child.setText(str(buff_i_stop_charge))

        settings_channel = '«' + str(buff_i_start_discharge) + '», ' + \
                            '«' + str(buff_u_stop_discharge) + \
                            '», ' + '«' + str(buff_i_stop_charge) + '»'

        QMessageBox.information(self, 'Информация', 'Чтение настроек канала ' + \
                                str(channel) + '. Настройки: ' + settings_channel)
   

    # Обработка нажатия на одну из кнопок btn_write_settings_chX (записать настройки канала)
    def button_ch_write_settings_clicked(self, btn):
        # Получение номера канала из текста кнопки
        number_ch = int(btn.text())
        # Вызов функции, соответствующей кнопке
        self.btn_write_settings_channel(number_ch)

    # Записать настройки канала
    def btn_write_settings_channel(self, channel: int):
        # Запоминаем старые настройки
        buff_i_start_discharge = self.i_start_discharge_list[channel - 1]
        buff_u_stop_discharge = self.u_stop_discharge_list[channel - 1]
        buff_i_stop_charge = self.i_stop_charge_list[channel - 1]

        # Записываем новые настройки
        for i in range(1, 5):
            if i == channel:
                child = self.findChild(QLineEdit, f'edit_i_start_discharge_ch{i}')
                self.i_start_discharge_list[channel - 1] = float(child.text())
                child = self.findChild(QLineEdit, f'edit_u_stop_discharge_ch{i}')
                self.u_stop_discharge_list[channel - 1] = float(child.text())
                child = self.findChild(QLineEdit, f'edit_i_stop_charge_ch{i}')
                self.i_stop_charge_list[channel - 1] = float(child.text())

        settings_channel_before = '«' + str(buff_i_start_discharge) + '», ' + \
                                  '«' + str(buff_u_stop_discharge) + \
                                  '», ' + '«' + str(buff_i_stop_charge) + '»'
        settings_channel_after = '«' + str(self.i_start_discharge_list[channel - 1]) + '», ' + \
                                 '«' + str(self.u_stop_discharge_list[channel - 1]) + \
                                 '», ' + '«' + str(self.i_stop_charge_list[channel - 1]) + '»'
        # Делаем недоступной кнопку «Записать настройки канала»
        self.settings_channel_changed(channel)
        MainWindow.insert_text_to_log(win, logging.INFO, 'Были изменены настройки канала ' + str(channel) + '. До сохранения: ' + \
                                        settings_channel_before + '. После сохранения: ' + settings_channel_after)
        QMessageBox.information(self, 'Информация', 'Были изменены настройки канала ' + str(channel) + '. До сохранения: ' + \
                                        settings_channel_before + '. После сохранения: ' + settings_channel_after)


    # Обработка нажатия на одну из кнопок btn_start_test_chX (запустить тестирование канала)
    def button_ch_start_test_clicked(self, btn):
        # Получение номера канала из objectName кнопки
        number_ch = int(btn.objectName().split('btn_start_test_ch')[1])
        # Вызов функции, соответствующей кнопке
        self.btn_start_test_channel(number_ch)

    # Запустить тестирование АКБ в канале
    def btn_start_test_channel(self, channel: int):
        if self.findChild(QPushButton, f'btn_start_test_ch{channel}').text() == ' Запуск теста':
        
            if self.findChild(QToolButton, f'btn_write_settings_ch{channel}').isEnabled():
                buff_i_start_discharge = self.i_start_discharge_list[channel - 1]
                buff_u_stop_discharge = self.u_stop_discharge_list[channel - 1]
                buff_i_stop_charge = self.i_stop_charge_list[channel - 1]
                answer = QMessageBox.warning(self, 'Предупреждение', 'Изменённые настройки канала ' + str(channel) + \
                                    ' не переданы в прибор. Продолжить тестирование, используя прежние настройки?\n' + \
                                    f'\nПрежние настройки: {buff_i_start_discharge} | {buff_u_stop_discharge} | {buff_i_stop_charge}.', \
                                    buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, \
                                    defaultButton=QMessageBox.StandardButton.No)
                if answer == QMessageBox.StandardButton.Yes:
                    self.findChild(QLabel, f'lbl_status_ch{channel}').setText('РАЗРЯД АКБ')
                    self.findChild(QLabel, f'lbl_ico_ch{channel}').setPixmap(QPixmap(':/ICO/N1_2_36.png'))
                    self.findChild(QFrame, f'frm_back_ch{channel}').setEnabled(False)
                    self.findChild(QPushButton, f'btn_start_test_ch{channel}').setText(' Остановить тестирование')
                    self.findChild(QPushButton, f'btn_start_test_ch{channel}').setStatusTip('Остановка теста АКБ в канале ' + str(channel))
                    MainWindow.insert_text_to_log(win, logging.WARNING, 'Запущено тестирование АКБ на канале ' + str(channel))
                    
            else:
                self.findChild(QLabel, f'lbl_status_ch{channel}').setText('РАЗРЯД АКБ')
                self.findChild(QLabel, f'lbl_ico_ch{channel}').setPixmap(QPixmap(':/ICO/N1_2_36.png'))
                self.findChild(QFrame, f'frm_back_ch{channel}').setEnabled(False)
                self.findChild(QPushButton, f'btn_start_test_ch{channel}').setText(' Остановить тестирование')
                self.findChild(QPushButton, f'btn_start_test_ch{channel}').setStatusTip('Остановка теста АКБ в канале ' + str(channel))
                MainWindow.insert_text_to_log(win, logging.WARNING, 'Запущено тестирование АКБ на канале ' + str(channel))

        else:
            answer = QMessageBox.warning(self, 'Внимание!', 'В данный момент происходит тестирование АКБ в канале ' + str(channel) + \
                                '. Вы действительно хотите прервать процесс?', \
                                buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, \
                                defaultButton=QMessageBox.StandardButton.No)
            if answer == QMessageBox.StandardButton.Yes:
                self.findChild(QLabel, f'lbl_status_ch{channel}').setText('АКБ ПОДКЛЮЧЕНА')
                self.findChild(QLabel, f'lbl_ico_ch{channel}').setPixmap(QPixmap(':/ICO/N1_36.png'))
                self.findChild(QFrame, f'frm_back_ch{channel}').setEnabled(True)
                self.findChild(QPushButton, f'btn_start_test_ch{channel}').setText(' Запуск теста')
                self.findChild(QPushButton, f'btn_start_test_ch{channel}').setStatusTip('Запуск теста АКБ в канале ' + str(channel))
                MainWindow.insert_text_to_log(win, logging.WARNING, 'Остановлено тестирование АКБ на канале ' + str(channel))
    

    # Реакция на изменение настроек каналов
    def settings_channel_changed(self, channel: int):
        # Для установки доступности кнопки «Записать настройки канала»
        flag_btn = set()
        # Находим кнопку «Записать настройки канала» нужного канала
        child_btn = self.findChild(QToolButton, f'btn_write_settings_ch{channel}')
        for i in range(1, 5):
            if i == channel:
                # Находим поле edit_i_start_discharge_chX нужного канала
                child_edit = self.findChild(QLineEdit, f'edit_i_start_discharge_ch{i}')
                # Проверка наличия изменений
                if self.i_start_discharge_list[channel - 1] != float(child_edit.text()):
                    child_edit.setStyleSheet('border: 1px solid rgb(255, 55, 30); font-weight: bold;')
                    flag_btn.add('1')
                else:
                    child_edit.setStyleSheet('')
                    flag_btn.discard('1')

                # Находим поле edit_u_stop_discharge_chX нужного канала
                child_edit = self.findChild(QLineEdit, f'edit_u_stop_discharge_ch{i}')
                if self.u_stop_discharge_list[channel - 1] != float(child_edit.text()):
                    child_edit.setStyleSheet('border: 1px solid rgb(255, 55, 30); font-weight: bold;')
                    flag_btn.add('2')
                else:
                    child_edit.setStyleSheet('')
                    flag_btn.discard('2')

                # Находим поле edit_i_stop_charge_chX нужного канала
                child_edit = self.findChild(QLineEdit, f'edit_i_stop_charge_ch{i}')
                if self.i_stop_charge_list[channel - 1] != float(child_edit.text()):
                    child_edit.setStyleSheet('border: 1px solid rgb(255, 55, 30); font-weight: bold;')
                    flag_btn.add('3')
                else:
                    child_edit.setStyleSheet('')
                    flag_btn.discard('3')
        
        # Если множество flag_btn не пустое, то кнопка записи настроек доступна
        if len(flag_btn) == 0:
            child_btn.setEnabled(False)
        else:
            child_btn.setEnabled(True)

    def edit_i_start_discharge_ch1_changed(self):
        self.settings_channel_changed(1)

    def edit_u_stop_discharge_ch1_changed(self):
        self.settings_channel_changed(1)

    def edit_i_stop_charge_ch1_changed(self):
        self.settings_channel_changed(1)

    def edit_i_start_discharge_ch2_changed(self):
        self.settings_channel_changed(2)

    def edit_u_stop_discharge_ch2_changed(self):
        self.settings_channel_changed(2)

    def edit_i_stop_charge_ch2_changed(self):
        self.settings_channel_changed(2)

    def edit_i_start_discharge_ch3_changed(self):
        self.settings_channel_changed(3)

    def edit_u_stop_discharge_ch3_changed(self):
        self.settings_channel_changed(3)

    def edit_i_stop_charge_ch3_changed(self):
        self.settings_channel_changed(3)

    def edit_i_start_discharge_ch4_changed(self):
        self.settings_channel_changed(4)

    def edit_u_stop_discharge_ch4_changed(self):
        self.settings_channel_changed(4)

    def edit_i_stop_charge_ch4_changed(self):
        self.settings_channel_changed(4)


    # Обработка редактирования инвентарных номеров каналов
    def edit_number_ch1_changed(self):
        self.number_channel[0] = self.edit_number_ch1.text()

    def edit_number_ch2_changed(self):
        self.number_channel[1] = self.edit_number_ch2.text()

    def edit_number_ch3_changed(self):
        self.number_channel[2] = self.edit_number_ch3.text()

    def edit_number_ch4_changed(self):
        self.number_channel[3] = self.edit_number_ch4.text()


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
        
        # Позиционирование окна
        x = win.geometry().x() + win.btn_settings_port.geometry().x()
        y = win.geometry().y() + win.btn_settings_port.geometry().y()
        self.move(x, y)
        
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
