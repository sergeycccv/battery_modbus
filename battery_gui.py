'''
pyside6-uic ui/main.ui -o ui_main.py
pysyde6-designer

'''

from PySide6.QtWidgets import QApplication, QMainWindow
import sys
import ui_main

app = QApplication(sys.argv)
window = QMainWindow()

ui_main.Ui_MainWindow().setupUi(window)

window.show()
sys.exit(app.exec())
