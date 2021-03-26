#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):

        self.setGeometry(300, 300, 380, 300)
        self.setWindowTitle('Figure')
        self.show()


    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()


    def draw(self, qp):

        qp.setBrush(QColor(200, 0, 0))
        qp.drawRect(90, 90, 90, 90)

        qp.setBrush(QColor(255, 80, 0, 160))
        qp.drawRect(180, 130, 110, 110)

        qp.setBrush(QColor(25, 0, 90, 200))
        qp.drawRect(180, 90, 110, 40)
        
        qp.setBrush(QColor(180, 0, 90, 200))
        qp.drawRect(90, 180, 90, 60)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    
    sys.exit(app.exec_())
