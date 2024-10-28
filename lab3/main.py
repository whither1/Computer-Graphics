import matplotlib
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from math import *
import time
import matplotlib.pyplot as plt

from algoritm import *
from mainwwindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.canvas_width = 750
        self.canvas_height = 800
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
        self.button_bench.clicked.connect(lambda: self.average_times(100, 1))
        #self.button_bench_2.clicked.connect(lambda: self.times_analysis(self.spin_length.value(), self.spin_angle.value()))
        self.push_line.clicked.connect(self.draw_line)
        self.button_spec.clicked.connect(lambda: self.draw_spectre(self.spin_length.value(), self.spin_angle.value()))
        self.button_clean.clicked.connect(self.canvas_clear)
        self.button_step.clicked.connect(lambda: self.steps_analysis(100, 1))

    def get_line(self):
        return [self.spin_sx.value(), self.spin_sy.value()], [self.spin_ex.value(), self.spin_ey.value()]

    def get_algo(self):
        return self.algorithms[self.combo_algo.currentIndex()]

    def get_color_otr(self):
        return QColor(*self.colors[self.combo_color.currentIndex()])

    def draw_line(self):
        if self.combo_algo.currentIndex() == 0:
            ans = self.cda()
            self.draw_default(ans, self.get_color_otr())
        elif self.combo_algo.currentIndex() == 1:
            ans = self.bres_float()
            self.draw_default(ans, self.get_color_otr())
        elif self.combo_algo.currentIndex() == 2:
            ans = self.bres_int()
            self.draw_default(ans, self.get_color_otr())
        elif self.combo_algo.currentIndex() == 3:
            ans = self.bresenham_del_steps()
            self.draw_with_intense(ans, self.get_color_otr())
        elif self.combo_algo.currentIndex() == 4:
            ans = self.wu_alg()
            self.draw_with_intense(ans, self.get_color_otr())
        elif self.combo_algo.currentIndex() == 5:
            data = self.get_line()
            self.lib_alg_draw(data, self.get_color_otr())

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

    def draw_with_intense(self, array, color):
        painter = QtGui.QPainter(self.label_10.pixmap())
        pen = painter.pen()
        pen.setWidth(1)
        my_color = QtGui.QColor(color)
        pen.setColor(my_color)
        painter.setPen(pen)
        for elem in array:
            my_color.setAlphaF(elem[2])
            pen.setColor(my_color)
            painter.setPen(pen)
            painter.drawPoint(elem[0] + int(self.canvas_width * 0.5), int(self.canvas_height * 0.5) - elem[1])
        pixmap = self.label_10.pixmap()
        self.label_10.setPixmap(pixmap)
        return 0

    def cda(self):
        data = self.get_line()
        ans = cda_a(data[0][0], data[0][1], data[1][0], data[1][1])[0]
        return ans

    def bres_float(self):
        data = self.get_line()
        ans = bres_float_a(data[0][0], data[0][1], data[1][0], data[1][1])[0]
        return ans

    def bres_int(self):
        data = self.get_line()
        ans = bres_int_a(data[0][0], data[0][1], data[1][0], data[1][1])[0]
        return ans

    def bresenham_del_steps(self):
        data = self.get_line()
        ans = bres_anti_a(data[0][0], data[0][1], data[1][0], data[1][1])[0]
        return ans

    def wu_alg(self):
        data = self.get_line()
        ans = wu_a(data[0][0], data[0][1], data[1][0], data[1][1])[0]
        return ans

    def lib_alg_draw(self, data, color):
        painter = QtGui.QPainter(self.label_10.pixmap())
        pen = painter.pen()
        pen.setWidth(1)
        pen.setColor(QtGui.QColor(color))
        painter.setPen(pen)
        x0 = int(data[0][0])
        y0 = int(data[0][1])
        x1 = int(data[1][0])
        y1 = int(data[1][1])
        painter.drawLine(x0 + int(self.canvas_width * 0.5), int(self.canvas_height * 0.5) - y0,
                         x1 + int(self.canvas_width * 0.5), int(self.canvas_height * 0.5) - y1, )
        pixmap = self.label_10.pixmap()
        self.label_10.setPixmap(pixmap)

    def draw_spectre(self, length, angle):
        angle = angle * pi / 180
        sum_angle = 0
        x0 = 0
        y0 = 0
        while sum_angle < pi * 2:
            x1 = length * cos(sum_angle)
            y1 = length * sin(sum_angle)
            if self.combo_algo.currentIndex() == 0:
                ans = cda_a(x0, y0, x1, y1)[0]
                self.draw_default(ans, self.get_color_otr())
            elif self.combo_algo.currentIndex() == 1:
                ans = bres_float_a(x0, y0, x1, y1)[0]
                self.draw_default(ans, self.get_color_otr())
            elif self.combo_algo.currentIndex() == 2:
                ans = bres_int_a(x0, y0, x1, y1)[0]
                self.draw_default(ans, self.get_color_otr())
            elif self.combo_algo.currentIndex() == 3:
                ans = bres_anti_a(x0, y0, x1, y1)[0]
                self.draw_with_intense(ans, self.get_color_otr())
            elif self.combo_algo.currentIndex() == 4:
                ans = wu_a(x0, y0, x1, y1)[0]
                self.draw_with_intense(ans, self.get_color_otr())
            elif self.combo_algo.currentIndex() == 5:
                self.lib_alg_draw([[x0, y0], [x1, y1]], self.get_color_otr())
            sum_angle += angle


    def plots_by_angles(self, fir, sec, thrd, frth, fifth, labels, head, y_label):
        font = {'weight': 'bold',
                'size': 18}
        matplotlib.rc('font', **font)
        fig, ax = plt.subplots(2, 3, figsize=(30, 30))
        fig.suptitle(head)
        fig.delaxes(ax[1][2])
        data = []
        angles = []
        for elem in fir:
            data.append(elem[0])
            angles.append(elem[1])
        ax[0][0].plot(angles, data)
        ax[0][0].set_title(labels[0])
        ax[0][0].set_xlabel("")
        ax[0][0].set_ylabel(y_label)

        data = []
        angles = []
        for elem in sec:
            data.append(elem[0])
            angles.append(elem[1])
        ax[0][1].plot(angles, data)
        ax[0][1].set_title(labels[1])
        ax[0][1].set_xlabel("")
        ax[0][1].set_ylabel("")

        data = []
        angles = []
        for elem in thrd:
            data.append(elem[0])
            angles.append(elem[1])
        ax[1][0].plot(angles, data)
        ax[1][0].set_title(labels[2])
        ax[1][0].set_xlabel("Угол, градусы")
        ax[1][0].set_ylabel(y_label)

        data = []
        angles = []
        for elem in frth:
            data.append(elem[0])
            angles.append(elem[1])
        ax[1][1].plot(angles, data)
        ax[1][1].set_title(labels[3])
        ax[1][1].set_xlabel("Угол, градусы")
        ax[1][1].set_ylabel("")

        data = []
        angles = []
        for elem in fifth:
            data.append(elem[0])
            angles.append(elem[1])
        ax[0][2].plot(angles, data)
        ax[0][2].set_title(labels[4])
        ax[0][2].set_xlabel("Угол, градусы")
        ax[0][2].set_ylabel("")

        plt.legend()
        plt.show()

    def steps_analysis(self, length, angle):
        step_angle = angle
        angle = angle * pi / 180
        sum_angle = 0
        x0 = 0
        y0 = 0
        cda = []
        bres_float = []
        bres_int = []
        bres_del = []
        wu = []
        print_angle = 0
        while sum_angle < pi / 2:
            x1 = length * cos(sum_angle)
            y1 = length * sin(sum_angle)

            steps = cda_a(x0, y0, x1, y1)[1]
            cda.append([steps, print_angle])

            steps = bres_float_a(x0, y0, x1, y1)[1]
            bres_float.append([steps, print_angle])

            steps = bres_int_a(x0, y0, x1, y1)[1]
            bres_int.append([steps, print_angle])

            steps = bres_anti_a(x0, y0, x1, y1)[1]
            bres_del.append([steps, print_angle])

            steps = wu_a(x0, y0, x1, y1)[1]
            wu.append([steps, print_angle])

            print_angle += step_angle
            sum_angle += angle
        labels = ["ЦДА", "Брезенхем(обычный)", "Брезенхем(целый)",
                  "Брезенхем(с устр ступ)", "Алгоритм Ву"]
        head = "Графики ступенчатости"
        self.plots_by_angles(cda, bres_float, bres_int, bres_del, wu, labels, head, "Количество ступенек")

    def plots_average(self, groups, data):
        font = {'weight': 'bold',
                'size': 18}
        matplotlib.rc('font', **font)
        plt.figure(figsize=(30, 20))
        plt.bar(groups, data)
        plt.ylabel("Среднее время, нс")
        plt.show()

    def average_times(self, length, angle):
        angle = angle * pi / 180
        sum_angle = 0
        x0 = 0
        y0 = 0
        cda = 0
        bres_ord = 0
        bres_int = 0
        bres_del = 0
        wu = 0
        cnt = 100
        angles_cnt = 0
        while sum_angle < pi * 2:
            angles_cnt += 5
            x1 = length * cos(sum_angle)
            y1 = length * sin(sum_angle)

            res = 0
            for i in range(cnt):
                start = time.perf_counter_ns()
                cda_a(x0, y0, x1, y1)
                end = time.perf_counter_ns()
                res += end - start
            cda += res / cnt

            res = 0
            for i in range(cnt):
                start = time.perf_counter_ns()
                bres_float_a(x0, y0, x1, y1)
                end = time.perf_counter_ns()
                res += end - start
            bres_ord += res / cnt

            res = 0
            for i in range(cnt):
                start = time.perf_counter_ns()
                bres_int_a(x0, y0, x1, y1)
                end = time.perf_counter_ns()
                res += end - start
            bres_int += res / cnt

            res = 0
            for i in range(cnt):
                start = time.perf_counter_ns()
                bres_anti_a(x0, y0, x1, y1)
                end = time.perf_counter_ns()
                res += end - start
            bres_del += res / cnt

            res = 0
            for i in range(cnt):
                start = time.perf_counter_ns()
                wu_a(x0, y0, x1, y1)
                end = time.perf_counter_ns()
                res += end - start
            wu += res / cnt
            sum_angle += angle

        bres_ord /= angles_cnt
        bres_int /= angles_cnt
        bres_del /= angles_cnt
        wu /= angles_cnt
        cda /= angles_cnt
        labels = ["ЦДА", "Брез(обычный)", "Брез(целый)",
                  "Брез(с устр)", "Ву"]
        self.plots_average(labels, [cda, bres_ord, bres_int, bres_del, wu])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()