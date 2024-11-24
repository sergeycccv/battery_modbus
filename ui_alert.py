# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'alert.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QSizePolicy,
    QTextBrowser, QWidget)
import res_rc

class Ui_AlertsWindow(object):
    def setupUi(self, AlertsWindow):
        if not AlertsWindow.objectName():
            AlertsWindow.setObjectName(u"AlertsWindow")
        AlertsWindow.setWindowModality(Qt.WindowModality.ApplicationModal)
        AlertsWindow.resize(900, 700)
        icon = QIcon()
        icon.addFile(u":/ICO/Alert24.png", QSize(), QIcon.Normal, QIcon.Off)
        AlertsWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(AlertsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.text_log = QTextBrowser(self.centralwidget)
        self.text_log.setObjectName(u"text_log")
        font = QFont()
        font.setPointSize(11)
        self.text_log.setFont(font)

        self.gridLayout.addWidget(self.text_log, 0, 0, 1, 1)

        AlertsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AlertsWindow)

        QMetaObject.connectSlotsByName(AlertsWindow)
    # setupUi

    def retranslateUi(self, AlertsWindow):
        AlertsWindow.setWindowTitle(QCoreApplication.translate("AlertsWindow", u"\u041b\u043e\u0433 \u0440\u0430\u0431\u043e\u0442\u044b \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b", None))
    # retranslateUi

