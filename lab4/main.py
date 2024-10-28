import matplotlib
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from math import *
import time
import matplotlib.pyplot as plt
import matplotlib
import breeze_resources

from algoritm import *
from mainwwindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.canvas_width = 1100
        self.canvas_height = 1100
        self.background_color = [255, 255, 255]
        self.colors = [[0, 0, 255], [0, 0, 0], [255, 0, 0], [0, 255, 0], [255, 255, 255]]
        self.initUi()
        self.set_listeners()

    def initUi(self):
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.canvas_clear()

    def canvas_clear(self):
        canvas = QtGui.QPixmap(self.canvas_width, self.canvas_height)
        canvas.fill(Qt.GlobalColor.white)
        self.label_10.setPixmap(canvas)

    def set_listeners(self):
        self.button_bench.clicked.connect(self.circle_times)
        self.button_step.clicked.connect(self.ellypse_times)

        self.push_line.clicked.connect(self.draw_ellipse)
        self.push_line_2.clicked.connect(self.draw_circle)

        self.button_spec.clicked.connect(lambda: self.draw_circle_spectr(self.get_circle_spec()))
        self.button_spec_2.clicked.connect(lambda: self.draw_ellipse_spectr(self.get_ellipse_spec()))

        self.button_clean.clicked.connect(self.canvas_clear)

    def get_ellipse(self):
        return [self.spin_sx.value(), self.spin_sy.value()], [self.spin_ex.value(), self.spin_ey.value()]

    def get_ellipse_spec(self):
        return ([self.spin_sx.value(), self.spin_sy.value()], [self.start_x_e_spin.value(), self.start_y_e_spin.value()],
                self.step_e_spin.value(), self.num_e_spin.value())

    def get_circle_spec(self):
        return ([self.spin_sx.value(), self.spin_sy.value()], self.star_rad_spin.value(), self.end_rad_spin.value(),
                self.step_c_spin.value(), self.num_c_spin.value())

    def get_circle(self):
        return [self.spin_sx.value(), self.spin_sy.value()], [self.spin_ex_2.value(), self.spin_ex_2.value()]

    def get_color_otr(self):
        return QColor(*self.colors[self.combo_color.currentIndex()])

    def draw_ellipse(self):
        if self.combo_algo.currentIndex() == 0:
            ans = self.canonic_ellipse_create()
            self.draw_default(ans, self.get_color_otr())
        elif self.combo_algo.currentIndex() == 1:
            ans = self.param_ellipse_create()
            self.draw_default(ans, self.get_color_otr())
        elif self.combo_algo.currentIndex() == 2:
            ans = self.bres_ellipse_create()
            self.draw_default(ans, self.get_color_otr())
        elif self.combo_algo.currentIndex() == 3:
            ans = self.central_point_ellipse_create()
            self.draw_default(ans, self.get_color_otr())
        elif self.combo_algo.currentIndex() == 4:
            data = self.get_ellipse()
            self.lib_alg_figure_create(data, self.get_color_otr())

    def draw_circle(self):
        if self.combo_algo.currentIndex() == 0:
            ans = self.canonic_circle_create()
            self.draw_default(ans, self.get_color_otr())
        elif self.combo_algo.currentIndex() == 1:
            ans = self.param_circle_create()
            self.draw_default(ans, self.get_color_otr())
        elif self.combo_algo.currentIndex() == 2:
            ans = self.bres_circle_create()
            self.draw_default(ans, self.get_color_otr())
        elif self.combo_algo.currentIndex() == 3:
            ans = self.central_point_circle_create()
            self.draw_default(ans, self.get_color_otr())
        elif self.combo_algo.currentIndex() == 4:
            data = self.get_circle()
            self.lib_alg_figure_create(data, self.get_color_otr())

    def draw_default(self, array, color):
        painter = QtGui.QPainter(self.label_10.pixmap())
        pen = QPen()
        pen.setWidth(1)
        pen.setColor(QtGui.QColor(color))
        painter.setPen(pen)
        painter.fillRect(self.label_10.pixmap().rect(), QtGui.QColor(0, 0, 0, 0))
        for elem in array:
            painter.drawPoint(elem[0] + int(self.canvas_width * 0.5), int(self.canvas_height * 0.5) - elem[1])
        painter.end()
        self.label_10.update()

        return 0

    def draw_ellipse_spectr(self, data):
        x0 = data[0][0]
        y0 = data[0][1]
        r_x = data[1][0]
        r_y = data[1][1]
        step_x = data[2]
        number = data[3]
        while number > 0:
            if self.combo_algo.currentIndex() == 0:
                ans = canonic_ellipse([[x0, y0], [r_x, r_y]])
                self.draw_default(ans, self.get_color_otr())
            elif self.combo_algo.currentIndex() == 1:
                ans = param_ellipse([[x0, y0], [r_x, r_y]])
                self.draw_default(ans, self.get_color_otr())
            elif self.combo_algo.currentIndex() == 2:
                ans = bres_ellipse([[x0, y0], [r_x, r_y]])
                self.draw_default(ans, self.get_color_otr())
            elif self.combo_algo.currentIndex() == 3:
                ans = middle_point_ellipse([[x0, y0], [r_x, r_y]])
                self.draw_default(ans, self.get_color_otr())
            elif self.combo_algo.currentIndex() == 4:
                self.lib_alg_figure_create([[x0, y0], [r_x, r_y]], self.get_color_otr())
            number -= 1
            r_x_new = r_x + step_x
            r_y = (r_y * r_x_new) / r_x
            r_x = r_x_new

    def draw_circle_spectr(self, data):
        x0 = data[0][0]
        y0 = data[0][1]
        r_start = data[1]
        r_end = data[2]
        step_r = data[3]
        number = data[4]
        if (self.start_rad_c.isChecked() and self.end_rad_c.isChecked() and self.num_c_c.isChecked() and not(self.step_cir_c.isChecked())):
            step = (r_end - r_start) / (number - 1)
            while number > 0:
                if self.combo_algo.currentIndex() == 0:
                    ans = canonic_circle([[x0, y0], [r_start, r_start]])
                    self.draw_default(ans, self.get_color_otr())
                elif self.combo_algo.currentIndex() == 1:
                    ans = param_circle([[x0, y0], [r_start, r_start]])
                    self.draw_default(ans, self.get_color_otr())
                elif self.combo_algo.currentIndex() == 2:
                    ans = bres_circle([[x0, y0], [r_start, r_start]])
                    self.draw_default(ans, self.get_color_otr())
                elif self.combo_algo.currentIndex() == 3:
                    ans = middle_point_circle([[x0, y0], [r_start, r_start]])
                    self.draw_default(ans, self.get_color_otr())
                elif self.combo_algo.currentIndex() == 4:
                    self.lib_alg_figure_create([[x0, y0], [r_start, r_start]], self.get_color_otr())
                number -= 1
                r_start += step

        elif (self.start_rad_c.isChecked() and self.end_rad_c.isChecked() and self.step_cir_c.isChecked() and not(self.num_c_c.isChecked())):
            while r_start <= r_end:
                if self.combo_algo.currentIndex() == 0:
                    ans = canonic_circle([[x0, y0], [r_start, r_start]])
                    self.draw_default(ans, self.get_color_otr())
                elif self.combo_algo.currentIndex() == 1:
                    ans = param_circle([[x0, y0], [r_start, r_start]])
                    self.draw_default(ans, self.get_color_otr())
                elif self.combo_algo.currentIndex() == 2:
                    ans = bres_circle([[x0, y0], [r_start, r_start]])
                    self.draw_default(ans, self.get_color_otr())
                elif self.combo_algo.currentIndex() == 3:
                    ans = middle_point_circle([[x0, y0], [r_start, r_start]])
                    self.draw_default(ans, self.get_color_otr())
                elif self.combo_algo.currentIndex() == 4:
                    self.lib_alg_figure_create([[x0, y0], [r_start, r_start]], self.get_color_otr())
                r_start += step_r

        elif (self.start_rad_c.isChecked() and self.num_c_c.isChecked() and self.step_cir_c.isChecked() and not(self.end_rad_c.isChecked())):
            while number > 0:
                if self.combo_algo.currentIndex() == 0:
                    ans = canonic_circle([[x0, y0], [r_start, r_start]])
                    self.draw_default(ans, self.get_color_otr())
                elif self.combo_algo.currentIndex() == 1:
                    ans = param_circle([[x0, y0], [r_start, r_start]])
                    self.draw_default(ans, self.get_color_otr())
                elif self.combo_algo.currentIndex() == 2:
                    ans = bres_circle([[x0, y0], [r_start, r_start]])
                    self.draw_default(ans, self.get_color_otr())
                elif self.combo_algo.currentIndex() == 3:
                    ans = middle_point_circle([[x0, y0], [r_start, r_start]])
                    self.draw_default(ans, self.get_color_otr())
                elif self.combo_algo.currentIndex() == 4:
                    self.lib_alg_figure_create([[x0, y0], [r_start, r_start]], self.get_color_otr())
                number -= 1
                r_start += step_r

        elif (self.end_rad_c.isChecked() and self.num_c_c.isChecked() and self.step_cir_c.isChecked() and not(self.start_rad_c.isChecked())):
            while number > 0:
                if self.combo_algo.currentIndex() == 0:
                    ans = canonic_circle([[x0, y0], [r_end, r_end]])
                    self.draw_default(ans, self.get_color_otr())
                elif self.combo_algo.currentIndex() == 1:
                    ans = param_circle([[x0, y0], [r_end, r_end]])
                    self.draw_default(ans, self.get_color_otr())
                elif self.combo_algo.currentIndex() == 2:
                    ans = bres_circle([[x0, y0], [r_end, r_end]])
                    self.draw_default(ans, self.get_color_otr())
                elif self.combo_algo.currentIndex() == 3:
                    ans = middle_point_circle([[x0, y0], [r_end, r_end]])
                    self.draw_default(ans, self.get_color_otr())
                elif self.combo_algo.currentIndex() == 4:
                    self.lib_alg_figure_create([[x0, y0], [r_end, r_end]], self.get_color_otr())
                number -= 1
                r_end -= step_r
        else:
            QMessageBox.critical(self, "Ввод данных",
                                 "Пожалуйста выберете ровно три пунта из предложенных для опстроения спектра концентрических эллипсов.",
                                 buttons=QMessageBox.StandardButton.Ok)

    def canonic_ellipse_create(self):
        data = self.get_ellipse()
        ans = canonic_ellipse(data)
        return ans

    def param_ellipse_create(self):
        data = self.get_ellipse()
        ans = param_ellipse(data)
        return ans

    def bres_ellipse_create(self):
        data = self.get_ellipse()
        ans = bres_ellipse(data)
        return ans

    def middle_point_ellipse_create(self):
        data = self.get_ellipse()
        ans = middle_point_ellipse(data)
        return ans

    def canonic_circle_create(self):
        data = self.get_circle()
        ans = canonic_circle(data)
        return ans

    def param_circle_create(self):
        data = self.get_circle()
        ans = param_circle(data)
        return ans

    def bres_circle_create(self):
        data = self.get_circle()
        ans = bres_circle(data)
        return ans

    def middle_point_circle_create(self):
        data = self.get_circle()
        ans = middle_point_circle(data)
        return ans

    def lib_alg_figure_create(self, data, color):
        painter = QtGui.QPainter(self.label_10.pixmap())
        pen = painter.pen()
        pen.setWidth(1)
        pen.setColor(QtGui.QColor(color))
        painter.setPen(pen)
        x0 = int(data[0][0])
        y0 = int(data[0][1])
        r_x = int(data[1][0])
        r_y = int(data[1][1])
        painter.drawEllipse(QPoint(x0 + int(self.canvas_width * 0.5), int(self.canvas_height * 0.5) - y0), r_x, r_y)
        pixmap = self.label_10.pixmap()
        self.label_10.setPixmap(pixmap)


    def plots(self, labels, plots_y, plot_x, xlabel, ylabel):
        if len(plots_y) != len(labels):
            return
        plt.figure(figsize=(20, 20))
        font = {'weight': 'bold',
                'size': 18}
        matplotlib.rc('font', **font)
        for i in range(len(plots_y)):
            plt.plot(plot_x, plots_y[i], label=labels[i])

        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        plt.legend()
        plt.show()

    def circle_times(self):
        experiments_num = 150
        r_start = 10
        r_step = 100
        amount = 15
        canonical = []
        parametric = []
        bres = []
        mid_pnt = []
        x_axis = []
        for i in range(amount):
            times = 0.0
            for j in range(experiments_num):
                start = time.perf_counter_ns()
                canonic_circle([[0, 0], [r_start, r_start]])
                end = time.perf_counter_ns()
                times += (end - start)
            canonical.append([times / experiments_num])
            times = 0
            for j in range(experiments_num):
                start = time.perf_counter_ns()
                param_circle([[0, 0], [r_start, r_start]])
                end = time.perf_counter_ns()
                times += (end - start)
            parametric.append([times / experiments_num])
            times = 0
            for j in range(experiments_num):
                start = time.perf_counter_ns()
                bres_circle([[0, 0], [r_start, r_start]])
                end = time.perf_counter_ns()
                times += (end - start)
            bres.append([times / experiments_num])
            times = 0
            for j in range(experiments_num):
                start = time.perf_counter_ns()
                middle_point_circle([[0, 0], [r_start, r_start]])
                end = time.perf_counter_ns()
                times += (end - start)
            mid_pnt.append([times / experiments_num])
            x_axis.append(r_start)
            r_start += r_step

        labels = ["Брезенхем", "Параметрическое", "Каноническое", "Средняя точка"]
        self.plots(labels, [canonical, parametric, bres, mid_pnt], x_axis, "Радиус, пиксели",
                   "Время построения, нс")

    def ellypse_times(self):
        experiments_num = 150
        a_start = 30
        b_start = 10
        r_step = 100
        amount = 15
        canonical = []
        parametric = []
        bres = []
        mid_pnt = []
        x_axis = []
        for i in range(amount):
            times = 0
            for j in range(experiments_num):
                start = time.perf_counter_ns()
                canonic_ellipse([[0, 0], [a_start, b_start]])
                end = time.perf_counter_ns()
                times += (end - start)
            canonical.append([times / experiments_num])
            times = 0
            for j in range(experiments_num):
                start = time.perf_counter_ns()
                param_ellipse([[0, 0], [a_start, b_start]])
                end = time.perf_counter_ns()
                times += (end - start)
            parametric.append([times / experiments_num])
            times = 0
            for j in range(experiments_num):
                start = time.perf_counter_ns()
                bres_ellipse([[0, 0], [a_start, b_start]])
                end = time.perf_counter_ns()
                times += (end - start)
            bres.append([times / experiments_num])
            times = 0
            for j in range(experiments_num):
                start = time.perf_counter_ns()
                middle_point_ellipse([[0, 0], [a_start, b_start]])
                end = time.perf_counter_ns()
                times += (end - start)
            mid_pnt.append([times / experiments_num])
            x_axis.append(a_start)
            a_start += r_step
            b_start += r_step

        labels = ["Брезенхем", "Параметрическое", "Каноническое", "Средняя точка"]
        self.plots(labels, [canonical, parametric, bres, mid_pnt], x_axis, "Полуось a, пиксели",
                   "Время, нс")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    # set stylesheet
    file = QFile(":/light/stylesheet.qss")
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())
    window = MainWindow()
    window.show()
    app.exec()