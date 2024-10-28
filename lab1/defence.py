import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint, QObject, QRect, QMetaObject, QCoreApplication, QLine, QRegExp
from PyQt5.QtGui import QPen, QPainter, QPixmap, QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QHBoxLayout, QVBoxLayout, QLabel, QTableWidget, QSizePolicy, \
    QTextEdit, QSpacerItem, QPushButton, QTableWidgetItem, QLineEdit

import solver
import solver_def


class Canvas(QWidget):
    def __init__(self):
        super().__init__()
        self.size = 720, 720
        self.init_pixmap = QPixmap(self.size[0], self.size[1])
        self.init_pixmap.fill(Qt.white)
        self.canvas = QtWidgets.QLabel()
        self.canvas.setPixmap(self.init_pixmap)

        self.pen_color = QtGui.QColor(0, 0, 0)
        self.pressed = False
        self.button_used = Qt.LeftButton
        self.center = QPoint(0, 0)

        self.points = [QPoint(1, 360), QPoint(719, 360), QPoint(360, 1), QPoint(360, 719)]
        self.answer = None

    def mousePressEvent(self, e):
        if e.button() == self.button_used and (720 - e.pos().x() > 0 and 720 - e.pos().y() > 0):
            self.center = e.pos()
            self.add_to_list_points()
            self.redraw_canvas()
            self.update()

    def paintEvent(self, e):
        painter = QPainter(self)
        rect = e.rect()
        painter.drawPixmap(rect, self.canvas.pixmap(), rect)
        self.draw_point(painter)

    def draw_point(self, qp):
        qp.setPen(QPen(Qt.black, 5))
        qp.drawPoint(self.center)

    def draw_answer(self, qp):
        qp.setPen(QPen(Qt.red, 5))
        qp.drawLine(self.answer)

    def clearAll(self):
        self.points.clear()
        self.answer = None
        self.redraw_canvas()
        self.update()

    def add_point(self, x, y):
        self.center = QPoint(x, y)
        self.add_to_list_points()
        self.redraw_canvas()

    def set_answer(self, point1, point2):
        answer = solver.get_edge_points(self.size, point1, point2)
        self.answer = QLine(QPoint(answer[0][0], answer[0][1]), QPoint(answer[1][0], answer[1][1]))
        self.redraw_canvas()

    def delete_answer(self):
        self.answer = None
        self.redraw_canvas()

    def redraw_canvas(self):
        self.canvas.clear()
        self.canvas.setPixmap(self.init_pixmap)
        painter = QPainter(self.canvas.pixmap())
        for point in self.points:
            self.center = point
            self.draw_point(painter)
        if self.answer:
            self.draw_answer(painter)
        painter.end()
        self.center = QPoint(0, 0)
        self.update()

    def add_to_list_points(self):
        if len(self.points) == 0 or self.center != self.points[-1]:
            self.points.append(self.center)


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1728, 972)

        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.centralwidget.setObjectName("centralwidget")
        self.canvas = Canvas()
        grid = QGridLayout(self.centralwidget)
        grid.addWidget(self.canvas)

        self.points_list = self.canvas.points

        self.getResult = QPushButton(self.centralwidget)
        self.getResult.setGeometry(QRect(800, 180, 200, 50))
        self.getResult.setObjectName("getResult")
        self.getResult.setText('Найти решение')
        self.getResult.clicked.connect(self.get_result)

        self.getResult = QPushButton(self.centralwidget)
        self.getResult.setGeometry(QRect(1100, 180, 200, 50))
        self.getResult.setObjectName("getResult")
        self.getResult.setText('Очистить холст')
        self.getResult.clicked.connect(self.canvas.clearAll)

    def get_result(self):
        if len(self.points_list) > 2:
            res = solver_def.solve([(point.x(), point.y()) for point in self.points_list])
            self.canvas.set_answer(res[0], res[1])


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    app.exec_()
