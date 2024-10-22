'''
pyside6-uic ui/main.ui -o ui_main.py
pysyde6-designer

'''

from PySide6.QtWidgets import QApplication, QMainWindow
import sys
import ui_main


class ExampleApp(QMainWindow, ui_main.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.statusBar.showMessage('Ожидание подключения...')


def main():
    app = QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
