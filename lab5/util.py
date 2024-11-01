"""
    Drawing utilities.
"""

import tkinter as tk
from tkinter import messagebox
from time import time
import fill


def draw_line(img, line):
    """
        Draw line by setting pixels.
    """

    for dot in line:
        rgb = img.get(dot[0], dot[1])
        cur_color = "#{0:02x}{1:02x}{2:02x}".format(rgb[0], rgb[1], rgb[2])
        if cur_color == dot[2]:
            img.put("#FFFFFF", (dot[0], dot[1]))
        else:
            img.put(dot[2], (dot[0], dot[1]))

def bresenham_int(x_start, y_start, x_end, y_end, color):
    """
        Implementation of Bresenham integer algorithm.
    """

    dx = x_end - x_start
    dy = y_end - y_start

    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0

    e = 2*dy - dx
    y = 0

    dots = []

    for x in range(dx + 1):
        dots.extend([[x_start + x*xx + y*yx, y_start + x*xy + y*yy, color]])
        if e >= 0:
            y += 1
            e -= 2*dx
        e += 2*dy

    return dots


def measure_time(root):
    root.modelst.select_clear(0, 1)
    root.modelst.select_set(0)
    start = time()
    fill.fill(root)
    end = time()
    messagebox.showinfo("Временная характеристика",
                        f"Время, затраченно на закраску: {(end - start) / 1000} сек.")
