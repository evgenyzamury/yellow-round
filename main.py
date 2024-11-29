import sys
import random

from PyQt6.QtCore import Qt, QRectF, QPoint
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QBrush, QColor
from PyQt6 import uic
from UI import Ui_MainWindow


class Suprematism(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.x = 370
        self.y = 150
        self.pushButton.clicked.connect(lambda x: self.update())

    def paintEvent(self, event):
        self.side = random.randint(20, 100)
        painter = QPainter(self)
        r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        brush = QBrush(QColor(r, g, b))
        painter.setBrush(brush)
        painter.drawEllipse(self.x - self.side, self.y - self.side, self.side * 2, self.side * 2)


def except_hook(cls, exeption, traceback):
    sys.__excepthook__(cls, exeption, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
