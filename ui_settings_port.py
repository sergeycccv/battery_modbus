# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_port.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QWidget)
import res_rc

class Ui_SettingsPortWindow(object):
    def setupUi(self, SettingsPortWindow):
        if not SettingsPortWindow.objectName():
            SettingsPortWindow.setObjectName(u"SettingsPortWindow")
        SettingsPortWindow.setWindowModality(Qt.WindowModality.ApplicationModal)
        SettingsPortWindow.resize(270, 270)
        SettingsPortWindow.setMinimumSize(QSize(270, 270))
        SettingsPortWindow.setMaximumSize(QSize(270, 270))
        icon = QIcon()
        icon.addFile(u":/ICO/Gear24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        SettingsPortWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(SettingsPortWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_cancel = QPushButton(self.centralwidget)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setGeometry(QRect(140, 233, 111, 24))
        self.cb_xonxoff = QCheckBox(self.centralwidget)
        self.cb_xonxoff.setObjectName(u"cb_xonxoff")
        self.cb_xonxoff.setGeometry(QRect(152, 192, 101, 20))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(32, 32, 111, 16))
        self.cb_parity = QComboBox(self.centralwidget)
        self.cb_parity.addItem("")
        self.cb_parity.addItem("")
        self.cb_parity.addItem("")
        self.cb_parity.setObjectName(u"cb_parity")
        self.cb_parity.setGeometry(QRect(152, 152, 90, 22))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(32, 112, 111, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(32, 152, 71, 16))
        self.btn_save = QPushButton(self.centralwidget)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(20, 233, 111, 24))
        self.edit_stopbits = QLineEdit(self.centralwidget)
        self.edit_stopbits.setObjectName(u"edit_stopbits")
        self.edit_stopbits.setGeometry(QRect(152, 110, 90, 22))
        self.edit_bytesize = QLineEdit(self.centralwidget)
        self.edit_bytesize.setObjectName(u"edit_bytesize")
        self.edit_bytesize.setGeometry(QRect(152, 70, 90, 22))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(32, 72, 111, 16))
        self.edit_buadrate = QLineEdit(self.centralwidget)
        self.edit_buadrate.setObjectName(u"edit_buadrate")
        self.edit_buadrate.setGeometry(QRect(152, 29, 90, 22))
        SettingsPortWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SettingsPortWindow)

        self.cb_parity.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SettingsPortWindow)
    # setupUi

    def retranslateUi(self, SettingsPortWindow):
        SettingsPortWindow.setWindowTitle(QCoreApplication.translate("SettingsPortWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u043e\u0440\u0442\u0430", None))
        self.btn_cancel.setText(QCoreApplication.translate("SettingsPortWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.cb_xonxoff.setText(QCoreApplication.translate("SettingsPortWindow", u"XOn / XOff", None))
        self.label_2.setText(QCoreApplication.translate("SettingsPortWindow", u"\u0411\u0438\u0442 \u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0443", None))
        self.cb_parity.setItemText(0, QCoreApplication.translate("SettingsPortWindow", u"\u041d\u0435\u0442", None))
        self.cb_parity.setItemText(1, QCoreApplication.translate("SettingsPortWindow", u"\u0427\u0435\u0442", None))
        self.cb_parity.setItemText(2, QCoreApplication.translate("SettingsPortWindow", u"\u041d\u0435\u0447\u0435\u0442", None))

        self.cb_parity.setCurrentText(QCoreApplication.translate("SettingsPortWindow", u"\u041d\u0435\u0442", None))
        self.label_4.setText(QCoreApplication.translate("SettingsPortWindow", u"\u0421\u0442\u043e\u043f\u043e\u0432\u044b\u0435 \u0431\u0438\u0442\u044b", None))
        self.label_5.setText(QCoreApplication.translate("SettingsPortWindow", u"\u0427\u0451\u0442\u043d\u043e\u0441\u0442\u044c", None))
        self.btn_save.setText(QCoreApplication.translate("SettingsPortWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.edit_stopbits.setText(QCoreApplication.translate("SettingsPortWindow", u"1", None))
        self.edit_bytesize.setText(QCoreApplication.translate("SettingsPortWindow", u"8", None))
        self.label_3.setText(QCoreApplication.translate("SettingsPortWindow", u"\u0411\u0438\u0442\u044b \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.edit_buadrate.setText(QCoreApplication.translate("SettingsPortWindow", u"9600", None))
    # retranslateUi

