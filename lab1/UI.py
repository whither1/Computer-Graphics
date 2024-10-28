import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint, QRect, QMetaObject, QCoreApplication, QLine, QRegExp
from PyQt5.QtGui import QPen, QPainter, QPixmap, QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QHBoxLayout, QVBoxLayout, QLabel, QTableWidget, QSizePolicy, \
    QSpacerItem, QPushButton, QTableWidgetItem, QLineEdit, QMessageBox

import solver

from math import pi


class Canvas(QWidget):
    def __init__(self):
        super().__init__()
        self.size = 720, 720
        self.x0 = 20
        self.x1 = self.size[0] - self.x0 - 50
        self.y0 = 20
        self.y1 = self.size[1] - self.y0
        self.step = 1
        # self.y_step = 1
        self.init_pixmap = QPixmap(self.size[0], self.size[1])
        self.init_pixmap.fill(Qt.white)
        self.canvas = QtWidgets.QLabel()
        self.canvas.setPixmap(self.init_pixmap)

        self.pen_color = QtGui.QColor(0, 0, 0)
        self.pressed = False
        self.button_used = Qt.LeftButton

        self.points = []
        self.real_answer = []
        self.canvas_answer = []
    
    def paintEvent(self, e):
        painter = QPainter(self)
        rect = e.rect()
        painter.drawPixmap(rect, self.canvas.pixmap(), rect)
        if self.pressed:
            self.draw_point(painter)

    def draw_text(self, qp, color, point, text):
        qp.setPen(QPen(color, 5))
        qp.drawText(QPoint(point.x() + 7, point.y()), text)

    def draw_point(self, qp, color, point):
        qp.setPen(QPen(color, 5))
        qp.drawPoint(point)
    
    def draw_line(self, qp, color, point1, point2):
        self.draw_point(qp, color, point1)
        self.draw_point(qp, color, point2)
        qp.setPen(QPen(color, 5))
        qp.drawLine(point1, point2)

    def draw_circle(self, qp, color, center, radius):
        self.draw_point(qp, color, center)
        qp.setPen(QPen(color, 5))
        qp.drawEllipse(center, radius, radius)

    def draw_answer(self, qp):
        for i in range(len(self.canvas_answer[0])):
            point1 = QPoint(self.canvas_answer[0][i][0], self.canvas_answer[0][i][1])
            point2 = QPoint(self.canvas_answer[0][i - 1][0], self.canvas_answer[0][i - 1][1])
            self.draw_line(qp, Qt.red, point1, point2)
        self.draw_circle(qp, Qt.green, QPoint(self.canvas_answer[1][0][0], self.canvas_answer[1][0][1]), self.canvas_answer[1][1])
        self.draw_circle(qp, Qt.blue, QPoint(self.canvas_answer[2][0][0], self.canvas_answer[2][0][1]), self.canvas_answer[2][1])
        for i in range(len(self.canvas_answer[0])):
            point = QPoint(self.canvas_answer[0][i][0], self.canvas_answer[0][i][1])
            point_real = self.real_answer[0][i]
            self.draw_text(qp, Qt.black, point, f"{point_real[0]}: ({point_real[1]}, {point_real[2]})")
        self.draw_text(qp, Qt.black, QPoint(self.canvas_answer[1][0][0], self.canvas_answer[1][0][1]), f"({self.real_answer[1][0]} {self.real_answer[1][1]})")
        self.draw_text(qp, Qt.black, QPoint(self.canvas_answer[2][0][0], self.canvas_answer[2][0][1]), f"({self.real_answer[2][0]} {self.real_answer[2][1]})")

    def clearAll(self):
        self.canvas_answer = []
        self.real_answer = []
        self.redraw_canvas()
        self.update()

    def add_point(self, x, y):
        self.center = QPoint(x, y)
        self.add_to_list_points()
        self.redraw_canvas()

    def delete_point(self, index):
        self.points.pop(index)
        self.redraw_canvas()

    def set_answer(self, answer: list):
        real_triangle = answer[0]
        real_outer_circle = answer[3]
        real_min_x = real_outer_circle[0][0] - real_outer_circle[1]
        real_max_x = real_outer_circle[0][0] + real_outer_circle[1]
        real_min_y = real_outer_circle[0][1] - real_outer_circle[1]
        real_circles = [answer[2], real_outer_circle]
        self.step = (real_max_x - real_min_x) / (self.x1 - self.x0)
        triangle = []
        format_triangle = []
        for point in real_triangle:
            i = 0
            j = 0
            while real_min_x + i * self.step < point[0]: i += 1
            while real_min_y + j * self.step < point[1]: j += 1
            triangle.append([self.x0 + i, self.y1 - j, real_triangle[2]])
            format_triangle.append([str(point[2]), format(point[0], '.2f'), format(point[1], '.2f')])
        self.canvas_answer.append(triangle)
        self.real_answer.append(format_triangle)
        for circle in real_circles:
            i = 0
            j = 0
            r = 0
            while real_min_x + i * self.step < circle[0][0]: i += 1
            while real_min_y + j * self.step < circle[0][1]: j += 1
            r = circle[1] / self.step
            self.canvas_answer.append([[self.x0 + i, self.y1 - j], r])
            self.real_answer.append([format(circle[0][0], '.2f'), format(circle[0][1], '.2f')])
        # self.answer = answer

    # def delete_answer(self):
        # self.answer = None
        # self.redraw_canvas()

    def redraw_canvas(self):
        self.canvas.clear()
        self.canvas.setPixmap(self.init_pixmap)
        painter = QPainter(self.canvas.pixmap())
        if self.canvas_answer:
            self.draw_answer(painter)
        painter.end()
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
        self.canvas.setVisible(True)
        # self.canvas.setStyleSheet("border-color: rgb(0, 0, 0);")
        grid = QGridLayout(self.centralwidget)
        grid.addWidget(self.canvas)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.points_list = []
        self.result = []
        # self.points_changed = []
        # self.canvas.points = self.points_list //TODO

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(730, 0, 990, 721))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout2")
        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        font = QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.points = QTableWidget(self.horizontalLayoutWidget)
        self.points.setObjectName("points")
        self.points.setColumnCount(2)
        # self.points.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.points.setHorizontalHeaderItem(0, QTableWidgetItem('X'))
        self.points.setHorizontalHeaderItem(1, QTableWidgetItem('Y'))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.points.sizePolicy().hasHeightForWidth())
        self.points.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.points)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.pointInputX = QLineEdit(self.horizontalLayoutWidget)
        self.pointInputX.setObjectName("pointInputX")
        reg_ex = QRegExp("^(-)?[0-9]+((\.)?[0-9]+)?$")
        v = QtGui.QRegExpValidator(reg_ex, self.pointInputX)
        self.pointInputX.setValidator(v)
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pointInputX.sizePolicy().hasHeightForWidth())
        self.pointInputX.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.pointInputX)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.pointInputY = QLineEdit(self.horizontalLayoutWidget)
        self.pointInputY.setObjectName("pointInputY")
        v = QtGui.QRegExpValidator(reg_ex, self.pointInputY)
        self.pointInputY.setValidator(v)
        sizePolicy2.setHeightForWidth(self.pointInputY.sizePolicy().hasHeightForWidth())
        self.pointInputY.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.pointInputY)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.addPoint = QPushButton(self.horizontalLayoutWidget)
        self.addPoint.setObjectName("addPoint")
        self.addPoint.clicked.connect(self.add_point)

        self.horizontalLayout_2.addWidget(self.addPoint)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName("label_6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_6)

        self.pointInputDeleteNumber = QLineEdit(self.horizontalLayoutWidget)
        self.pointInputDeleteNumber.setObjectName("pointInputDeleteNumber")
        reg_ex_del = QRegExp("^[1-9]+[0-9]*$")
        v = QtGui.QRegExpValidator(reg_ex_del, self.pointInputDeleteNumber)
        self.pointInputDeleteNumber.setValidator(v)
        sizePolicy2.setHeightForWidth(self.pointInputDeleteNumber.sizePolicy().hasHeightForWidth())
        self.pointInputDeleteNumber.setSizePolicy(sizePolicy2)

        self.horizontalLayout_6.addWidget(self.pointInputDeleteNumber)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.horizontalLayout_5.addLayout(self.horizontalLayout_6)

        self.deletePoint = QPushButton(self.horizontalLayoutWidget)
        self.deletePoint.setObjectName("deletePoint")
        self.deletePoint.clicked.connect(self.delete_point)

        self.horizontalLayout_5.addWidget(self.deletePoint)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 719, 711, 191))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_2)

        self.getResult = QPushButton(self.verticalLayoutWidget)
        self.getResult.setObjectName("getResult")
        self.getResult.clicked.connect(self.get_result)

        self.horizontalLayout_14.addWidget(self.getResult)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_9)

        self.verticalLayout_5.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.clearAll = QPushButton(self.verticalLayoutWidget)
        self.clearAll.setObjectName("clearAll")
        self.clearAll.clicked.connect(self.clear_all)

        self.horizontalLayout_13.addWidget(self.clearAll)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_10)

        self.deleteResult = QPushButton(self.verticalLayoutWidget)
        self.deleteResult.setObjectName("deleteResult")
        self.deleteResult.clicked.connect(self.delete_result)

        self.horizontalLayout_13.addWidget(self.deleteResult)

        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.label_result = QLabel(self.centralwidget)
        self.label_result.setObjectName("label_result")
        self.label_result.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.label_result.setGeometry(QRect(730, 725, 800, 200))
        # self.label_result.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.points.itemChanged.connect(self.log_change)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    # setupUi

    def retranslateUi(self):
        self.setWindowTitle("Lab 1")
        self.label_2.setText("Точки")
        self.label_2.setFont(QFont('Arial', 18))
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);")
        self.label_4.setText("X")
        self.label_4.setFont(QFont('Arial', 18))
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);")
        self.label_5.setText("Y")
        self.label_5.setFont(QFont('Arial', 18))
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);")
        self.label_6.setText("Номер")
        self.label_6.setFont(QFont('Arial', 18))
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);")
        self.label_result.setFont(QFont('Arial', 17))
        self.label_result.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);")


        color = 'rgb(0, 0, 0)'
        background_color = 'rgb(230, 230, 230)'
        self.addPoint.setText("Добавить точку")
        self.addPoint.setFont(QFont('Arial', 18))
        self.addPoint.setStyleSheet('''
                            QPushButton:!pressed {'''
                                f'''color: {color};
                                background-color: {background_color};
                                border: 2px solid black'''
                            '}')
        self.getResult.setText("Получить результат")
        self.getResult.setFont(QFont('Arial', 18))
        self.getResult.setStyleSheet('''
                            QPushButton:!pressed {'''
                                f'''color: {color};
                                background-color: {background_color};
                                border: 2px solid black'''
                            '}')
        self.clearAll.setText("Очистить всё")
        self.clearAll.setFont(QFont('Arial', 18))
        self.clearAll.setStyleSheet('''
                            QPushButton:!pressed {'''
                                f'''color: {color};
                                background-color: {background_color};
                                border: 2px solid black'''
                            '}')
        self.deleteResult.setText("Очистить результат")
        self.deleteResult.setFont(QFont('Arial', 18))
        self.deleteResult.setStyleSheet('''
                            QPushButton:!pressed {'''
                                f'''color: {color};
                                background-color: {background_color};
                                border: 2px solid black'''
                            '}')
        self.deletePoint.setText("Удалить точку")
        self.deletePoint.setFont(QFont('Arial', 18))
        self.deletePoint.setStyleSheet('''
                            QPushButton:!pressed {'''
                                f'''color: {color};
                                background-color: {background_color};
                                border: 2px solid black'''
                            '}')
        
        self.pointInputX.setFont(QFont("Arial", 15))
        self.pointInputX.setStyleSheet("QLineEdit"
                                "{"
                                "color : black;"
                                "border : 1px solid black;"
                                "background : white;"
                                "}")
        self.pointInputY.setFont(QFont("Arial", 15))
        self.pointInputY.setStyleSheet("QLineEdit"
                                "{"
                                "color : black;"
                                "border : 1px solid black;"
                                "background : white;"
                                "}")
        self.pointInputDeleteNumber.setFont(QFont("Arial", 15))
        self.pointInputDeleteNumber.setStyleSheet("QLineEdit"
                                "{"
                                "color : black;"
                                "border : 1px solid black;"
                                "background : white;"
                                "}")
        
        self.points.setFont(QFont("Arial", 15))
        self.points.setStyleSheet('''QTableWidget::item
                                  {
                                  color : black;
                                  background-color : white;
                                  }''')

    def add_point(self):
        if len(self.pointInputX.text()) != 0 and len(self.pointInputY.text()) != 0:
            try:
                # self.canvas.add_point(int(self.pointInputX.text()), int(self.pointInputY.text()))
                self.points_list.append([float(self.pointInputX.text()), float(self.pointInputY.text())])
                self.pointInputX.clear()
                self.pointInputY.clear()
                self.update()
            # print(self.points_list)
            except ValueError:
                self.show_error(2)
        else:
            self.show_error(2)

    def delete_point(self):
        if len(self.pointInputDeleteNumber.text()) != 0 and len(self.points_list) != 0:
            if int(self.pointInputDeleteNumber.text()) - 1 < len(self.points_list):
                self.points_list.pop(int(self.pointInputDeleteNumber.text()) - 1)
                self.pointInputDeleteNumber.clear()
                self.update()
                return
        self.show_error(3)

    def clear_all(self):
        self.points_list.clear()
        self.canvas.clearAll()
        self.label_result.clear()
        self.update()

    def log_change(self, item):
        self.clear_all
        try:
            self.points_list[item.row()][item.column()] = float(item.text())
        except ValueError:
            self.show_error(2)
            self.update()
            self.label_result.clear()
        else:
            self.canvas.clearAll()
            self.points.blockSignals(True)
            self.update()
            self.points.blockSignals(False)
            self.label_result.clear()

    def update(self):
        self.points.setRowCount(len(self.points_list))
        for i, point in enumerate(self.points_list):
            x = QTableWidgetItem(str(point[0]))
            y = QTableWidgetItem(str(point[1]))

            self.points.setItem(i, 0, x)
            self.points.setItem(i, 1, y)

    def get_result(self):
        if len(self.points_list) >= 3:
            self.canvas.clearAll()
            self.result = solver.solve([[point[0], point[1], i + 1] for i, point in enumerate(self.points_list)])
            if self.result:
                self.canvas.set_answer(self.result)
                self.show_result()
                # self.show_result(solver.get_line_coeffs(result[0], result[1]))
            else:
                self.show_error(4)
        else:
            self.show_error(1)

    def delete_result(self):
        self.canvas.clearAll()
        # self.show_result()
        self.label_result.clear()

    def show_result(self):
        self.label_result.clear()
        self.canvas.redraw_canvas()
        self.label_result.setText('\n'.join([f"Максимальная разность площадей: {format(self.result[1], '.2f')}",
                                  "Координаты точек треугольника:",
                                  '\n'.join(["{}: ({}, {})".format(point[2], format(point[0], '.2f'), format(point[1], '.2f')) for point in self.result[0]]),
                                  f"Площадь вписанной окружности: {format(self.result[2][1] ** 2 * pi, '.2f')}",
                                  f"Площадь описанной окружности: {format(self.result[3][1] ** 2 * pi, '.2f')}"]))

    def show_error(self, number):
        error_not_enough_elements = "Задайте минимум 3 точки"
        error_wrong_input = "Введите два вещественных числа"
        error_element_out_of_list = "Введите номер элемента из таблицы"
        error_unexpected = "Задайте минимум 3 точки, не лежащие на одной прямой"
        if number == 1:
            QMessageBox.critical(self, "Ошибка", error_not_enough_elements, buttons=QMessageBox.StandardButton.Ok)
        elif number == 2:
            QMessageBox.critical(self, "Ошибка", error_wrong_input, buttons=QMessageBox.StandardButton.Ok)
        elif number == 3:
            QMessageBox.critical(self, "Ошибка", error_element_out_of_list, buttons=QMessageBox.StandardButton.Ok)
        elif number == 4:
            QMessageBox.critical(self, "Ошибка", error_unexpected, buttons=QMessageBox.StandardButton.Ok)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    # window.setStyleSheet('')
    window.show()
    app.exec_()
