# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'alert.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QWidget)
import res_rc

class Ui_AlertsWindow(object):
    def setupUi(self, AlertsWindow):
        if not AlertsWindow.objectName():
            AlertsWindow.setObjectName(u"AlertsWindow")
        AlertsWindow.setWindowModality(Qt.WindowModality.ApplicationModal)
        AlertsWindow.resize(900, 700)
        icon = QIcon()
        icon.addFile(u":/ICO/Alert24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        AlertsWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(AlertsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        AlertsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AlertsWindow)

        QMetaObject.connectSlotsByName(AlertsWindow)
    # setupUi

    def retranslateUi(self, AlertsWindow):
        AlertsWindow.setWindowTitle(QCoreApplication.translate("AlertsWindow", u"\u041e\u0431\u0449\u0438\u0439 \u043b\u043e\u0433 \u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
    # retranslateUi

