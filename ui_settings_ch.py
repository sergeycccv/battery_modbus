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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
import res_rc

class Ui_SettingsChWindow(object):
    def setupUi(self, SettingsChWindow):
        if not SettingsChWindow.objectName():
            SettingsChWindow.setObjectName(u"SettingsChWindow")
        SettingsChWindow.setWindowModality(Qt.WindowModality.ApplicationModal)
        SettingsChWindow.resize(350, 250)
        SettingsChWindow.setMinimumSize(QSize(350, 250))
        SettingsChWindow.setMaximumSize(QSize(350, 250))
        icon = QIcon()
        icon.addFile(u":/ICO/Gear24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        SettingsChWindow.setWindowIcon(icon)
        SettingsChWindow.setProperty(u"channel", -1)
        self.centralwidget = QWidget(SettingsChWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_OK = QPushButton(self.centralwidget)
        self.btn_OK.setObjectName(u"btn_OK")
        self.btn_OK.setGeometry(QRect(110, 179, 75, 24))
        self.btn_cancel = QPushButton(self.centralwidget)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setGeometry(QRect(190, 179, 75, 24))
        self.edit_IstartDischarge = QLineEdit(self.centralwidget)
        self.edit_IstartDischarge.setObjectName(u"edit_IstartDischarge")
        self.edit_IstartDischarge.setGeometry(QRect(171, 51, 113, 22))
        self.lbl_001 = QLabel(self.centralwidget)
        self.lbl_001.setObjectName(u"lbl_001")
        self.lbl_001.setGeometry(QRect(60, 52, 101, 20))
        font = QFont()
        font.setBold(True)
        self.lbl_001.setFont(font)
        self.lbl_001.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.edit_UstopDischarge = QLineEdit(self.centralwidget)
        self.edit_UstopDischarge.setObjectName(u"edit_UstopDischarge")
        self.edit_UstopDischarge.setGeometry(QRect(171, 89, 113, 22))
        self.lbl_002 = QLabel(self.centralwidget)
        self.lbl_002.setObjectName(u"lbl_002")
        self.lbl_002.setGeometry(QRect(60, 90, 101, 20))
        self.lbl_002.setFont(font)
        self.lbl_002.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.edit_IstopCharge = QLineEdit(self.centralwidget)
        self.edit_IstopCharge.setObjectName(u"edit_IstopCharge")
        self.edit_IstopCharge.setGeometry(QRect(171, 129, 113, 22))
        self.edit_IstopCharge.setInputMask(u"0.000")
        self.lbl_003 = QLabel(self.centralwidget)
        self.lbl_003.setObjectName(u"lbl_003")
        self.lbl_003.setGeometry(QRect(60, 130, 101, 20))
        self.lbl_003.setFont(font)
        self.lbl_003.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        SettingsChWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SettingsChWindow)

        QMetaObject.connectSlotsByName(SettingsChWindow)
    # setupUi

    def retranslateUi(self, SettingsChWindow):
        SettingsChWindow.setWindowTitle(QCoreApplication.translate("SettingsChWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043a\u0430\u043d\u0430\u043b\u0430", None))
        self.btn_OK.setText(QCoreApplication.translate("SettingsChWindow", u"OK", None))
        self.btn_cancel.setText(QCoreApplication.translate("SettingsChWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.edit_IstartDischarge.setInputMask(QCoreApplication.translate("SettingsChWindow", u"0.000", None))
        self.edit_IstartDischarge.setText(QCoreApplication.translate("SettingsChWindow", u"0.025", None))
        self.lbl_001.setText(QCoreApplication.translate("SettingsChWindow", u"I \u0441\u0442\u0430\u0440\u0442 \u0440\u0430\u0437\u0440\u044f\u0434\u0430", None))
        self.edit_UstopDischarge.setInputMask(QCoreApplication.translate("SettingsChWindow", u"00.0", None))
        self.edit_UstopDischarge.setText(QCoreApplication.translate("SettingsChWindow", u"10.8", None))
        self.lbl_002.setText(QCoreApplication.translate("SettingsChWindow", u"U \u0441\u0442\u043e\u043f \u0440\u0430\u0437\u0440\u044f\u0434\u0430", None))
        self.edit_IstopCharge.setText(QCoreApplication.translate("SettingsChWindow", u"0.025", None))
        self.lbl_003.setText(QCoreApplication.translate("SettingsChWindow", u"I \u0441\u0442\u043e\u043f \u0437\u0430\u0440\u044f\u0434\u0430", None))
    # retranslateUi

