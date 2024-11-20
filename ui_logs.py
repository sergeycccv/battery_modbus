# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logs.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QToolButton, QTreeView, QWidget)
import res_rc

class Ui_LogsWindow(object):
    def setupUi(self, LogsWindow):
        if not LogsWindow.objectName():
            LogsWindow.setObjectName(u"LogsWindow")
        LogsWindow.setWindowModality(Qt.WindowModality.ApplicationModal)
        LogsWindow.resize(800, 580)
        LogsWindow.setMinimumSize(QSize(800, 580))
        LogsWindow.setMaximumSize(QSize(800, 580))
        icon = QIcon()
        icon.addFile(u":/ICO/Charge24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        LogsWindow.setWindowIcon(icon)
        LogsWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.centralwidget = QWidget(LogsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, 9, 782, 61))
        self.frame.setFrameShape(QFrame.Shape.Box)
        self.frame.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(11, 22, 131, 16))
        self.line_path_logs = QLineEdit(self.frame)
        self.line_path_logs.setObjectName(u"line_path_logs")
        self.line_path_logs.setGeometry(QRect(143, 20, 601, 22))
        self.line_path_logs.setReadOnly(True)
        self.btn_path_logs = QToolButton(self.frame)
        self.btn_path_logs.setObjectName(u"btn_path_logs")
        self.btn_path_logs.setGeometry(QRect(742, 19, 30, 24))
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(9, 80, 782, 491))
        self.frame_2.setFrameShape(QFrame.Shape.Box)
        self.frame_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.btn_view_log = QPushButton(self.frame_2)
        self.btn_view_log.setObjectName(u"btn_view_log")
        self.btn_view_log.setGeometry(QRect(591, 9, 181, 31))
        self.btn_make_graph = QPushButton(self.frame_2)
        self.btn_make_graph.setObjectName(u"btn_make_graph")
        self.btn_make_graph.setGeometry(QRect(591, 50, 181, 31))
        self.btn_close = QPushButton(self.frame_2)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(590, 441, 181, 41))
        self.btn_save_graph = QPushButton(self.frame_2)
        self.btn_save_graph.setObjectName(u"btn_save_graph")
        self.btn_save_graph.setGeometry(QRect(591, 90, 181, 31))
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(591, 175, 181, 16))
        self.frame_3.setFrameShape(QFrame.Shape.HLine)
        self.frame_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(591, 187, 181, 71))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_2.setWordWrap(True)
        self.btn_save_graph_2 = QPushButton(self.frame_2)
        self.btn_save_graph_2.setObjectName(u"btn_save_graph_2")
        self.btn_save_graph_2.setGeometry(QRect(591, 130, 181, 31))
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(591, 250, 181, 16))
        self.frame_4.setFrameShape(QFrame.Shape.HLine)
        self.frame_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.list_file_logs = QTreeView(self.frame_2)
        self.list_file_logs.setObjectName(u"list_file_logs")
        self.list_file_logs.setGeometry(QRect(10, 10, 571, 471))
        self.list_file_logs.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.list_file_logs.setAlternatingRowColors(True)
        self.list_file_logs.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        LogsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LogsWindow)

        QMetaObject.connectSlotsByName(LogsWindow)
    # setupUi

    def retranslateUi(self, LogsWindow):
        LogsWindow.setWindowTitle(QCoreApplication.translate("LogsWindow", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u0438 \u0430\u043d\u0430\u043b\u0438\u0437 \u043b\u043e\u0433\u043e\u0432 \u0437\u0430\u0440\u044f\u0434\u0430 \u0431\u0430\u0442\u0430\u0440\u0435\u0439", None))
        self.label.setText(QCoreApplication.translate("LogsWindow", u"\u041f\u0430\u043f\u043a\u0430 \u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f \u043b\u043e\u0433\u043e\u0432", None))
        self.btn_path_logs.setText(QCoreApplication.translate("LogsWindow", u"...", None))
        self.btn_view_log.setText(QCoreApplication.translate("LogsWindow", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u0444\u0430\u0439\u043b\u0430", None))
        self.btn_make_graph.setText(QCoreApplication.translate("LogsWindow", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u0433\u0440\u0430\u0444\u0438\u043a\u0430", None))
        self.btn_close.setText(QCoreApplication.translate("LogsWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        self.btn_save_graph.setText(QCoreApplication.translate("LogsWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a", None))
        self.label_2.setText(QCoreApplication.translate("LogsWindow", u"\u0414\u043b\u044f \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u0434\u0432\u0443\u0445 \u0433\u0440\u0430\u0444\u0438\u043a\u043e\u0432 \u043d\u0430 \u043e\u0434\u043d\u043e\u043c \u043f\u043e\u043b\u0435, \u0432\u044b\u0434\u0435\u043b\u0438\u0442\u0435 \u043d\u0443\u0436\u043d\u044b\u0435 \u043b\u043e\u0433\u0438 \u043c\u044b\u0448\u044c\u044e, \u0437\u0430\u0436\u0430\u0432 CTRL.", None))
        self.btn_save_graph_2.setText(QCoreApplication.translate("LogsWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0412\u0421\u0415 \u0433\u0440\u0430\u0444\u0438\u043a\u0438", None))
    # retranslateUi

