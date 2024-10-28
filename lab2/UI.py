import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from math import sin, cos, pi
import copy
import mover

class Canvas(QWidget):
    def __init__(self):
        super().__init__()
        self.size = 720, 970
        self.init_pixmap = QPixmap(self.size[0], self.size[1])
        self.init_pixmap.fill(Qt.white)
        self.canvas = QtWidgets.QLabel()
        self.canvas.setPixmap(self.init_pixmap)

        self.pen_color = QtGui.QColor(0, 0, 0)

        self.points_canvas = []
        self.lines_canvas = []
        self.circles_canvas = []
        self.points_real = []
        self.lines_real = []
        self.circles_real = []

    def paintEvent(self, e):
        painter = QPainter(self)
        rect = e.rect()
        painter.drawPixmap(rect, self.canvas.pixmap(), rect)
    
    def draw_text(self, qp, color, point, text):
        qp.setPen(QPen(color, 5))
        qp.drawText(point, text)

    def draw_point(self, qp, color, point):
        qp.setPen(QPen(color, 5))
        qp.drawPoint(point)
    
    def draw_line(self, qp, color, point1, point2):
        # self.draw_point(qp, color, point1)
        # self.draw_point(qp, color, point2)
        qp.setPen(QPen(color, 4))
        qp.drawLine(point1, point2)

    def draw_circle(self, qp, color, circle):
        # qp.setPen(QPen(color, 5))
        for i in range(len(circle) - 1):
            self.draw_line(qp, color, circle[i], circle[i + 1])

    # def clearAll(self):
    #     self.canvas_answer = []
    #     self.real_answer = []
    #     self.redraw_canvas()
    #     self.update()

    def set_state(self, state: dict):
        self.points_canvas = [QPoint(round(point[0]), round(point[1])) for point in state['points']]
        self.points_real = state['points']
        self.lines_canvas = [[QPoint(round(line[0][0]), round(line[0][1])), QPoint(round(line[1][0]), round(line[1][1]))] for line in state['lines']]
        self.lines_real = state['lines']
        self.circles_canvas = [[QPoint(round(point[0]), round(point[1])) for point in circle] for circle in state['circles']]
        self.circles_real = state['circles']
        self.redraw_canvas()

    def get_state(self) -> dict:
        state = dict()
        state['points'] = self.points_real
        state['lines'] = self.lines_real
        state['circles'] = self.circles_real
        return state

    def redraw_canvas(self):
        self.canvas.clear()
        self.canvas.setPixmap(self.init_pixmap)
        painter = QPainter(self.canvas.pixmap())
        for point in self.points_canvas:
            self.draw_point(painter, Qt.black, point)
        for line in self.lines_canvas:
            self.draw_line(painter, Qt.black, line[0], line[1])
        for circle in self.circles_canvas:
            self.draw_circle(painter, Qt.black, circle)
        painter.end()
        self.update()

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1720, 972)
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.canvas = Canvas()
        self.canvas.setVisible(True)
        self.prev_state = ()
        self.fig_center = [360, 485]

        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 1720, 972))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(720, 0, 1000, 950))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(30)
        # self.centralwidget.addWidget(self.canvas)
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_17 = QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        self.label_17.setSizePolicy(sizePolicy)

        self.verticalLayout_13.addWidget(self.label_17)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_19 = QLabel(self.gridLayoutWidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignCenter)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        self.label_19.setSizePolicy(sizePolicy)

        self.verticalLayout_14.addWidget(self.label_19)

        self.InAngleRotate = QLineEdit(self.gridLayoutWidget)
        self.InAngleRotate.setObjectName(u"InAngleRotate")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InAngleRotate.sizePolicy().hasHeightForWidth())
        self.InAngleRotate.setSizePolicy(sizePolicy)

        self.verticalLayout_14.addWidget(self.InAngleRotate)


        self.verticalLayout_13.addLayout(self.verticalLayout_14)


        self.gridLayout.addLayout(self.verticalLayout_13, 1, 1, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.BtnMove = QPushButton(self.gridLayoutWidget)
        self.BtnMove.setObjectName(u"BtnMove")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.BtnMove.sizePolicy().hasHeightForWidth())
        self.BtnMove.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.BtnMove)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 2, 1, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_16 = QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_16)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_23 = QLabel(self.gridLayoutWidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_23)

        self.InXCenterRotate = QLineEdit(self.gridLayoutWidget)
        self.InXCenterRotate.setObjectName(u"InXCenter")
        sizePolicy.setHeightForWidth(self.InXCenterRotate.sizePolicy().hasHeightForWidth())
        self.InXCenterRotate.setSizePolicy(sizePolicy)

        self.verticalLayout_18.addWidget(self.InXCenterRotate)


        self.verticalLayout_8.addLayout(self.verticalLayout_18)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_20 = QLabel(self.gridLayoutWidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_20)

        self.InYCenterRotate = QLineEdit(self.gridLayoutWidget)
        self.InYCenterRotate.setObjectName(u"InYCenter")
        sizePolicy.setHeightForWidth(self.InYCenterRotate.sizePolicy().hasHeightForWidth())
        self.InYCenterRotate.setSizePolicy(sizePolicy)

        self.verticalLayout_15.addWidget(self.InYCenterRotate)


        self.verticalLayout_8.addLayout(self.verticalLayout_15)


        self.gridLayout.addLayout(self.verticalLayout_8, 1, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_5)

        self.InXCenterScale = QLineEdit(self.gridLayoutWidget)
        self.InXCenterScale.setObjectName(u"InXCenterScale")
        sizePolicy.setHeightForWidth(self.InXCenterScale.sizePolicy().hasHeightForWidth())
        self.InXCenterScale.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.InXCenterScale)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_6)

        self.InYCenterScale = QLineEdit(self.gridLayoutWidget)
        self.InYCenterScale.setObjectName(u"InYCenterScale")
        sizePolicy.setHeightForWidth(self.InYCenterScale.sizePolicy().hasHeightForWidth())
        self.InYCenterScale.setSizePolicy(sizePolicy)

        self.verticalLayout_6.addWidget(self.InYCenterScale)


        self.verticalLayout_3.addLayout(self.verticalLayout_6)


        self.gridLayout.addLayout(self.verticalLayout_3, 2, 0, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label)

        self.InXMove = QLineEdit(self.gridLayoutWidget)
        self.InXMove.setObjectName(u"InXMove")
        sizePolicy.setHeightForWidth(self.InXMove.sizePolicy().hasHeightForWidth())
        self.InXMove.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.InXMove)


        self.verticalLayout_9.addLayout(self.verticalLayout_5)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_2)

        self.InYMove = QLineEdit(self.gridLayoutWidget)
        self.InYMove.setObjectName(u"InYMove")
        sizePolicy.setHeightForWidth(self.InYMove.sizePolicy().hasHeightForWidth())
        self.InYMove.setSizePolicy(sizePolicy)

        self.verticalLayout_10.addWidget(self.InYMove)


        self.verticalLayout_9.addLayout(self.verticalLayout_10)


        self.gridLayout.addLayout(self.verticalLayout_9, 0, 1, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_12.addItem(self.verticalSpacer_6)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_12.addItem(self.verticalSpacer_7)

        self.BtnScale = QPushButton(self.gridLayoutWidget)
        self.BtnScale.setObjectName(u"BtnScale")
        sizePolicy.setHeightForWidth(self.BtnScale.sizePolicy().hasHeightForWidth())
        self.BtnScale.setSizePolicy(sizePolicy)

        self.verticalLayout_12.addWidget(self.BtnScale)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_12.addItem(self.verticalSpacer_8)


        self.gridLayout.addLayout(self.verticalLayout_12, 2, 2, 1, 1)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_18 = QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_18)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_22 = QLabel(self.gridLayoutWidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_22)

        self.InXScale = QLineEdit(self.gridLayoutWidget)
        self.InXScale.setObjectName(u"InXScale")
        sizePolicy.setHeightForWidth(self.InXScale.sizePolicy().hasHeightForWidth())
        self.InXScale.setSizePolicy(sizePolicy)

        self.verticalLayout_19.addWidget(self.InXScale)


        self.verticalLayout_16.addLayout(self.verticalLayout_19)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_21 = QLabel(self.gridLayoutWidget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_21)

        self.InYScale = QLineEdit(self.gridLayoutWidget)
        self.InYScale.setObjectName(u"InYScale")
        sizePolicy.setHeightForWidth(self.InYScale.sizePolicy().hasHeightForWidth())
        self.InYScale.setSizePolicy(sizePolicy)

        self.verticalLayout_17.addWidget(self.InYScale)


        self.verticalLayout_16.addLayout(self.verticalLayout_17)


        self.gridLayout.addLayout(self.verticalLayout_16, 2, 1, 1, 1)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_20.addItem(self.verticalSpacer_9)

        self.center = QLabel(self.gridLayoutWidget)
        self.center.setObjectName(u"label_center")
        self.center.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.center)

        self.BtnBack = QPushButton(self.gridLayoutWidget)
        self.BtnBack.setObjectName(u"BtnBack")
        sizePolicy.setHeightForWidth(self.BtnBack.sizePolicy().hasHeightForWidth())
        self.BtnBack.setSizePolicy(sizePolicy)

        self.verticalLayout_20.addWidget(self.BtnBack)

        # self.verticalSpacer_10 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        # self.verticalLayout_20.addItem(self.verticalSpacer_10)

        self.BtnStart = QPushButton(self.gridLayoutWidget)
        self.BtnStart.setObjectName(u"BtnStart")
        sizePolicy.setHeightForWidth(self.BtnStart.sizePolicy().hasHeightForWidth())
        self.BtnStart.setSizePolicy(sizePolicy)

        self.verticalLayout_20.addWidget(self.BtnStart)

        # self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        # self.verticalLayout_20.addItem(self.verticalSpacer_11)


        self.gridLayout.addLayout(self.verticalLayout_20, 0, 0, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_11.addItem(self.verticalSpacer_4)

        self.BtnRotate = QPushButton(self.gridLayoutWidget)
        self.BtnRotate.setObjectName(u"BtnRotate")
        sizePolicy.setHeightForWidth(self.BtnRotate.sizePolicy().hasHeightForWidth())
        self.BtnRotate.setSizePolicy(sizePolicy)

        self.verticalLayout_11.addWidget(self.BtnRotate)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_11.addItem(self.verticalSpacer_5)

        # self.gridLayout.addWidget(self.center, 0, 0, 1, 1)

        self.gridLayout.addLayout(self.verticalLayout_11, 1, 2, 1, 1)

        self.gridLayout_2.addWidget(self.canvas, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.retranslateUi()
        self.draw_start()

        self.BtnStart.clicked.connect(self.draw_start)
        self.BtnMove.clicked.connect(self.move)
        self.BtnRotate.clicked.connect(self.rotate)
        self.BtnScale.clicked.connect(self.scale)
        self.BtnBack.clicked.connect(self.go_back)

        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle("Спутник")
        color = 'rgb(0, 0, 0)'
        background_color = 'rgb(230, 230, 230)'
        # shadow = background_color.darker(115).name()
        self.label_17.setText("Вращение")
        self.label_17.setFont(QFont('Arial', 18))
        self.label_17.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);")
        self.label_19.setText("Угол")
        self.label_19.setFont(QFont('Arial', 18))
        self.label_19.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);")
        self.BtnMove.setText("Выполнить перенос")
        self.BtnMove.setFont(QFont('Arial', 18))
        self.BtnMove.setStyleSheet('''
                            QPushButton:!pressed {'''
                                f'''color: {color};
                                background-color: {background_color};
                                border: 2px solid black'''
                            '}')
        self.label_16.setText("Центр вращения")
        self.label_16.setFont(QFont('Arial', 18))
        self.label_16.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);")
        self.label_23.setText("X")
        self.label_23.setFont(QFont('Arial', 18))
        self.label_23.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);")
        self.label_20.setText("Y")
        self.label_20.setFont(QFont('Arial', 18))
        self.label_20.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);")
        self.label_4.setText("Центр\nмасштабирования")
        self.label_4.setFont(QFont('Arial', 18))
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);")
        self.label_5.setText("X")
        self.label_5.setFont(QFont('Arial', 18))
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);")
        self.label_6.setText("Y")
        self.label_6.setFont(QFont('Arial', 18))
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);")
        self.label_3.setText("Перенос")
        self.label_3.setFont(QFont('Arial', 18))
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);")
        self.label.setText("dx")
        self.label.setFont(QFont('Arial', 18))
        self.label.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);")
        self.label_2.setText("dy")
        self.label_2.setFont(QFont('Arial', 18))
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);")
        self.BtnScale.setText("Выполнить\nмасштабирование")
        self.BtnScale.setFont(QFont('Arial', 18))
        self.BtnScale.setStyleSheet('''
                            QPushButton:!pressed {'''
                                f'''color: {color};
                                background-color: {background_color};
                                border: 2px solid black'''
                            '}')
        self.label_18.setText("Масштабирование")
        self.label_18.setFont(QFont('Arial', 18))
        self.label_18.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);")
        self.label_22.setText("kx")
        self.label_22.setFont(QFont('Arial', 18))
        self.label_22.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);")
        self.label_21.setText("ky")
        self.label_21.setFont(QFont('Arial', 18))
        self.label_21.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);")
        self.BtnBack.setText("Вернуться на 1 шаг назад")
        self.BtnBack.setFont(QFont('Arial', 18))
        self.BtnBack.setStyleSheet('''
                            QPushButton:!pressed {'''
                                f'''color: {color};
                                background-color: {background_color};
                                border: 2px solid black'''
                            '}')
        self.BtnStart.setText("Вернуть исходное состояние")
        self.BtnStart.setFont(QFont('Arial', 18))
        self.BtnStart.setStyleSheet('''
                            QPushButton:!pressed {'''
                                f'''color: {color};
                                background-color: {background_color};
                                border: 2px solid black'''
                            '}')
        self.BtnRotate.setText("Выполнить поворот")
        self.BtnRotate.setFont(QFont('Arial', 18))
        self.BtnRotate.setStyleSheet('''
                            QPushButton:!pressed {'''
                                f'''color: {color};
                                background-color: {background_color};
                                border: 2px solid black'''
                            '}')
        self.center.setText(f"Центр фигуры:\nX: ({self.fig_center[0]})\nY: ({self.fig_center[1]})")
        self.center.setFont(QFont('Arial', 18))
        self.center.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);")
        
        self.InAngleRotate.setFont(QFont("Arial", 15))
        self.InAngleRotate.setStyleSheet("QLineEdit"
                                "{"
                                "color : black;"
                                "border : 1px solid black;"
                                "background : white;"
                                "}")
        self.InXMove.setFont(QFont("Arial", 15))
        self.InXMove.setStyleSheet("QLineEdit"
                                "{"
                                "color : black;"
                                "border : 1px solid black;"
                                "background : white;"
                                "}")
        self.InYMove.setFont(QFont("Arial", 15))
        self.InYMove.setStyleSheet("QLineEdit"
                                "{"
                                "color : black;"
                                "border : 1px solid black;"
                                "background : white;"
                                "}")
        self.InXCenterRotate.setFont(QFont("Arial", 15))
        self.InXCenterRotate.setStyleSheet("QLineEdit"
                                "{"
                                "color : black;"
                                "border : 1px solid black;"
                                "background : white;"
                                "}")
        self.InYCenterRotate.setFont(QFont("Arial", 15))
        self.InYCenterRotate.setStyleSheet("QLineEdit"
                                "{"
                                "color : black;"
                                "border : 1px solid black;"
                                "background : white;"
                                "}")
        self.InXCenterScale.setFont(QFont("Arial", 15))
        self.InXCenterScale.setStyleSheet("QLineEdit"
                                "{"
                                "color : black;"
                                "border : 1px solid black;"
                                "background : white;"
                                "}")
        self.InYCenterScale.setFont(QFont("Arial", 15))
        self.InYCenterScale.setStyleSheet("QLineEdit"
                                "{"
                                "color : black;"
                                "border : 1px solid black;"
                                "background : white;"
                                "}")
        self.InXScale.setFont(QFont("Arial", 15))
        self.InXScale.setStyleSheet("QLineEdit"
                                "{"
                                "color : black;"
                                "border : 1px solid black;"
                                "background : white;"
                                "}")
        self.InYScale.setFont(QFont("Arial", 15))
        self.InYScale.setStyleSheet("QLineEdit"
                                "{"
                                "color : black;"
                                "border : 1px solid black;"
                                "background : white;"
                                "}")

    def draw_start(self):
        rads = pi / 180
        self.fig_center = [360, 485]
        state = dict()
        state['points'] = []
        state['lines'] = [[[210, 435], [260, 435]], [[260, 435], [235, 385]], 
                          [[235, 385], [335, 385]], [[335, 385], [360, 435]],
                          [[260, 435], [360, 435]], [[360, 435], [460, 435]],
                          [[460, 435], [495, 395]], [[210, 535], [260, 535]],
                          [[260, 535], [235, 585]], [[235, 585], [335, 585]],
                          [[335, 585], [360, 535]], [[260, 535], [360, 535]],
                          [[360, 535], [460, 535]], [[460, 535], [495, 575]]]
        state['circles'] = []
        circles = [[[210, 485], [50, 50], [90, 270]], [[460, 485], [10, 10], [0, 360]],
                   [[460, 485], [50, 50], [0, 360]]]
        # circles = []
        for circle in circles:
            circle_state = []
            for i in range(circle[2][0], circle[2][1] + 1):
                x0 = circle[0][0] + circle[1][0] * cos(i * rads)
                y0 = circle[0][1] + circle[1][1] * sin(i * rads)
                circle_state.append([round(x0), round(y0)])
            state['circles'].append(circle_state)
        self.canvas.set_state(state)
        self.update_center()
    
    def go_back(self):
        self.canvas.set_state(self.prev_state[0])
        self.fig_center = self.prev_state[1]
        self.update_center()

    def update_center(self):
        self.center.clear()
        self.center.setText(f"Центр фигуры:\nX: ({round(self.fig_center[0])})\nY: ({round(self.fig_center[1])})")

    def move(self):
        state = self.canvas.get_state()
        self.prev_state = copy.deepcopy(state), copy.deepcopy(self.fig_center)
        try:
            dx = float(self.InXMove.text() if self.InXMove.text() else 0)
            dy = float(self.InYMove.text() if self.InYMove.text() else 0)
        except ValueError:
            self.show_error()
            return
        state, self.fig_center = mover.move(state, self.fig_center, dx, dy)
        self.canvas.set_state(state)
        self.update_center()

    def rotate(self):
        state = self.canvas.get_state()
        self.prev_state = copy.deepcopy(state), copy.deepcopy(self.fig_center)
        try:
            angle = float(self.InAngleRotate.text() if self.InAngleRotate.text() else 0)
        except ValueError:
            self.show_error()
            return
        center = [int(self.InXCenterRotate.text() if self.InXCenterRotate.text() else self.fig_center[0]), 
                  int(self.InYCenterRotate.text() if self.InYCenterRotate.text() else self.fig_center[1])]
        state, self.fig_center = mover.rotate(state, center, angle, self.fig_center)
        self.canvas.set_state(state)
        self.update_center()

    def scale(self):
        state = self.canvas.get_state()
        self.prev_state = copy.deepcopy(state), copy.deepcopy(self.fig_center)
        kx = float(self.InXScale.text() if self.InXScale.text() else 1)
        ky = float(self.InYScale.text() if self.InYScale.text() else 1)
        center = [int(self.InXCenterScale.text() if self.InXCenterScale.text() else self.fig_center[0]), 
                  int(self.InYCenterScale.text() if self.InYCenterScale.text() else self.fig_center[1])]
        state, self.fig_center = mover.scale(state, center, kx, ky, self.fig_center)
        self.canvas.set_state(state)
        self.update_center()

    def show_error(self):
        error = QMessageBox(self)
        error.setWindowTitle("Ошибка")
        error.setIcon(QMessageBox.critical)
        error.exec_()
        error.show()
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.setStyleSheet('')
    window.show()
    app.exec_()