# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_ch.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
import res_rc

class Ui_SettingsChWindow(object):
    def setupUi(self, SettingsChWindow):
        if not SettingsChWindow.objectName():
            SettingsChWindow.setObjectName(u"SettingsChWindow")
        SettingsChWindow.setWindowModality(Qt.WindowModality.ApplicationModal)
        SettingsChWindow.resize(400, 250)
        SettingsChWindow.setMinimumSize(QSize(350, 250))
        SettingsChWindow.setMaximumSize(QSize(400, 250))
        icon = QIcon()
        icon.addFile(u":/ICO/Gear24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        SettingsChWindow.setWindowIcon(icon)
        SettingsChWindow.setStyleSheet(u" #lbl_info {\n"
"	background-color: rgb(210, 210, 210);\n"
"	padding-left: 5;\n"
"}")
        SettingsChWindow.setProperty(u"channel", -1)
        self.centralwidget = QWidget(SettingsChWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_write = QPushButton(self.centralwidget)
        self.btn_write.setObjectName(u"btn_write")
        self.btn_write.setGeometry(QRect(295, 10, 91, 31))
        self.btn_cancel = QPushButton(self.centralwidget)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setGeometry(QRect(295, 210, 91, 31))
        self.btn_read = QPushButton(self.centralwidget)
        self.btn_read.setObjectName(u"btn_read")
        self.btn_read.setGeometry(QRect(295, 50, 91, 31))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 270, 231))
        self.frame.setFrameShape(QFrame.Shape.Box)
        self.frame.setFrameShadow(QFrame.Shadow.Sunken)
        self.edit_u_stop_discharge = QLineEdit(self.frame)
        self.edit_u_stop_discharge.setObjectName(u"edit_u_stop_discharge")
        self.edit_u_stop_discharge.setGeometry(QRect(130, 125, 113, 22))
        self.lbl_001 = QLabel(self.frame)
        self.lbl_001.setObjectName(u"lbl_001")
        self.lbl_001.setGeometry(QRect(19, 88, 101, 20))
        font = QFont()
        font.setBold(True)
        self.lbl_001.setFont(font)
        self.lbl_001.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lbl_003 = QLabel(self.frame)
        self.lbl_003.setObjectName(u"lbl_003")
        self.lbl_003.setGeometry(QRect(19, 166, 101, 20))
        self.lbl_003.setFont(font)
        self.lbl_003.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.edit_i_stop_charge = QLineEdit(self.frame)
        self.edit_i_stop_charge.setObjectName(u"edit_i_stop_charge")
        self.edit_i_stop_charge.setGeometry(QRect(130, 165, 113, 22))
        self.edit_i_stop_charge.setInputMask(u"0.000")
        self.edit_i_start_discharge = QLineEdit(self.frame)
        self.edit_i_start_discharge.setObjectName(u"edit_i_start_discharge")
        self.edit_i_start_discharge.setGeometry(QRect(130, 87, 113, 22))
        self.lbl_002 = QLabel(self.frame)
        self.lbl_002.setObjectName(u"lbl_002")
        self.lbl_002.setGeometry(QRect(19, 126, 101, 20))
        self.lbl_002.setFont(font)
        self.lbl_002.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lbl_info = QLabel(self.frame)
        self.lbl_info.setObjectName(u"lbl_info")
        self.lbl_info.setGeometry(QRect(36, 30, 201, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.lbl_info.setFont(font1)
        self.lbl_info.setFrameShape(QFrame.Shape.Box)
        self.lbl_info.setFrameShadow(QFrame.Shadow.Sunken)
        self.lbl_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        SettingsChWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SettingsChWindow)

        QMetaObject.connectSlotsByName(SettingsChWindow)
    # setupUi

    def retranslateUi(self, SettingsChWindow):
        SettingsChWindow.setWindowTitle(QCoreApplication.translate("SettingsChWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043a\u0430\u043d\u0430\u043b\u0430", None))
        self.btn_write.setText(QCoreApplication.translate("SettingsChWindow", u"\u0417\u0430\u043f\u0438\u0441\u0430\u0442\u044c", None))
        self.btn_cancel.setText(QCoreApplication.translate("SettingsChWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.btn_read.setText(QCoreApplication.translate("SettingsChWindow", u"\u041f\u0440\u043e\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.edit_u_stop_discharge.setInputMask(QCoreApplication.translate("SettingsChWindow", u"00.0", None))
        self.edit_u_stop_discharge.setText(QCoreApplication.translate("SettingsChWindow", u"10.8", None))
        self.lbl_001.setText(QCoreApplication.translate("SettingsChWindow", u"I \u0441\u0442\u0430\u0440\u0442 \u0440\u0430\u0437\u0440\u044f\u0434\u0430", None))
        self.lbl_003.setText(QCoreApplication.translate("SettingsChWindow", u"I \u0441\u0442\u043e\u043f \u0437\u0430\u0440\u044f\u0434\u0430", None))
        self.edit_i_stop_charge.setText(QCoreApplication.translate("SettingsChWindow", u"0.025", None))
        self.edit_i_start_discharge.setInputMask(QCoreApplication.translate("SettingsChWindow", u"0.000", None))
        self.edit_i_start_discharge.setText(QCoreApplication.translate("SettingsChWindow", u"0.025", None))
        self.lbl_002.setText(QCoreApplication.translate("SettingsChWindow", u"U \u0441\u0442\u043e\u043f \u0440\u0430\u0437\u0440\u044f\u0434\u0430", None))
        self.lbl_info.setText(QCoreApplication.translate("SettingsChWindow", u"\u041f\u0440\u043e\u0447\u0438\u0442\u0430\u043d\u043e \u0438\u0437 \u043a\u0430\u043d\u0430\u043b\u0430", None))
    # retranslateUi

