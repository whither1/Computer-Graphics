# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 900)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 650))
        MainWindow.setMaximumSize(QtCore.QSize(1500, 1000))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(810, 10, 650, 850))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.spin_angle = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.spin_angle.setFont(font)
        self.spin_angle.setMinimum(-100.0)
        self.spin_angle.setMaximum(1000.0)
        self.spin_angle.setSingleStep(0.1)
        self.spin_angle.setProperty("value", 30.0)
        self.spin_angle.setObjectName("spin_angle")
        self.gridLayout_2.addWidget(self.spin_angle, 16, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 12, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 16, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 11, 0, 1, 2)
        self.spin_length = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.spin_length.setFont(font)
        self.spin_length.setMinimum(0.0)
        self.spin_length.setMaximum(1000.0)
        self.spin_length.setSingleStep(0.1)
        self.spin_length.setProperty("value", 200.0)
        self.spin_length.setObjectName("spin_length")
        self.gridLayout_2.addWidget(self.spin_length, 12, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        # font.setFamily("Lucida Grande")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 4, 0, 1, 1)
        self.spin_sx = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.spin_sx.setFont(font)
        self.spin_sx.setMinimum(-1000.0)
        self.spin_sx.setMaximum(1000.0)
        self.spin_sx.setProperty("value", 0.0)
        self.spin_sx.setObjectName("spin_sx")
        self.gridLayout_2.addWidget(self.spin_sx, 4, 1, 1, 1)
        self.combo_algo = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.combo_algo.setFont(font)
        self.combo_algo.setObjectName("combo_algo")
        self.combo_algo.addItem("")
        self.combo_algo.addItem("")
        self.combo_algo.addItem("")
        self.combo_algo.addItem("")
        self.combo_algo.addItem("")
        self.combo_algo.addItem("")
        self.gridLayout_2.addWidget(self.combo_algo, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 2)
        self.spin_ex = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.spin_ex.setFont(font)
        self.spin_ex.setDecimals(2)
        self.spin_ex.setMinimum(-1000.0)
        self.spin_ex.setMaximum(1000.0)
        self.spin_ex.setProperty("value", 0.0)
        self.spin_ex.setObjectName("spin_ex")
        self.gridLayout_2.addWidget(self.spin_ex, 6, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 5, 0, 1, 1)
        self.spin_ey = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.spin_ey.setFont(font)
        self.spin_ey.setMinimum(-1000.0)
        self.spin_ey.setMaximum(1000.0)
        self.spin_ey.setProperty("value", 0.0)
        self.spin_ey.setObjectName("spin_ey")
        self.gridLayout_2.addWidget(self.spin_ey, 7, 1, 1, 1)
        self.spin_sy = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.spin_sy.setFont(font)
        self.spin_sy.setMinimum(-1000.0)
        self.spin_sy.setMaximum(1000.0)
        self.spin_sy.setProperty("value", 0.0)
        self.spin_sy.setObjectName("spin_sy")
        self.gridLayout_2.addWidget(self.spin_sy, 5, 1, 1, 1)
        self.push_line = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.push_line.setFont(font)
        self.push_line.setObjectName("push_line")
        self.gridLayout_2.addWidget(self.push_line, 10, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        # font.setFamily("Arial")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 6, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 7, 0, 1, 1)
        self.combo_color = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.combo_color.setFont(font)
        self.combo_color.setObjectName("combo_color")
        self.combo_color.addItem("")
        self.combo_color.addItem("")
        self.combo_color.addItem("")
        self.combo_color.addItem("")
        self.combo_color.addItem("")
        self.gridLayout_2.addWidget(self.combo_color, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.button_spec = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_spec.setFont(font)
        self.button_spec.setObjectName("button_spec")
        self.gridLayout_2.addWidget(self.button_spec, 17, 0, 1, 2)
        self.gridLayout_2.setRowStretch(0, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_2)
        self.button_clean = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        # font.setFamily("Lucida Grande")
        font.setPointSize(14)
        self.button_clean.setFont(font)
        self.button_clean.setObjectName("button_clean")
        self.verticalLayout_4.addWidget(self.button_clean)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.button_bench = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_bench.setFont(font)
        self.button_bench.setObjectName("button_bench")
        self.verticalLayout_4.addWidget(self.button_bench)
        self.button_step = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_step.setFont(font)
        self.button_step.setObjectName("button_step")
        self.verticalLayout_4.addWidget(self.button_step)
        self.horizontalWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalWidget.setGeometry(QtCore.QRect(10, 0, 900, 900))
        self.horizontalWidget.setMinimumSize(QtCore.QSize(600, 600))
        self.horizontalWidget.setMaximumSize(QtCore.QSize(900, 900))
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_10 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_8.setText(_translate("MainWindow", "Выберете алгоритм построения и цвет отрезков и цвет экрана"))
        self.label_21.setText(_translate("MainWindow", "Длина отрезка"))
        self.label_7.setText(_translate("MainWindow", "Угол поворота"))
        self.label.setText(_translate("MainWindow", "Введите данные для построения спектра"))
        self.label_2.setText(_translate("MainWindow", "Начальная абсцисса отрезка x0:"))
        self.combo_algo.setItemText(0, _translate("MainWindow", "ЦДА"))
        self.combo_algo.setItemText(1, _translate("MainWindow", "Брезенхем (float)"))
        self.combo_algo.setItemText(2, _translate("MainWindow", "Брезенхем (int)"))
        self.combo_algo.setItemText(3, _translate("MainWindow", "Брезенхем (устр. ступ.)"))
        self.combo_algo.setItemText(4, _translate("MainWindow", "Ву"))
        self.combo_algo.setItemText(5, _translate("MainWindow", "Библиотечная функция"))
        self.label_5.setText(_translate("MainWindow", "Введите данные для построения отрезка"))
        self.label_11.setText(_translate("MainWindow", "Начальная ордината отрезка y0:"))
        self.push_line.setText(_translate("MainWindow", "Построить отрезок"))
        self.label_3.setText(_translate("MainWindow", "Конечная абсцисса отрезка x1:"))
        self.label_4.setText(_translate("MainWindow", "Цвет линий:"))
        self.label_9.setText(_translate("MainWindow", "Конечная ордината отрезка y1:"))
        self.combo_color.setItemText(0, _translate("MainWindow", "Синий"))
        self.combo_color.setItemText(1, _translate("MainWindow", "Чёрный"))
        self.combo_color.setItemText(2, _translate("MainWindow", "Красный"))
        self.combo_color.setItemText(3, _translate("MainWindow", "Зелёный"))
        self.combo_color.setItemText(4, _translate("MainWindow", "Белый"))
        self.label_6.setText(_translate("MainWindow", "Алгоритм построения:"))
        self.button_spec.setText(_translate("MainWindow", "Построить спектр"))
        self.button_clean.setText(_translate("MainWindow", "Очистить экран"))
        self.button_bench.setText(_translate("MainWindow", "Сравнение производительности"))
        self.button_step.setText(_translate("MainWindow", "Сравнение ступенчатости"))
        self.label_10.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())