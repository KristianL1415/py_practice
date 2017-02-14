#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
PyQt5 tutorial

Create a window in PyQt5
"""

import sys, os
from PyQt5.QtWidgets import (QApplication, QWidget, QDesktopWidget, QToolTip, QPushButton, QMessageBox)
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QFont


class CustomWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is  a <b>QWidget</b> widget')

        btn = QPushButton('Quit', self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())

        self.resize(250, 150)
        self.center()
        self.setWindowTitle('Py Practice')

        self.show()

    def center(self):
        frame = self.frameGeometry()
        desktopCenter = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(desktopCenter)
        self.move(frame.topLeft())
        
    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Message", "Are you sure you want to quit?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'web.png')
    app.setWindowIcon(QIcon(path))
    cw = CustomWindow()
    sys.exit(app.exec_())
