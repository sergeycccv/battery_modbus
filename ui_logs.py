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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QListView, QMainWindow, QPushButton, QSizePolicy,
    QToolButton, QWidget)
import res_rc

class Ui_LogsWindow(object):
    def setupUi(self, LogsWindow):
        if not LogsWindow.objectName():
            LogsWindow.setObjectName(u"LogsWindow")
        LogsWindow.setWindowModality(Qt.WindowModality.ApplicationModal)
        LogsWindow.resize(550, 400)
        LogsWindow.setMinimumSize(QSize(550, 400))
        LogsWindow.setMaximumSize(QSize(550, 400))
        icon = QIcon()
        icon.addFile(u":/ICO/Charge24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        LogsWindow.setWindowIcon(icon)
        LogsWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.centralwidget = QWidget(LogsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, 9, 532, 61))
        self.frame.setFrameShape(QFrame.Shape.Box)
        self.frame.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(11, 22, 131, 16))
        self.line_path_logs = QLineEdit(self.frame)
        self.line_path_logs.setObjectName(u"line_path_logs")
        self.line_path_logs.setGeometry(QRect(143, 20, 351, 22))
        self.tbtn_path_logs = QToolButton(self.frame)
        self.tbtn_path_logs.setObjectName(u"tbtn_path_logs")
        self.tbtn_path_logs.setGeometry(QRect(492, 19, 30, 24))
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(9, 80, 532, 311))
        self.frame_2.setFrameShape(QFrame.Shape.Box)
        self.frame_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.list_file_logs = QListView(self.frame_2)
        self.list_file_logs.setObjectName(u"list_file_logs")
        self.list_file_logs.setGeometry(QRect(10, 10, 321, 291))
        self.list_file_logs.setFrameShape(QFrame.Shape.Box)
        self.list_file_logs.setFrameShadow(QFrame.Shadow.Plain)
        self.btn_view_log = QPushButton(self.frame_2)
        self.btn_view_log.setObjectName(u"btn_view_log")
        self.btn_view_log.setGeometry(QRect(340, 10, 181, 24))
        self.btn_make_graph = QPushButton(self.frame_2)
        self.btn_make_graph.setObjectName(u"btn_make_graph")
        self.btn_make_graph.setGeometry(QRect(340, 40, 181, 24))
        self.btn_close = QPushButton(self.frame_2)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(340, 278, 181, 24))
        self.btn_save_graph = QPushButton(self.frame_2)
        self.btn_save_graph.setObjectName(u"btn_save_graph")
        self.btn_save_graph.setGeometry(QRect(340, 70, 181, 24))
        self.btn_update_list = QPushButton(self.frame_2)
        self.btn_update_list.setObjectName(u"btn_update_list")
        self.btn_update_list.setGeometry(QRect(340, 248, 181, 24))
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(340, 143, 181, 16))
        self.frame_3.setFrameShape(QFrame.Shape.HLine)
        self.frame_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(340, 155, 181, 71))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_2.setWordWrap(True)
        self.btn_save_graph_2 = QPushButton(self.frame_2)
        self.btn_save_graph_2.setObjectName(u"btn_save_graph_2")
        self.btn_save_graph_2.setGeometry(QRect(340, 100, 181, 24))
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(340, 218, 181, 16))
        self.frame_4.setFrameShape(QFrame.Shape.HLine)
        self.frame_4.setFrameShadow(QFrame.Shadow.Sunken)
        LogsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LogsWindow)

        QMetaObject.connectSlotsByName(LogsWindow)
    # setupUi

    def retranslateUi(self, LogsWindow):
        LogsWindow.setWindowTitle(QCoreApplication.translate("LogsWindow", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u0438 \u0430\u043d\u0430\u043b\u0438\u0437 \u043b\u043e\u0433\u043e\u0432 \u0437\u0430\u0440\u044f\u0434\u0430 \u0431\u0430\u0442\u0430\u0440\u0435\u0439", None))
        self.label.setText(QCoreApplication.translate("LogsWindow", u"\u041f\u0430\u043f\u043a\u0430 \u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f \u043b\u043e\u0433\u043e\u0432", None))
        self.tbtn_path_logs.setText(QCoreApplication.translate("LogsWindow", u"...", None))
        self.btn_view_log.setText(QCoreApplication.translate("LogsWindow", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u0444\u0430\u0439\u043b\u0430", None))
        self.btn_make_graph.setText(QCoreApplication.translate("LogsWindow", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u0433\u0440\u0430\u0444\u0438\u043a\u0430", None))
        self.btn_close.setText(QCoreApplication.translate("LogsWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        self.btn_save_graph.setText(QCoreApplication.translate("LogsWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a", None))
        self.btn_update_list.setText(QCoreApplication.translate("LogsWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a", None))
        self.label_2.setText(QCoreApplication.translate("LogsWindow", u"\u0414\u043b\u044f \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u0434\u0432\u0443\u0445 \u0433\u0440\u0430\u0444\u0438\u043a\u043e\u0432 \u043d\u0430 \u043e\u0434\u043d\u043e\u043c \u043f\u043e\u043b\u0435, \u0432\u044b\u0434\u0435\u043b\u0438\u0442\u0435 \u043d\u0443\u0436\u043d\u044b\u0435 \u043b\u043e\u0433\u0438 \u043c\u044b\u0448\u044c\u044e, \u0437\u0430\u0436\u0430\u0432 CTRL.", None))
        self.btn_save_graph_2.setText(QCoreApplication.translate("LogsWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0412\u0421\u0415 \u0433\u0440\u0430\u0444\u0438\u043a\u0438", None))
    # retranslateUi

