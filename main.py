import sys

from PyQt5 import uic
from random import choice
from PyQt5.QtGui import QBrush, QColor, QPainter
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1139, 866)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 121, 41))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1139, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Случайнык окружности"))
        self.pushButton.setText(_translate("MainWindow", "Жёлтый круг"))


class Canvas(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Canvas, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.flg = False

    def run(self):
        self.flg = True
        self.update()

    def paintEvent(self, event):
        if self.flg:
            painter = QPainter()
            painter.begin(self)
            self.draw(painter)
            painter.end()

    def draw(self, painter):
        painter.setBrush(QBrush(QColor(choice(range(0, 256)), choice(range(0, 256)), choice(range(0, 256)))))
        painter.setPen(QColor(0, 0, 0))
        x = choice(range(50, 1200))
        y = choice(range(50, 600))
        radius = choice(range(10, 300))
        painter.drawEllipse(x, y, radius, radius)
        self.flg = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cnv = Canvas()
    cnv.show()
    sys.exit(app.exec())
